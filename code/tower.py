from cmu_graphics import *
class Tower:
    def __init__(self, x, y):
        self.floor = 0
        self.totalFloors = 3
        self.x = x
        self.y = y
    
    def drawTower(self):
        if self.floor == -1:
            drawRect(900, 200, app.width - 900, app.height - 200, fill = 'gray')
            drawRect(1000, 500, app.width - 1100, app.height - 600, fill = 'red')
        else:
            drawRect(self.x, self.y, app.width - 900, app.height - 200, fill = 'gray')
            drawRect(self.x + 100, self.y + 300, app.width - 1100, app.height - 600, fill = 'red')
    
    def changeCoord(self, mapX, mapY):
        self.x = mapX
        self.y = mapY