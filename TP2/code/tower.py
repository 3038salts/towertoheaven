from cmu_graphics import *
import random, copy
class Tower:
    def __init__(self):
        self.floor = 0
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
        self.colors = [rgb(186, 205, 252), rgb(252, 200, 186), # blue, red
                       rgb(238, 252, 186), rgb(205, 252, 186), # yellow, green
                       rgb(252, 186, 205)]
        self.groundY = app.height
        self.loadFloor()
    
    def drawTower(self):
        if self.floor == 0: #before entering tower
            #tower
            drawRect(self.x, self.y, self.towerWidth, self.towerHeight,
                     fill = 'gray', opacity = 80)
            #door
            drawRect(self.doorX, self.doorY, self.doorWidth, self.doorHeight,
                     fill = 'brown')
            #stairs
            self.drawStartStairs()
        elif self.floor == 1: #in tower
            # tower in the back
            drawRect(self.modifiedX, self.modifiedY, self.towerWidth,
                     self.towerHeight, fill = 'gray', opacity = 75)
            self.draw1stFloorSign()
            # steps to ascend floor (not implemented yet)
            self.drawSteps()
            # self.drawGround()
    
    # def drawGround(self):
    #     width = 800
    #     height = 245
    #     for i in range(len(self.stepCoords), len(self.stepCoords) + 1):
    #         drawRect(app.coordsOfObjectsFloor1[i][0], app.coordsOfObjectsFloor
    # 1[i][1], width, height, fill = rgb(193, 170, 207))

    # def loadGround(self):
    #     x, y, width, height = 200, 555, 800, 245
    #     self.originalGroundCoords = [x, y, width, height]
    #     app.coordsOfObjectsFloor1.append(copy.copy(self.originalGroundCoords))

    def drawSteps(self):
        for i in range(len(self.stepCoords)):
            drawRect(app.coordsOfObjectsFloor1[i][0],
                     app.coordsOfObjectsFloor1[i][1], self.stepWidth,
                     self.stepHeight, fill = self.colors[i])

    def loadStepCoords(self):
        self.originalStepCoords = []
        self.stepHeight = 60
        self.stepWidth = 150
        y = 600
        dy = 200
        xRange = [4000, 4900]
        xChange = 100
        for step in range(5):
            x = random.randrange(xRange[0] + xChange, xRange[1], 100)
            xChange += 100
            self.originalStepCoords.append([x, y, self.stepWidth,
                                            self.stepHeight])
            y -= dy
        self.stepCoords = copy.deepcopy(self.originalStepCoords)
        app.coordsOfObjectsFloor1 = copy.deepcopy(self.stepCoords)

    def drawStartStairs(self):
        self.stairCoords = []
        # colors = self.loadStairColors()
        y = 720
        self.stairHeight = 80
        self.stairWidth = 150
        startX = app.width - (self.stairWidth * 5) - 75
        for x in range(startX, app.width - self.stairWidth, self.stairWidth):
            self.stairCoords.append((x, y))
            app.coordsOfObjectsFloor0.append([x, y, self.stairWidth,
                                                 self.stairHeight])
            y -= self.stairHeight
        for i in range(len(self.stairCoords)):
            drawRect(self.stairCoords[i][0], self.stairCoords[i][1],
                     self.stairWidth, self.stairHeight, fill = self.colors[i])

    def draw1stFloorSign(self):
        drawRect(200, 300, 200, 150, fill = rgb(29, 242, 99))
        drawLabel('Move right to proceed', 300, 375)

    # def loadStairColors(self):
    #     colors = []
    #     while len(colors) != len(self.colors):
    #         newColor = (self.colors[random.randint(0, 4)])
    #         if newColor not in colors:
    #             colors.append(newColor)
    #     return colors

    def changeCoord(self):
        if self.floor >= 1: #within tower
            self.modifiedX = self.x + app.mapX
            self.modifiedY = self.y + app.mapY
            for i in range(len(self.originalStepCoords)):
                app.coordsOfObjectsFloor1[i][0] = self.originalStepCoords[i][0] + app.mapX
                app.coordsOfObjectsFloor1[i][1] = self.originalStepCoords[i][1] + app.mapY
            # for i in range(len(self.originalStepCoords), len(self.originalStepCoords) + 1):
            #     app.coordsOfObjectsFloor1[i][0] = self.originalGroundCoords[i - len(self.originalStepCoords)] + app.mapX
            #     app.coordsOfObjectsFloor1[i][1] = self.originalGroundCoords[i - len(self.originalStepCoords) + 1] + app.mapY
            # for i in range(len(self.stepCoords)):
            #     self.stepCoords[i][0] = self.originalStepCoords[i][0] + app.mapX
            #     self.stepCoords[i][1] = self.originalStepCoords[i][1] + app.mapY
            # app.coordsOfObjectsFloor1 = []
            # app.coordsOfObjectsFloor1.extend(self.stepCoords)
    
    #checks if center of player is within door
    def atDoor(self, playerx, playery):
        if (self.floor == 0 and self.doorX <= playerx <= self.doorX + self.doorWidth
            and self.doorY <= playery <= self.doorY + self.doorHeight):
            return True
        #add more cases for other floors
        return False

    def loadFloor(self):
        if self.floor == 0: #before entering tower
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
            self.y = self.modified = -app.height
            self.towerWidth = app.width * 2
            self.towerHeight = app.height * 2
            app.skyscraper.loadStepCoords()
            # app.skyscraper.loadGround()
        elif self.floor == 2:
            pass
        elif self.floor == 3:
            pass
        elif self.floor == 4: #in heaven
            pass
    
    # def drawLoadingScreen(self):
    #     drawRect(0, 0, app.width, app.height, fill = 'black', opacity = 100)