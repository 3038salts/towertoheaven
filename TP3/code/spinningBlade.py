from cmu_graphics import * # cmu graphics module
from PIL import Image #
import random
class SpinningBlade():
    lastX = 800
    def __init__(self, x, y):
        self.modifiedX = self.x = x
        self.y = y
        self.r = 0
        self.width = 0
        self.height = 0
        self.spriteList = []
        self.spriteCount = 0
        self.getSprites()
    
    def drawBlade(self):
        sprite = self.spriteList[self.spriteCount]
        self.width, self.height = getImageSize(sprite)
        self.r = self.height // 2 # circular hitbox for a square image
        drawImage(sprite, self.modifiedX, self.y, width = self.width,
                  height = self.height, align = 'center')

    def getSprites(self): # from Ray's cmu_graphics demos
        # image source: https://giphy.com/gifs/kays-kaysbetongsaging-betongsaging-lpw5Rnl86VNz0ZkGHl
        file = Image.open('../assets/blade.gif')
        self.spriteList = []
        for frame in range(file.n_frames): # for every frame index
            file.seek(frame) # seek to the frame
            fr = file.resize((file.size[0] // 2, file.size[1] // 2)) # width, height
            fr = fr.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            fr = CMUImage(fr)
            self.spriteList.append(fr)

    def load(self):
        if app.skyscraper.floor == 1: #after entering
            xChange = random.randrange(200, 400)
            xRange = [SpinningBlade.lastX, SpinningBlade.lastX + xChange]
            SpinningBlade.lastX = self.modifiedX = self.x = random.randrange(xRange[0], xRange[1])
            self.y = 800
            self.width = self.height = 445
            app.bladeList.append(SpinningBlade(self.modifiedX, self.y))

    def move(self):
        self.modifiedX = self.x + app.mapX
    
    def touchingPlayer(self):
        if (distance(self.modifiedX, self.y, app.character.x,
                     app.character.y) <= self.r):
            return True
        return False

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)