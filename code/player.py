from cmu_graphics import *
from PIL import Image

class Player:
    def __init__(self):
        self.spriteImage = None
        self.spriteList = None
        self.spriteCount = 0
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.jumping = False
    
    def getSprites(self, file): #from Ray's cmu_graphics demos
        self.spriteImage = Image.open(file)
        self.spriteList = []
        for i in range(2):
            for j in range(3):
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
    
    def notColliding(self): #keeps player in tower and not inside other objects
       if app.skyscraper.floor == -1:
           pass
       else:
            #for the tower bounds
            if app.skyscraper.modifiedx + app.dx > self.x - (self.width // 2): #left bound
                app.mapx = self.x - (self.width // 2) - app.skyscraper.x - app.dx
            elif app.skyscraper.modifiedx + app.skyscraper.towerWidth - app.dx < self.x + (self.width // 2): #right bound
                app.mapx = self.x + (self.width // 2) - app.skyscraper.towerWidth - app.skyscraper.x + app.dx
            for x, y in app.skyscraper.stepCoords: #for the steps
                if (self.x + (self.width // 2) >= x - app.dx and self.x - (self.width // 2) + app.dx < x + app.skyscraper.stepWidth
                and self.y + (self.height // 2) >= y - app.dy and self.y - (self.height // 2) <= y + app.skyscraper.stepHeight + app.dy):
                    return None
            return None
        
    # def jump(self): #doesn't work yet
    #     self.jumping = True
    #     startTime = time.time()
    #     endTime = startTime + 1
    #     elapsedTime = 0
    #     startY = self.y
    #     while elapsedTime <= (endTime - startTime) * 60:
    #         print(elapsedTime)
    #         temp = (-0.1 * elapsedTime ** 2) + (6 * elapsedTime) + startY
    #         self.y = float(f'{temp:.2f}') #cite if needed
    #         if time.time() - elapsedTime > 1 / 60:
    #             elapsedTime = (time.time() - startTime) * 60
    #     self.jumping = False

    def load(self): #prob the same for each floor
        if app.skyscraper.floor == -1:
            self.x = 150
            self.y = 750
        else: #after entering
            self.x = app.width // 2
            self.y = 500