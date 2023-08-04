from cmu_graphics import *
import time
class Tower:
    def __init__(self):
        self.floor = -1
        self.totalFloors = 3
        self.x = 900
        self.y = 0
        self.towerWidth = 0
        self.towerHeight = 0
        self.doorX = 0
        self.doorY = 0
        self.doorWidth = 0
        self.doorHeight = 0
    
    def drawTower(self):
        if self.floor == -1: #before entering tower
            #tower is in a fixed position
            self.towerWidth = app.width - 900
            self.towerHeight = app.height - 400
            #tower
            drawRect(self.x, self.y, self.towerWidth, self.towerHeight, fill = 'gray')
            #door
            self.doorX = self.x + (self.towerWidth // 4)
            self.doorY = self.y + self.towerHeight // 2
            self.doorWidth = self.towerWidth // 2
            self.doorHeight = self.towerHeight // 2
            drawRect(self.doorX, self.doorY, self.doorWidth, self.doorHeight, fill = 'brown')
            self.drawStartStairs()
        # else:
            # drawRect(self.x, self.y, app.width - 900, app.height - 200, fill = 'gray')
            # drawRect(self.x + 100, self.y + 300, app.width - 1100, app.height - 600, fill = 'red')
    
    def drawStartStairs(self):
        stairCoords = []
        colors = [rgb(186, 205, 252), rgb(252, 200, 186), rgb(238, 252, 186), rgb(205, 252, 186), rgb(252, 186, 205)]
        y = 720
        dy = 80
        dx = 150
        startX = app.width - (dx * 5) - 75
        for x in range(startX, app.width - dx, dx):
            stairCoords.append((x, y))
            y -= dy
        for i in range(len(stairCoords)):
            drawRect(stairCoords[i][0], stairCoords[i][1], dx, dy, fill = colors[i])

    def changeCoord(self, mapX, mapY):
        if self.floor == -1: #before entering tower
            self.x = mapX + 900
            self.y = mapY
    
    #checks if player is touching door to move up a floor
    def atDoor(self, playerX, playerY):
        if self.floor == -1 and distance(playerX, playerY, self.doorX, self.doorY) <= self.doorWidth:
            return True
        #add more cases for other floors
        return False

    def loadNextFloor(self):
        if self.floor == 1:
            pass
        elif self.floor == 2:
            pass
        elif self.floor == 3:
            pass
        elif self.floor == 4: #finished game
            pass

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    
    # def drawLoadingScreen(self):
    #     drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 100)
