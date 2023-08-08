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
        self.dx = 8
        self.dy = 0
        self.width = 0
        self.height = 0
        self.health = 100

    def getSprites(self): #from Ray's cmu_graphics demos
        file = '../assets/ghost.png'
        self.spriteImage = Image.open(file)
        self.spriteList = []
        for i in range(1):
            #temporary sprite
            sprite = CMUImage(self.spriteImage.crop((0, 0, 1247, 1280)))
            self.spriteList.append(sprite)
    
    def drawEnemy(self): #from Ray's cmu_graphics demos
        sprite = self.spriteList[self.spriteCount]
        spriteWidth, spriteHeight = getImageSize(sprite)
        self.width = spriteWidth // 7
        self.height = spriteHeight // 7
        drawImage(sprite, self.modifiedX, self.modifiedY, width = self.width,
                  height = self.height, align='center')
    
    def spawn(self):
        if app.skyscraper.floor == 1:
            x = random.randint(500, 800)
            y = random.randint(100, 600)
        app.enemyList.append(Enemy(x, y))
    
    def move(self): #move towards player
        if self.modifiedX > app.character.x:
            self.dx = -2
        elif self.modifiedX < app.character.x:
            self.dx = 2
        else:
            self.dx = 0
        if self.modifiedY > app.character.y:
            self.dy = -2
        elif self.modifiedY < app.character.y:
            self.dy = 2
        else:
            self.dy = 0
        self.x += self.dx
        self.y += self.dy
        self.modifiedX = app.mapX + self.x
        self.modifiedY = app.mapY + self.y

    def isHit(self):
        if app.bullet.isHit():
            pass

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)