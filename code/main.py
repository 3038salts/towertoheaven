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
    app.stepsOccurred = 0
    app.skyscraper = tower.Tower()
    #-----------------------#

def redrawAll(app):
    app.skyscraper.drawTower()
    app.character.drawPlayer()

def onStep(app):
    app.stepsOccurred += 1
    app.character.spriteCount = 0 # (1 + app.character.spriteCount) % len(app.character.spriteList)
    app.skyscraper.changeCoord(app.mapX, app.mapY)
    # app.character.y.changeCoord(app.skyscraper.floor,)

def onKeyHold(app, keys):
    if app.skyscraper.floor == -1:
        if 'd' in keys and 'a' not in keys:
            app.character.x += 5
        elif 'a' in keys and 'd' not in keys:
            app.character.x -= 5
    else:
        if 'd' in keys and 'a' not in keys:
            app.mapX -= 5
        elif 'a' in keys and 'd' not in keys:
            app.mapX += 5

def onKeyPress(app, key):
    if key == 'w' and app.skyscraper.floor == -1 and app.character.jumping == False:
        # app.character.jump()
        # start = app.stepsOccurred
        app.character.y -= 100
        # while app.stepsOccurred - start < 60:
        #     if app.stepsOccurred - start > 60:
        #         app.character.y += 100

    else:
        pass
    
def main():
    runApp()

main()