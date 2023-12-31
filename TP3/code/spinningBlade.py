from cmu_graphics import * # cmu graphics module
from PIL import Image #
import random
class SpinningBlade():
    lastX = 300
    floatingLastX = 300
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
        self.r = self.height // 2 # circular hitbox
        drawImage(sprite, self.modifiedX, self.y, width = self.width,
                  height = self.height, align = 'center')

    def getSprites(self): # from Ray's cmu_graphics demos
        # image source: https://giphy.com/gifs/kays-kaysbetongsaging-betong
        # saging-lpw5Rnl86VNz0ZkGHl
        file = Image.open('../assets/blade.gif')
        self.spriteList = []
        for frame in range(file.n_frames): # for every frame index
            file.seek(frame) # seek to the frame
            fr = file.resize((file.size[0] // 2, file.size[1] // 2))
            fr = fr.transpose(Image.Transpose.FLIP_LEFT_RIGHT)
            fr = CMUImage(fr)
            self.spriteList.append(fr)

    def load(self):
        minSpace = 400
        self.width = self.height = 445
        if app.skyscraper.floor <= 3:
            xChange = random.randrange(0, 400)
            xRange = [SpinningBlade.lastX + minSpace, SpinningBlade.lastX +
                      minSpace + xChange]
            self.x = random.randrange(xRange[0], xRange[1])
            SpinningBlade.lastX = self.modifiedX = self.x
            self.y = 800
            app.bladeList.append(SpinningBlade(self.modifiedX, self.y))
        if 2 <= app.skyscraper.floor <= 3:
            xChange = random.randrange(20, 250)
            xFloatingChange = random.randrange(20, 200)
            first = SpinningBlade.floatingLastX + minSpace
            second = SpinningBlade.floatingLastX + minSpace + xFloatingChange
            xFloatingRange = [first, second]
            self.x = random.randrange(xFloatingRange[0], xFloatingRange[1])
            SpinningBlade.floatingLastX = self.modifiedX = self.x
            self.y = random.randint(320, 385)
            app.bladeList.append(SpinningBlade(self.modifiedX, self.y))

    def move(self):
        self.modifiedX = self.x + app.mapX
    
    def touchingPlayer(self):
        closestEdgeX, closestEdgeY = None, None
        if self.modifiedX < app.character.x - app.character.width // 2:
            closestEdgeX = app.character.x - app.character.width // 2
        elif self.modifiedX > app.character.x + app.character.width // 2:
            closestEdgeX = app.character.x + app.character.width // 2
        else:
            closestEdgeX = app.character.x
        if self.y < app.character.y - app.character.height // 2:
            closestEdgeY = app.character.y - app.character.height // 2
        elif self.y > app.character.y + app.character.height // 2:
            closestEdgeY = app.character.y + app.character.height // 2
        else:
            closestEdgeY = app.character.y
        if (distance(self.modifiedX, self.y, closestEdgeX, closestEdgeY)
            <= self.r):
            return True
        return False

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)