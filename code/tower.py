from cmu_graphics import *
class Tower:
    def __init__(self):
        self.floor = -1
        self.totalFloors = 3
        self.x = 900
        self.y = 0
    
    def drawTower(self):
        if self.floor == -1: #before entering tower
            #tower is in a fixed position
            towerWidth = app.width - 900
            towerHeight = app.height - 400
            drawRect(self.x, self.y, towerWidth, towerHeight, fill = 'gray')
            drawRect(self.x + (towerWidth // 4), self.y + towerHeight // 2, towerWidth // 2, towerHeight // 2, fill = 'brown')
            self.drawStartStairs()
        # else:
            # drawRect(self.x, self.y, app.width - 900, app.height - 200, fill = 'gray')
            # drawRect(self.x + 100, self.y + 300, app.width - 1100, app.height - 600, fill = 'red')
    
    def drawStartStairs(self):
        stairCoords = []
        colors = [rgb(186, 205, 252), rgb(252, 200, 186), rgb(238, 252, 186), rgb(205, 252, 186), rgb(252, 186, 205)]
        y = 720
        dy = 80
        dx = 155
        startX = app.width - (dx * 5) - 70
        for x in range(startX, app.width - dx, dx):
            stairCoords.append((x, y))
            y -= dy
        for i in range(len(stairCoords)):
            drawRect(stairCoords[i][0], stairCoords[i][1], dx, dy, fill = colors[i])

    def changeCoord(self, mapX, mapY):
        if self.floor == -1: #before entering tower
            self.x = mapX + 900
            self.y = mapY