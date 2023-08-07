from cmu_graphics import *
from PIL import Image
import random
class Enemy:
    def __init__(self):
        self.spriteImage = None
        self.spriteList = None
        self.spriteCount = 0
        self.x = 0
        self.y = 0
        self.dx = 8
        self.dy = 0
        self.width = 0
        self.height = 0

    def getSprites(self, file): #from Ray's cmu_graphics demos
        self.spriteImage = Image.open(file)
        self.spriteList = []
        for i in range(1):
            #temporary sprite
            sprite = CMUImage(self.spriteImage.crop((0, 0, 1247, 1280)))
            self.spriteList.append(sprite)
    
    def drawEnemy(self): #from Ray's cmu_graphics demos
        # ghost png from https://purepng.com/photo/3928/clipart-halloween-ghost-clipart
        sprite = self.spriteList[self.spriteCount]
        spriteWidth, spriteHeight = getImageSize(sprite)
        self.width = spriteWidth // 7
        self.height = spriteHeight // 7
        drawImage(sprite, self.x, self.y, width = self.width,
                  height = self.height, align='center')
    
    def load(self):
        self.x = random.randint(500, 700)
        self.y = app.height - 300
    
    def move(self): #move towards player
        if self.x > app.character.x:
            self.dx = -1
        elif self.x < app.character.x:
            self.dx = 1
        else:
            self.dx = 0
        if self.y > app.character.y:
            self.dy = -1
        elif self.y < app.character.y:
            self.dy = 1
        else:
            self.dy = 0
        self.x += self.dx
        self.y += self.dy


    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)