from cmu_graphics import *
import obstacles, random, copy
class Tower:
    def __init__(self):
        self.floor = -1
        self.totalFloors = 3
        self.x = 900
        self.y = 0
        self.modifiedX = self.x
        self.modifiedY = self.y
        self.towerWidth = 0
        self.towerHeight = 0
        self.doorX = 0
        self.doorY = 0
        self.doorWidth = 0
        self.doorHeight = 0
        self.colors = [rgb(186, 205, 252), rgb(252, 200, 186), rgb(238, 252, 186),
                       rgb(205, 252, 186), rgb(252, 186, 205)]
        self.groundY = app.height
    
    def drawTower(self):
        if self.floor == -1: #before entering tower
            #tower
            drawRect(self.x, self.y, self.towerWidth, self.towerHeight, fill = 'gray')
            #door
            drawRect(self.doorX, self.doorY, self.doorWidth, self.doorHeight, fill = 'brown')
            #stairs
            self.drawStartStairs()
        elif self.floor == 1: #in tower
            #tower in the back
            drawRect(self.modifiedX, self.modifiedY, self.towerWidth, self.towerHeight, fill = 'gray')
            #wall pattern
            # self.drawBrickPattern()
            #jumping up steps
            self.drawSteps()
            # drawRect(self.x + 100, self.y + 300, app.width - 1100, app.height - 600, fill = 'red')
    
    # def drawBrickPattern(self): #this makes it lag too much
    #     brickHeight = self.towerHeight // 60
    #     brickWidth = self.towerWidth // 50
    #     for row in range(self.modifiedX, self.modifiedX + self.towerWidth, brickWidth + 2):
    #         for col in range(self.modifiedY, self.modifiedY + self.towerHeight, brickHeight + 2):
    #             drawRect(row, col, brickWidth, brickHeight, fill = rgb(244, 248, 184), border = 'black', borderWidth = 1)

    def drawSteps(self):
        self.stepHeight = 60
        self.stepWidth = 150
        # colors = []
        # while len(colors) != len(self.colors):
        #     newColor = (self.colors[random.randint(0, 4)])
        #     if newColor not in colors:
        #         colors.append(newColor)
        for i in range(len(self.stepCoords)):
            drawRect(self.stepCoords[i][0], self.stepCoords[i][1], self.stepWidth, self.stepHeight, fill = self.colors[i])

    def loadStepCoords(self):
        self.originalStepCoords = []
        y = 250
        dy = 200
        xrange = (200, 800)
        for step in range(5):
            x = random.randrange(xrange[0], xrange[1], 100)
            self.originalStepCoords.append([x, y])
            y -= dy
        self.stepCoords = copy.deepcopy(self.originalStepCoords)

    def drawStartStairs(self):
        self.stairCoords = []
        # colors = self.loadStairColors()
        y = 720
        self.stairHeight = 80
        self.stairWidth = 150
        startX = app.width - (self.stairWidth * 5) - 75
        for x in range(startX, app.width - self.stairWidth, self.stairWidth):
            self.stairCoords.append((x, y))
            y -= self.stairHeight
        for i in range(len(self.stairCoords)):
            drawRect(self.stairCoords[i][0], self.stairCoords[i][1], self.stairWidth, self.stairHeight, fill = self.colors[i])

    # def loadStairColors(self):
    #     colors = []
    #     while len(colors) != len(self.colors):
    #         newColor = (self.colors[random.randint(0, 4)])
    #         if newColor not in colors:
    #             colors.append(newColor)
    #     return colors

    def changeCoord(self):
        if self.floor != -1: #within tower
            self.modifiedX = self.x + app.mapX
            self.modifiedY = self.y + app.mapY
            for i in range(len(self.stepCoords)):
                self.stepCoords[i][0] = self.originalStepCoords[i][0] + app.mapX
                self.stepCoords[i][1] = self.originalStepCoords[i][1] + app.mapY
    
    #checks if center of player is within door
    def atDoor(self, playerx, playery):
        if (self.floor == -1 and self.doorX <= playerx <= self.doorX + self.doorWidth
            and self.doorY <= playery <= self.doorY + self.doorHeight):
            return True
        #add more cases for other floors
        return False

    def loadNextFloor(self):
        if self.floor == -1: #before entering tower
            #tower is in a fixed position
            self.towerWidth = app.width - 900
            self.towerHeight = app.height - 400
            #door
            self.doorX = self.x + (self.towerWidth // 4)
            self.doorY = self.y + self.towerHeight // 2
            self.doorWidth = self.towerWidth // 2
            self.doorHeight = self.towerHeight // 2
        elif self.floor == 1:
            self.x = self.modifiedX = 100
            self.y = self.modified = -2 * app.height
            self.towerWidth = app.width * 4
            self.towerHeight = app.height * 4
        elif self.floor == 2:
            pass
        elif self.floor == 3:
            pass
        elif self.floor == 4: #in heaven
            pass

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)
    
    # def drawLoadingScreen(self):
    #     drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 100)