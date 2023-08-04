from cmu_graphics import *
from PIL import Image
import os, pathlib, time

class Player:
    def __init__(self):
        self.spriteImage = None
        self.spriteList = None
        self.spriteCount = 0
        self.x = 150
        self.y = 750
        self.jumping = False
    
    def getSprites(self, file): #this part is from ray's demos but we might not use this code
        self.spriteImage = Image.open(file)
        self.spriteList = []
        for i in range(2):
            for j in range(3):
                sprite = CMUImage(self.spriteImage.crop((132 + 1000 * j, 259 + 1200 * i, 1002 + 1000 * j, 1034 + 1200 * i)))
                self.spriteList.append(sprite)
    
    def drawPlayer(self):
        sprite = self.spriteList[self.spriteCount]
        spriteWidth, spriteHeight = getImageSize(sprite)
        drawImage(sprite, self.x, self.y, width = spriteWidth // 7, height = spriteHeight // 7, align='center')
    
    def changeCoord(self, floor, mapX, mapY):
        if floor == -1: #before entering tower
            self.x = mapX + 900
            self.y = mapY
    
    def jump(self): #doesn't work yet
        self.jumping = True
        startTime = time.time()
        endTime = startTime + 1
        elapsedTime = 0
        startY = self.y
        while elapsedTime <= (endTime - startTime) * 60:
            print(elapsedTime)
            temp = (-0.1 * elapsedTime ** 2) + (6 * elapsedTime) + startY
            self.y = float(f'{temp:.2f}')
            if time.time() - elapsedTime > 1 / 60:
                elapsedTime = (time.time() - startTime) * 60
        self.jumping = False

    def load(self): #prob the same for each floor
        pass