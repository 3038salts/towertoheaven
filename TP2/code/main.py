from cmu_graphics import * #cmu graphics moduel
import tower, player, enemy, bullet # classes
import time # modules
def onAppStart(app):
    #----------------#
    # window size and framerate
    app.width = 1200
    app.height = 800
    app.stepsPerSecond = 60
    # app.stepsOccurred = 0
    # app.loading = False
    #-----------#
    # set coordinates of everything except the player
    app.mapX = 0
    app.mapY = 0
    app.dx = 9 # map moves, not player
    # these lists don't include player, tower, and enemy coordinates
    app.coordsOfObjectsFloorNeg1 = []
    app.coordsOfObjectsFloor1 = []
    app.coordsOfObjectsFloor2 = []
    app.coordsOfObjectsFloor3 = []
    #-----------#
    # instantiate tower and player
    app.skyscraper = tower.Tower()
    app.skyscraper.loadFloor()
    app.character = player.Player()
    app.character.getSprites()
    app.character.load()
    #---------------------------#
    #enemy and bullets
    app.enemy = enemy.Enemy(0, 0) # used only to call the class methods
    app.enemy.getSprites()
    app.bullet= bullet.Bullet(0, 0, 0, 0) # used only to call the class methods
    app.enemyList = []
    app.bulletList = []
    #-----------------------#

def redrawAll(app):
    # if app.loading == False:
    app.skyscraper.drawTower()
    app.character.drawPlayer()
    if app.skyscraper.floor != -1:
        for enemy in app.enemyList:
            enemy.drawEnemy()
    # if app.loading == True:
        # app.skyscraper.drawLoadingScreen()

def onStep(app):
    # if app.skyscraper.floor == -1:
    app.character.y += app.character.dy #makes player jump up and down
    app.character.jump() #enforces gravity
    app.skyscraper.changeCoord() #updates coordinates of tower and all objects
    if app.skyscraper.floor == 1:
        if len(app.enemyList) <= 3:
            #do timing interval then spawn a ghost
            enemy.getSprites()
            enemy.spawn()
        if len(app.enemyList) != 0:
            for enemy in app.enemyList:
                enemy.move()
        # app.character.colliding()
    # app.stepsOccurred += 1
    # app.character.isHit()
    # app.enemy.isHit()
    # app.bullet.isHit()

def onKeyHold(app, keys):
    # app.character.colliding()
    if app.skyscraper.floor == -1: #and app.character.colliding():
        if 'd' in keys and 'a' not in keys:
            app.character.x += app.character.dx
            while app.character.colliding():
                app.character.x -= 1
        elif 'a' in keys and 'd' not in keys:
            app.character.dx = -app.character.dx
            app.character.x += app.character.dx
            while app.character.colliding():
                app.character.x += 1
            app.character.dx = -app.character.dx
    elif app.skyscraper.floor >= 1:
        if 'd' in keys and 'a' not in keys:
            app.mapX -= app.dx
            app.skyscraper.changeCoord()
            while app.character.colliding():
                app.mapX += 1
                app.skyscraper.changeCoord()
        elif 'a' in keys and 'd' not in keys:
            app.mapX += app.dx
            app.skyscraper.changeCoord()
            while app.character.colliding():
                app.mapX -= 1
                app.skyscraper.changeCoord()

def onKeyPress(app, key):
    #for floor 0, we need to prevent crossing over
    if (key == 'w' and app.character.jumping == False and
        not app.character.colliding()):
        app.character.dy = -12
        app.character.jumping = True
        # if app.character.colliding():
            # app.character.dy = 0
            # pass
        # start = app.stepsOccurred
        # app.character.y -= 90
        # while app.stepsOccurred - start < 60:
        #     if app.stepsOccurred - start > 60:
        #         app.character.y += 100
    if (key == 's' and app.skyscraper.floor < 3 and
        app.skyscraper.atDoor(app.character.x, app.character.y)): #enter door
        app.skyscraper.floor = 1
        app.character.load()
        app.skyscraper.loadFloor()
        # app.enemy.load()
        # app.loading = True
        # app.loading = False
    elif key == 'j' and app.skyscraper.floor != -1:
           app.bullet.spawnPlayerBullet()
    else:
        pass
    
def main():
    runApp()

main()