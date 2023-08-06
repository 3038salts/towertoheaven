from cmu_graphics import *
from PIL import Image
import math
class Player:
    def __init__(self):
        self.spriteImage = None
        self.spriteList = None
        self.spriteCount = 0
        self.x = 0
        self.y = 0
        self.dx = 7
        self.dy = 0
        self.d2y = 0.2
        self.width = 0
        self.height = 0
        self.jumping = False
    
    def getSprites(self, file): #from Ray's cmu_graphics demos
        self.spriteImage = Image.open(file)
        self.spriteList = []
        for i in range(2):
            for j in range(3):
                #temporary sprite
                sprite = CMUImage(self.spriteImage.crop((132 + 1000 * j, 259 + 1200 * i, 1002 + 1000 * j, 1034 + 1200 * i)))
                self.spriteList.append(sprite)
    
    def drawPlayer(self): #from Ray's cmu_graphics demos
        sprite = self.spriteList[self.spriteCount]
        spriteWidth, spriteHeight = getImageSize(sprite)
        self.width = spriteWidth // 7
        self.height = spriteHeight // 7
        drawImage(sprite, self.x, self.y, width = self.width, height = self.height, align='center')
    
    def changeCoord(self, floor):
        pass
        # if floor != -1: #after entering tower
        #     self.x = app.width // 2
        #     self.y = app.height // 2

    def colliding(self): #keeps player in tower and not inside other objects
        if app.skyscraper.floor == -1:
            if self.x - (self.width // 2) < 0: #left bound for screen
                self.x = (self.width // 2)
            elif self.x + (self.width // 2) - app.dx > app.width: #right bound for screen
                self.x = app.width - (self.width // 2)
            for coord in app.coordsOfObjectsFloorNeg1:
                x, y, width, height = coord[0], coord[1], coord[2], coord[3]
                if (self.x + (self.width // 2) > x and #player right over left
                    self.x - (self.width // 2) < x + width and #player left over right
                    rounded(self.y - (self.height // 2) - self.dy) < y + height and #player top over bottom
                    rounded(self.y + (self.height // 2)) + self.dy) > y: #player bottom over top
                    return True
            return False
        elif app.skyscraper.floor >= 1:
            pass




        #     for x, y in app.skyscraper.stairCoords: #change to be app.listOfCoords later
        #         if (self.x + (self.width // 2) + app.dx > x and self.x - (self.width // 2) - app.dx < x and
        #             self.y + (self.height // 2) > y and self.y - (self.height // 2) < y + app.skyscraper.stairHeight):
        #             #left side of stair
        #             self.x = x - self.width // 2
        #         elif (self.x + (self.width // 2) + app.dx > x + app.skyscraper.stairWidth and
        #               self.x - (self.width // 2) - app.dx < x + app.skyscraper.stairWidth and
        #               self.y + (self.height // 2) > y and
        #               self.y - (self.height // 2) < y + app.skyscraper.stairHeight):
        #             #right side of stair
        #             #doesn't really apply because we can't get to the right side
        #             self.x = x + app.skyscraper.stairWidth + self.width // 2
        #         elif (self.y + (self.height // 2) > y and self.y - (self.height // 2) < y + app.skyscraper.stairHeight
        #               and self.x + (self.width // 2) > x and self.x - (self.width // 2) < x + app.skyscraper.stairWidth): #top side of stair
        #             self.y = y - (self.height // 2)
        #         # elif self.y - (self.height // 2) - app.dy <= y + app.skyscraper.stairHeight: #underside of stair
        #         #     self.y = app.skyscraper.stairHeight
        # else:
        #     #for the tower bounds
        #     if app.skyscraper.modifiedX + app.dx > self.x - (self.width // 2): #left bound
        #         app.mapX = self.x - (self.width // 2) - app.skyscraper.x - app.dx
        #     elif app.skyscraper.modifiedX + app.skyscraper.towerWidth - app.dx < self.x + (self.width // 2): #right bound
        #         app.mapX = self.x + (self.width // 2) - app.skyscraper.towerWidth - app.skyscraper.x + app.dx
        #     for x, y in app.skyscraper.stepCoords: #for the steps
        #         if (self.x + (self.width // 2) >= x - app.dx and self.x - (self.width // 2) + app.dx < x + app.skyscraper.stepWidth
        #         and self.y + (self.height // 2) >= y and self.y - (self.height // 2) <= y + app.skyscraper.stepHeight):
        #             return None

    def jump(self): #need to fix collision
        if app.skyscraper.floor == -1:
            if self.colliding() or self.y + (self.height // 2) > app.skyscraper.groundY: #player on surface
                self.dy = 0
                if self.y + (self.height // 2) > app.skyscraper.groundY:
                    self.y = app.skyscraper.groundY - (self.height // 2)
                elif self.colliding():
                    self.dy = -1
                    while self.colliding():
                        self.y += self.dy
                    self.dy = 0
                    # self.d2y = 0
                self.jumping = False
            else: #player in the air
                #tweak gravitational acceleration
                self.dy += self.d2y
                if self.colliding():
                    self.dy -= self.d2y
        elif app.skyscraper.floor >= 1:
            pass

    def load(self): #prob the same for each floor
        if app.skyscraper.floor == -1:
            self.x = 150
            self.y = app.height - 110 // 2
        else: #after entering
            self.x = app.width // 2
            self.y = 500    