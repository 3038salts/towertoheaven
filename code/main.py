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
    app.mapx = 0
    app.mapy = 0
    app.dx = 6
    app.dy = 6
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
    pass
    # app.stepsOccurred += 1
    # app.skyscraper.changeCoord(app.mapx, app.mapy)
    # app.character.changeCoord(app.skyscraper.floor)
    # app.character.y.changeCoord(app.skyscraper.floor,)

def onKeyHold(app, keys):
    if app.skyscraper.floor == -1: #and app.character.notColliding():
        if 'd' in keys and 'a' not in keys:
            app.character.x += 8
        elif 'a' in keys and 'd' not in keys:
            app.character.x -= 8
    elif app.skyscraper.floor >= 1:
        if 'd' in keys and 'a' not in keys:
            app.mapx -= app.dx
            app.character.notColliding()
            app.skyscraper.changeCoord()
        elif 'a' in keys and 'd' not in keys:
            app.mapx += app.dx
            app.character.notColliding()
            app.skyscraper.changeCoord()
    # elif app.skyscraper.floor >= 1 and app.character.notColliding() == False:
    #     if 'd' in keys and 'a' not in keys:
    #         app.mapx += app.dx * 10
    #         app.skyscraper.changeCoord()
    #     elif 'a' in keys and 'd' not in keys:
    #         app.mapx -= app.dx * 10
    #         app.skyscraper.changeCoord()

def onKeyPress(app, key):
    #for floor 0, we need to prevent crossing over
    if key == 'w' and app.skyscraper.floor == -1 and app.character.jumping == False:
        # app.character.jump()
        # start = app.stepsOccurred
        app.character.y -= 90
        # while app.stepsOccurred - start < 60:
        #     if app.stepsOccurred - start > 60:d
        #         app.character.y += 100
    elif key == 's' and app.skyscraper.floor == -1 and app.character.jumping == False:
        #this movement should be temporary and be replaced with "s" being used for entering door
        app.character.y += 90
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