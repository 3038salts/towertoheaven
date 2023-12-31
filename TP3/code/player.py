from cmu_graphics import *
from PIL import Image
class Player:
    def __init__(self):
        self.spriteList = None
        self.spriteCount = 0
        self.x = 0
        self.y = 0
        self.dx = 10
        self.dy = 0
        self.d2y = 0.8 # gravitational acceleration
        self.width = 0
        self.height = 0
        self.jumping = False
        self.moving = False
        self.health = 112
        self.getSprites()
        self.load()
    
    def getSprites(self): # from Ray's cmu_graphics demos
        # image source: https://bestanimations.com/gifs/kitty-run-art.html
        file = Image.open('../assets/player.gif')
        self.spriteList = []
        for frame in range(file.n_frames): # for every frame index
            file.seek(frame) # seek to the frame
            fr = file.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            fr = CMUImage(fr)
            self.spriteList.append(fr)
    
    def drawPlayer(self): # from Ray's cmu_graphics demos
        sprite = self.spriteList[self.spriteCount]
        self.width, self.height = getImageSize(sprite)
        drawImage(sprite, self.x, self.y, width = self.width,
                  height = self.height, align='center')
        self.drawPlayerStats()
    
    def drawPlayerStats(self):
        drawRect(10, 30, 170, 40, fill = rgb(25, 160, 195)) # brown
        drawLabel(f'HP: {self.health} Floor: {app.skyscraper.floor}', 95, 50,
                  size = 20, align = 'center')

    def colliding(self): # keeps player in tower and not inside other objects
        if self.x - (self.width // 2) < 0: # left bound for screen
            self.x = (self.width // 2)
        elif self.x + (self.width // 2) - app.dx > app.width:
            #right bound for screen
            self.x = app.width - (self.width // 2)
        if app.skyscraper.floor == 0:
            for coord in app.stairCoordsFloor0:
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
        elif 1 <= app.skyscraper.floor <= 3: #for the tower bounds
            if app.skyscraper.modifiedX > self.x - (self.width // 2):
                # left bound
                return True
            elif (app.skyscraper.modifiedX + app.skyscraper.towerWidth
                  < self.x + (self.width // 2)): #right bound
                return True
            for coord in app.stairCoordsFloor1: #collision checking
                x, y, width, height = coord[0], coord[1], coord[2], coord[3]
                if (self.x + (self.width // 2) > x and #player right over left
                    self.x - (self.width // 2) < x + width and #player L over R
                    rounded(self.y - (self.height // 2) - self.dy) < y + height
                    #player top over bottom 
                    and rounded(self.y + (self.height // 2)) + self.dy > y):
                    #player bottom over top
                    return True
        return False

    def jump(self): # enables jump with gravity
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

    def isDead(self):
        if self.health <= 0:
            self.health = 0
            return True
        return False

    def isTouchingEnemy(self):
        for enemy in app.enemyList:
            if (enemy.modifiedX + enemy.width // 2 > # enemy right over player left
                self.x - self.width // 2
                and enemy.modifiedX - (enemy.width // 2) < # enemy left over player right
                self.x + self.width // 2
                and rounded(enemy.modifiedY - (enemy.height // 2)) <
                # enemy top over player bottom 
                self.y + self.height // 2
                and rounded(enemy.modifiedY + (enemy.height // 2)) >
                self.y - self.width // 2):
                # enemy bottom over player top
                self.health -= 10
                return True
        return False

    def load(self): #prob the same for each floor after start
        if app.skyscraper.floor == 0:
            self.x = 150
            self.y = app.height - 110 // 2
        else: #after entering
            self.x = 500
            self.y = 730