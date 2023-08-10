from cmu_graphics import *
from PIL import Image
import random
# image source: https://purepng.com/photo/3928/clipart-halloween-ghost-clipart
class Enemy:
    def __init__(self, x, y):
        self.spriteImage = None
        self.spriteList = None
        self.spriteCount = 0
        self.modifiedX = self.x = x
        self.modifiedY = self.y = y
        self.dx = 0
        self.dy = 0
        self.width = 0
        self.height = 0
        self.health = 100
        self.getSprites()

    def getSprites(self): #from Ray's cmu_graphics demos
        file = '../assets/ghost.png'
        self.spriteImage = Image.open(file)
        self.spriteList = []
        for i in range(1):
            #temporary sprite
            sprite = CMUImage(self.spriteImage.crop((0, 0, 1247, 1280)))
            self.spriteList.append(sprite)
        spriteWidth, spriteHeight = getImageSize(sprite)
        self.width = spriteWidth // 7
        self.height = spriteHeight // 7
    
    def drawEnemy(self): #from Ray's cmu_graphics demos
        sprite = self.spriteList[self.spriteCount]
        drawImage(sprite, self.modifiedX, self.modifiedY, width = self.width,
                  height = self.height, align='center')
    
    def spawn(self):
        if app.skyscraper.floor == 1:
            xRange = [800, 2560]
        elif app.skyscraper.floor == 2:
            xRange = [800, 5120]
        elif app.skyscraper.floor == 3:
            pass
        yRange = [200, 600]
        newEnemyX = random.randint(xRange[0], xRange[1])
        newEnemyY = random.randint(yRange[0], yRange[1])
        while self.isLegal(newEnemyX, newEnemyY) == False:
            newEnemyX = random.randint(xRange[0], xRange[1])
            newEnemyY = random.randint(yRange[0], yRange[1])
        app.enemyList.append(Enemy(newEnemyX, newEnemyY))
    
    def isLegal(self, newEnemyX, newEnemyY):
        for coord in app.stairCoordsFloor1: # collision checking
            x, y, width, height = coord[0], coord[1], coord[2], coord[3]
            if (newEnemyX + (self.width // 2) > x and # ghost right over left
                newEnemyX - (self.width // 2) < x + width and # ghost L over R
                rounded(newEnemyY - (self.height // 2)) < y + height
                # ghost top over bottom 
                and rounded(newEnemyY + (self.height // 2)) > y):
                # ghost bottom over top
                return False
        if (newEnemyX + self.width // 2 > # ghost right over player left
            app.character.x - app.character.width // 2
            and newEnemyX - (self.width // 2) < # ghost left over player right
            app.character.x + app.character.width // 2
            and rounded(newEnemyY - (self.height // 2)) <
            # ghost top over player bottom 
            app.character.y + app.character.height // 2
            and rounded(newEnemyY + (self.height // 2)) >
            app.character.y - app.character.width // 2):
            # ghost bottom over player top
            return False
        return True
    
    def move(self): #move towards player
        if self.modifiedX > app.character.x:
            self.dx = -4
        elif self.modifiedX < app.character.x:
            self.dx = 4
        else:
            self.dx = 0
        if self.modifiedY > app.character.y:
            self.dy = -4
        elif self.modifiedY < app.character.y:
            self.dy = 4
        else:
            self.dy = 0
        self.x += self.dx
        self.y += self.dy
        self.modifiedX = app.mapX + self.x
        self.modifiedY = app.mapY + self.y
            
    def isHit(self): # checks if ghost is hit by a bullet
        # automatically deletes bullet and depeletes the health of ghost
        for bullet in app.bulletList:
            if (bullet.x + bullet.width // 2 > # bullet right over ghost left
                self.modifiedX - self.width // 2
                and bullet.x - (bullet.width // 2) < # bullet left over ghost right
                self.modifiedX + self.width // 2
                and rounded(bullet.y - (bullet.height // 2)) <
                # bullet top over ghost bottom 
                self.modifiedY + self.height // 2
                and rounded(bullet.y + (bullet.height // 2)) >
                self.modifiedY - self.width // 2):
                # bullet bottom over ghost top
                app.bulletList.remove(bullet)
                self.health -= 10
                if self.health == 0: # ghost dies
                    app.enemyList.remove(self)
                return True
        return False