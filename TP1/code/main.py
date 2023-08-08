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
    # app.listOfCoords = []
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
    # app.stepsOccurred += 1

def onKeyHold(app, keys):
    app.character.notColliding()
    if app.skyscraper.floor == -1: #and app.character.notColliding():
        if 'd' in keys and 'a' not in keys:
            app.character.x += 8
            app.character.notColliding()
        elif 'a' in keys and 'd' not in keys:
            app.character.x -= 8
            app.character.notColliding()
    elif app.skyscraper.floor >= 1:
        if 'd' in keys and 'a' not in keys:
            app.mapX -= app.dx
            app.skyscraper.changeCoord()
        elif 'a' in keys and 'd' not in keys:
            app.mapX += app.dx
            app.skyscraper.changeCoord()

def onKeyPress(app, key):
    #for floor 0, we need to prevent crossing over
    if key == 'w' and app.skyscraper.floor == -1 and app.character.jumping == False:
        app.character.dy = -9.8
        # app.character.jump()
        app.character.jumping = True
        # start = app.stepsOccurred
        # app.character.y -= 90
        # while app.stepsOccurred - start < 60:
        #     if app.stepsOccurred - start > 60:d
        #         app.character.y += 100
    elif key == 's' and app.skyscraper.floor == -1:
        #this movement should be temporary and be replaced with "s" being used for entering door
        # app.character.y += 90
        pass
    elif key == 'h' and app.skyscraper.floor < 3 and app.skyscraper.atDoor(app.character.x, app.character.y): #temporary for entering door
        app.skyscraper.floor = 1
        app.skyscraper.loadNextFloor()
        # app.loading = True
        app.character.load()
        # app.loading = False
    else:
        pass
    
def main():
    runApp()

main()