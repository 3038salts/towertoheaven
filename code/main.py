from cmu_graphics import *
import random, tower, player

def onAppStart(app):
    #----------------#
    #window size and framerate
    app.width = 1200
    app.height = 800
    app.stepsPerSecond = 60
    #-----------#
    #to set the coordinates of everything except the player
    app.mapX = 0
    app.mapY = 0
    #-----------#
    #initialize class veriables
    app.character = player.Player()
    app.character.getSprites('../assets/player.jpg')
    # app.stepsOccurloadred = 0
    app.skyscraper = tower.Tower()
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
    # app.stepsOccurred += 1
    app.character.spriteCount = 0 # (1 + app.character.spriteCount) % len(app.character.spriteList)
    app.skyscraper.changeCoord(app.mapX, app.mapY)
    # app.character.y.changeCoord(app.skyscraper.floor,)

def onKeyHold(app, keys):
    if app.skyscraper.floor == -1:
        if 'd' in keys and 'a' not in keys:
            app.character.x += 6
        elif 'a' in keys and 'd' not in keys:
            app.character.x -= 6
    else:
        if 'd' in keys and 'a' not in keys:
            app.mapX -= 5
        elif 'a' in keys and 'd' not in keys:
            app.mapX += 5

def onKeyPress(app, key):
    #for floor 0, we need to prevent crossing over
    if key == 'w' and app.skyscraper.floor == -1 and app.character.jumping == False:
        # app.character.jump()
        # start = app.stepsOccurred
        app.character.y -= 90
        # while app.stepsOccurred - start < 60:
        #     if app.stepsOccurred - start > 60:
        #         app.character.y += 100
    elif key == 's' and app.skyscraper.floor == -1 and app.character.jumping == False:
        #this movement should be temporary and be replaced with "s" being used for entering door
        app.character.y += 90
    elif key == 'h' and app.skyscraper.floor < 3 and app.skyscraper.atDoor(app.character.x, app.character.y): #temporary for entering door
        app.skyscraper.floor += 1
        # app.loading = True
        # app.skyscraper.loadNextFloor()
        # app.character.load()
        # app.loading = False
    else:
        pass
    
def main():
    runApp()

main()