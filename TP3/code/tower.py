from cmu_graphics import *
import random, copy
class Tower:
    def __init__(self):
        self.floor = -1
        # self.totalFloors = 3
        self.x = 900
        self.y = 0
        self.modifiedX = self.x
        self.modifiedY = self.y
        self.towerWidth = 0
        self.towerHeight = 0
        self.modifiedDoorX = self.doorX = 0
        self.modifiedDoorY = self.doorY = 0
        self.doorWidth = 0
        self.doorHeight = 0
        self.colors = [rgb(186, 205, 252), rgb(252, 200, 186), # blue, red
                       rgb(238, 252, 186), rgb(205, 252, 186), # yellow, green
                       rgb(234, 176, 129)] # orange
        self.groundY = app.height
        self.loadFloor()
    
    def drawTower(self):
        if self.floor == 0: # before entering tower
            drawRect(self.x, self.y, self.towerWidth, self.towerHeight,
                     fill = 'gray', opacity = 75) # tower
            self.drawStartStairs() # stairs
            self.drawDoor() # door
        elif 1 <= self.floor <= 3:
            drawRect(self.modifiedX, self.modifiedY, self.towerWidth,
                     self.towerHeight, fill = 'gray', opacity = 70) # tower
            self.drawFloorSign()
            self.drawSteps() # steps
            self.drawDoor() # door
        elif self.floor == 4:
            drawLabel('You beat the game!', app.width // 2, app.height // 2, size = 40)

    def drawDoor(self):
        drawRect(self.modifiedDoorX, self.modifiedDoorY, self.doorWidth, self.doorHeight,
                     fill = 'brown')

    def drawSteps(self):
        for i in range(len(self.stepCoords)):
            drawRect(app.stairCoordsFloor1[i][0],
                     app.stairCoordsFloor1[i][1], self.stepWidth,
                     self.stepHeight, fill = self.colors[i])

    def loadStepCoords(self):
        if self.floor == 1:
            xRange = [2000, 2500]
        elif self.floor == 2:
            xRange = [4200, 4900]
        elif self.floor == 3:
            xRange = [9000, 9600]
        self.originalStepCoords = []
        self.stepHeight = 60
        self.stepWidth = 150
        y = 600
        dy = random.randint(180, 200)
        xChange = 120
        for step in range(3):
            x = random.randrange(xRange[0] + xChange, xRange[1], 100)
            for index in self.originalStepCoords:
                while x == index[0]:
                    x = random.randrange(xRange[0] + xChange, xRange[1], 100)
            xChange += 100
            self.originalStepCoords.append([x, y, self.stepWidth,
                                            self.stepHeight])
            y -= dy
        self.stepCoords = copy.deepcopy(self.originalStepCoords)
        app.stairCoordsFloor1 = copy.deepcopy(self.stepCoords)

    def drawStartStairs(self):
        self.stairCoords = []
        # colors = self.loadStairColors()
        y = 720
        self.stairHeight = 80
        self.stairWidth = 150
        startX = app.width - (self.stairWidth * 5) - 75
        for x in range(startX, app.width - self.stairWidth, self.stairWidth):
            self.stairCoords.append((x, y))
            app.stairCoordsFloor0.append([x, y, self.stairWidth,
                                                 self.stairHeight])
            y -= self.stairHeight
        for i in range(len(self.stairCoords)):
            drawRect(self.stairCoords[i][0], self.stairCoords[i][1],
                     self.stairWidth, self.stairHeight, fill = self.colors[i])

    def drawFloorSign(self):
        drawRect(400 + app.mapX, 300 + app.mapY, 200, 150, fill = rgb(186, 205, 252))
        drawLabel('Move right to proceed', 500 + app.mapX, 375 + app.mapY, size = 20)

    def changeCoord(self):
        if 1 <= self.floor <= 3: #within tower
            self.modifiedX = self.x + app.mapX
            self.modifiedY = self.y + app.mapY
            self.modifiedDoorX = self.doorX + app.mapX
            self.modifiedDoorY = self.doorY + app.mapY
            for i in range(len(self.originalStepCoords)):
                app.stairCoordsFloor1[i][0] = self.originalStepCoords[i][0] + app.mapX
                app.stairCoordsFloor1[i][1] = self.originalStepCoords[i][1] + app.mapY

    #checks if center of player is within door
    def atDoor(self, playerX, playerY):
        if (self.modifiedDoorX <= playerX <= self.modifiedDoorX + self.doorWidth
            and self.modifiedDoorY <= playerY <= self.modifiedDoorY + self.doorHeight):
            return True
        return False

    def loadFloor(self):
        if self.floor == 0: #before entering tower
            #tower is in a fixed position
            self.towerWidth = app.width - 900
            self.towerHeight = app.height - 400
            #door
            self.modifiedDoorX = self.doorX = self.x + (self.towerWidth // 4)
            self.modifiedDoorY = self.doorY = self.y + self.towerHeight // 2 + 25
            self.doorWidth = self.towerWidth // 2
            self.doorHeight = self.towerHeight // 2 - 25
        elif self.floor == 1:
            self.x = self.modifiedX = 300
            self.y = self.modified = 0
            self.towerWidth = app.width * 2
            self.towerHeight = app.height * 2
            app.skyscraper.loadStepCoords()
            self.modifiedDoorX = self.doorX = self.originalStepCoords[-1][0]
            self.modifiedDoorY = self.doorY = self.originalStepCoords[-1][1] - 175
        elif self.floor == 2:
            self.x = self.modifiedX = 300
            self.y = self.modified = 0
            self.towerWidth = app.width * 4
            self.towerHeight = app.height * 4
            app.skyscraper.loadStepCoords()
            self.modifiedDoorX = self.doorX = self.originalStepCoords[-1][0]
            self.modifiedDoorY = self.doorY = self.originalStepCoords[-1][1] - 175
        elif self.floor == 3:
            self.x = self.modifiedX = 300
            self.y = self.modified = 0
            self.towerWidth = app.width * 8
            self.towerHeight = app.height * 8
            app.skyscraper.loadStepCoords()
            self.modifiedDoorX = self.doorX = self.originalStepCoords[-1][0]
            self.modifiedDoorY = self.doorY = self.originalStepCoords[-1][1] - 175
        elif self.floor == 4: #in heaven
            pass
    
    # def drawLoadingScreen(self):
    #     drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 100)