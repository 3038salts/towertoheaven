from cmu_graphics import *
import random, tower, player

def onAppStart(app):
    app.width = 1280
    app.height = 800
    app.stepsPerSecond = 60
    app.mapX = 0
    app.mapY = 0
    app.character = player.Player()
    app.character.getSprites('../assets/player.jpg')
    app.skyscraper = tower.Tower(900, 300)

def redrawAll(app):
    app.skyscraper.drawTower()
    app.character.drawPlayer()

def onStep(app):
    app.character.spriteCount = 0 # (1 + app.character.spriteCount) % len(app.character.spriteList)
    app.skyscraper.changeCoord(app.mapX, app.mapY)

def onKeyHold(app, keys):
    if 'right' in keys and 'left' not in keys:
        app.mapX -= 5
    elif 'left' in keys and 'right' not in keys:
        app.mapX += 5
        

def main():
    runApp()

main()