from cmu_graphics import *
from PIL import Image
import os, pathlib

class Player:
    def __init__(self):
        self.spriteImage = None
        self.spriteList = None
        self.spriteCount = 0
        self.x = 0
    
    def getSprites(self, file):
        self.spriteImage = Image.open(file)
        self.spriteList = []
        for i in range(2):
            for j in range(3):
                sprite = CMUImage(self.spriteImage.crop((132 + 1000 * j, 259 + 1200 * i, 1002 + 1000 * j, 1034 + 1200 * i)))
                self.spriteList.append(sprite)
    
    def drawPlayer(self):
        sprite = self.spriteList[self.spriteCount]
        spriteWidth, spriteHeight = getImageSize(sprite)
        drawImage(sprite, 640, 400, width = spriteWidth // 7, height = spriteHeight // 7, align='center')
