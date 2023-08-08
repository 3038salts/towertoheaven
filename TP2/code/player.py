from cmu_graphics import *
from PIL import Image
'''image source: https://www.freepik.com/free-vector/hand-drawn-animation-
frames-element-collection_33591464.htm#query=sprite%20sheets&position=2&from_
view=keyword&track=ais)'''
class Player:
    def __init__(self):
        self.spriteImage = None
        self.spriteList = None
        self.spriteCount = 0
        self.x = 0
        self.y = 0
        self.dx = 8
        self.dy = 0
        self.d2y = 0.32 #gravitational acceleration
        self.width = 0
        self.height = 0
        self.jumping = False
        self.getSprites()
        self.load()
    
    def getSprites(self): #from Ray's cmu_graphics demos
        file = '../assets/player.jpg'
        self.spriteImage = Image.open(file)
        self.spriteList = []
        for i in range(2):
            for j in range(3):
                #temporary sprite
                sprite = CMUImage(self.spriteImage.crop((132 + 1000 * j,
                259 + 1200 * i, 1002 + 1000 * j, 1034 + 1200 * i)))
                self.spriteList.append(sprite)
    
    def drawPlayer(self): #from Ray's cmu_graphics demos
        sprite = self.spriteList[self.spriteCount]
        spriteWidth, spriteHeight = getImageSize(sprite)
        self.width = spriteWidth // 7
        self.height = spriteHeight // 7
        drawImage(sprite, self.x, self.y, width = self.width,
                  height = self.height, align='center')

    def colliding(self): #keeps player in tower and not inside other objects
        if self.x - (self.width // 2) < 0: #left bound for screen
            self.x = (self.width // 2)
        elif self.x + (self.width // 2) - app.dx > app.width:
            #right bound for screen
            self.x = app.width - (self.width // 2)
        if app.skyscraper.floor == 0:
            for coord in app.coordsOfObjectsFloor0:
                x, y, width, height = coord[0], coord[1], coord[2], coord[3]
                if (self.x + (self.width // 2) > x and
                    #player right over left
                    self.x - (self.width // 2) < x + width and
                    #player left over right
                    rounded(self.y - (self.height // 2) - self.dy) < y + height
                    #player top over bottom 
                    and rounded(self.y + (self.height // 2)) + self.dy > y):
                    #player bottom over top
                    return True
            return False
        elif app.skyscraper.floor >= 1: #for the tower bounds
            if app.skyscraper.modifiedX > self.x - (self.width // 2):
                # left bound
                # app.mapX = self.x - (self.width // 2) - app.skyscraper.x
                # - app.dx
                return True
            elif (app.skyscraper.modifiedX + app.skyscraper.towerWidth
                  < self.x + (self.width // 2)): #right bound
                # app.mapX = self.x + (self.width // 2) -
                # app.skyscraper.towerWidth - app.skyscraper.x + app.dx
                return True
            for coord in app.coordsOfObjectsFloor1: #collision checking
                x, y, width, height = coord[0], coord[1], coord[2], coord[3]
                if (self.x + (self.width // 2) > x and #player right over left
                    self.x - (self.width // 2) < x + width and #player L over R
                    rounded(self.y - (self.height // 2) - self.dy) < y + height
                    #player top over bottom 
                    and rounded(self.y + (self.height // 2)) + self.dy > y):
                    #player bottom over top
                    return True
                # if (self.x + (self.width // 2) >= x - app.dx and self.x - (self.width // 2) + app.dx < x + width
                # and self.y + (self.height // 2) >= y and self.y - (self.height // 2) <= y + height):
                #     return True
        return False

    def jump(self): # enables jump with gravity
        # if app.skyscraper.floor == 0:
        #player on surface or hit something
        if (self.colliding() or self.y + (self.height // 2) >
            app.skyscraper.groundY):
            if self.y + (self.height // 2) > app.skyscraper.groundY:
                self.dy = 0
                self.y = app.skyscraper.groundY - (self.height // 2)
            elif self.colliding() and self.dy < 0:
                self.dy = 1
                while self.colliding():
                    self.y += self.dy
            elif self.colliding and self.dy > 0:
                self.dy = -1
                while self.colliding():
                    self.y += self.dy
            self.dy = 0
            self.jumping = False
        else: # player in the air
            # gravitational acceleration
            self.dy += self.d2y
            if self.colliding():
                self.dy -= self.d2y

    def load(self): #prob the same for each floor after start
        if app.skyscraper.floor == 0:
            self.x = 150
            self.y = app.height - 110 // 2
        else: #after entering
            self.x = 200
            self.y = 730