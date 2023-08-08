from cmu_graphics import * #cmu graphics module
import tower, player, enemy, bullet # classes
import random # modules
def onAppStart(app):
    #----------------#
    # window size and framerate
    app.width = 1200
    app.height = 800
    app.stepsPerSecond = 60
    # app.loading = False
    #-----------#
    # set coordinates of everything except the player
    app.mapX = 0
    app.mapY = 0
    app.dx = 9 # map moves, not player after floor 0
    # lists don't include player, tower, and enemy coordinates
    app.coordsOfObjectsFloor0 = []
    app.coordsOfObjectsFloor1 = []
    app.coordsOfObjectsFloor2 = []
    app.coordsOfObjectsFloor3 = []
    #-----------#
    # instantiate tower and player
    app.skyscraper = tower.Tower()
    app.character = player.Player()
    #---------------------------#
    # instantiate enemy and bullets for calling class methods
    app.enemy = enemy.Enemy(0, 0)
    app.bullet= bullet.Bullet(0, 0, 0, 0)
    # lists to keep track of them
    app.enemyList = []
    app.bulletList = []
     # for spawning enemies at separate times, first time after 2 secs
    app.stepsOccurred = 0
    app.interval = 120
    # to stop enemies from spawning continuously
    app.enemySpawnCount = 0
    #-----------------------#

def redrawAll(app):
    # if app.loading == False:
    app.skyscraper.drawTower()
    app.character.drawPlayer()
    if app.skyscraper.floor >= 1:
        for enemy in app.enemyList:
            enemy.drawEnemy()
    # if app.loading == True:
        # app.skyscraper.drawLoadingScreen()

def onStep(app):
    app.character.y += app.character.dy # modifies player y position
    app.character.jump() # enforces gravity
    app.skyscraper.changeCoord() # updates coordinates of tower and objects
    if app.skyscraper.floor == 1:
        app.stepsOccurred += 1
        if (len(app.enemyList) < 3 and app.stepsOccurred > app.interval
            and app.enemySpawnCount <= 5): # spawns a ghost every so often
            app.stepsOccurred = 0 # resets time
            app.interval = random.randint(420, 600)
            app.enemy.spawn()
            app.enemySpawnCount += 1
        for enemy in app.enemyList:
            enemy.move()
    # app.stepsOccurred += 1
    # app.character.isHit()
    # app.enemy.isHit()
    # app.bullet.isHit()

def onKeyHold(app, keys):
    if app.skyscraper.floor == 0:
        if 'd' in keys and 'a' not in keys:
            # character moves right
            app.character.x += app.character.dx
            while app.character.colliding():
                # makes sure player doesn't go into object or out of bounds
                app.character.x -= 1
        elif 'a' in keys and 'd' not in keys:
            # character moves left
            app.character.x -= app.character.dx
            while app.character.colliding():
                # makes sure player doesn't go into object or out of bounds
                app.character.x += 1
    elif app.skyscraper.floor >= 1:
        if 'd' in keys and 'a' not in keys:
            # map moves left to make it appear as if player moves right
            app.mapX -= app.dx
            app.skyscraper.changeCoord()
            while app.character.colliding():
                app.mapX += app.dx
                app.skyscraper.changeCoord()
        elif 'a' in keys and 'd' not in keys:
            # map moves right to make it appear as if player moves left
            app.mapX += app.dx
            app.skyscraper.changeCoord()
            while app.character.colliding():
                app.mapX -= app.dx
                app.skyscraper.changeCoord()
    
def onKeyPress(app, key):
    if (key == 'w' and app.character.jumping == False and
        not app.character.colliding()):
        app.character.dy = -12
        app.character.jumping = True
        # if app.character.colliding():
            # app.character.dy = 0
    if (key == 's' and app.skyscraper.floor < 3 and
        app.skyscraper.atDoor(app.character.x, app.character.y)): #enter door
        app.skyscraper.floor = 1
        app.character.load()
        app.skyscraper.loadFloor()
        # app.loading = True
    elif key == 'j' and app.skyscraper.floor != 0:
           app.bullet.spawnPlayerBullet()
    else:
        pass
    
def main():
    runApp()

main()