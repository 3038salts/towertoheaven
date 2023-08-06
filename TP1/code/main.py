from cmu_graphics import *
import random, tower, player

def onAppStart(app):
    #----------------#
    #window size, framerate, and shape limit
    app.width = 1200
    app.height = 800
    app.stepsPerSecond = 60
    app.setMaxShapeCount(10000)
    #-----------#
    #to set the coordinates of everything except the player
    app.mapX = 0
    app.mapY = 0
    app.dx = 6
    app.dy = 50
    #doesn't include player coordinates
    app.coordsOfObjectsFloorNeg1 = []
    app.coordsOfObjectsFloor1 = []
    #-----------#
    #initialize class veriables
    #app.stepsOccurred = 0
    app.skyscraper = tower.Tower()
    app.skyscraper.loadNextFloor()
    app.skyscraper.loadStepCoords()
    app.character = player.Player()
    app.character.getSprites('../assets/player.jpg')
    app.character.spriteCount = 0
    app.character.load()
    # app.loading = False
    #-----------------------#

def redrawAll(app):
    # drawCircle(1000000, 10, 34)
    # if app.loading == False:
    app.skyscraper.drawTower()
    app.character.drawPlayer()
    # if app.loading == True:
        # app.skyscraper.drawLoadingScreen()

def onStep(app):
    if app.skyscraper.floor == -1:
        app.character.y += app.character.dy
        app.character.jump()
        # app.character.colliding()
    # app.stepsOccurred += 1

def onKeyHold(app, keys):
    # app.character.colliding()
    if app.skyscraper.floor == -1: #and app.character.colliding():
        if 'd' in keys and 'a' not in keys:
            app.character.x += app.character.dx
            if app.character.colliding():
                app.character.x -= app.character.dx
        elif 'a' in keys and 'd' not in keys:
            app.character.dx = -app.character.dx
            app.character.x += app.character.dx
            if app.character.colliding():
                app.character.x -= app.character.dx
            app.character.dx = -app.character.dx
    elif app.skyscraper.floor >= 1:
        if 'd' in keys and 'a' not in keys:
            app.mapX -= app.dx
            app.skyscraper.changeCoord()
        elif 'a' in keys and 'd' not in keys:
            app.mapX += app.dx
            app.skyscraper.changeCoord()

def onKeyPress(app, key):
    #for floor 0, we need to prevent crossing over
    if key == 'w' and app.character.jumping == False:
        app.character.dy = -9.8
        app.character.jumping = True
        if app.character.colliding():
            app.character.dy = 0
        # start = app.stepsOccurred
        # app.character.y -= 90
        # while app.stepsOccurred - start < 60:
        #     if app.stepsOccurred - start > 60:d
        #         app.character.y += 100
    if key == 's' and app.skyscraper.floor == -1:
        #this movement should be temporary and be replaced with "s" being used for entering door
        # app.character.y += 90
        pass
    elif key == 'h' and app.skyscraper.floor < 3 and app.skyscraper.atDoor(app.character.x, app.character.y): #temporary for entering door
        app.skyscraper.floor = 1
        app.skyscraper.loadNextFloor()
        # app.loading = True
        app.character.load()
        # app.loading = False
    elif key == 'y':
        app.skyscraper.floor = 1
    else:
        pass
    
def main():
    runApp()

main()