from cmu_graphics import * # cmu graphics module
from PIL import Image # pillow for image processing 
import tower, player, enemy, bullet, pit, spinningBlade # classes
import random # modules
def onAppStart(app):
    #----------------#
    # window size, framerate, and pause
    app.width = 1200
    app.height = 800
    app.stepsPerSecond = 60
    app.paused = False
    # app.loading = False
    #-----------#
    # set coordinates of map
    app.mapX = 0
    app.mapY = 0
    app.dx = 0 # map moves, not player after floor 0
    app.dxLeft = 9
    app.dxRight = -9
    # keep track of stair coordinates
    app.stairCoordsFloor0 = []
    app.stairCoordsFloor1 = []
    app.stairCoordsFloor2 = []
    app.stairCoordsFloor3 = []
    #-----------#
    # instantiate tower and player
    app.skyscraper = tower.Tower()
    app.character = player.Player()
    # player sprite counter
    app.stepsElapsed = 0
    #---------------------------#
    # instantiate enemy and bullets for calling class methods
    app.enemy = enemy.Enemy(0, 0)
    app.bullet = bullet.Bullet(0, 0, 0, 0, 0, 0)
    # lists to keep track of them
    app.enemyList = []
    app.bulletList = []
     # for spawning enemies at separate times, first time after 2 secs
    app.stepsOccurred = 0
    app.interval = 120
    # for limiting attack speed, 5 shots per second
    app.stepsPassed = 12
    app.attackSpeed = 12
    app.startCountingShots = False
    # to stop enemies from spawning continuously
    app.enemySpawnCount = 0
    #-----------------------#
    # instantiate obstacles
    app.lava = pit.Pit()
    app.blade = spinningBlade.SpinningBlade(0, 0)
    # lists to keep track of them
    app.lavaList = []
    app.bladeList = []
    app.generalStepCounter = 0 # used for animating blade right now

def redrawAll(app):
    drawOutsideTowerBG(app)
    # if app.loading == False:
    app.skyscraper.drawTower()
    app.character.drawPlayer()
    if app.skyscraper.floor >= 1:
        for enemy in app.enemyList:
            enemy.drawEnemy()
        for bullet in app.bulletList:
            bullet.drawBullet()
        for saw in app.bladeList:
            saw.drawBlade()
    # if app.loading == True:
        # app.skyscraper.drawLoadingScreen()

def drawOutsideTowerBG(app):
    # background image source: https://www.vecteezy.com/vector-art/540991-
    # cartoon-forest-seamless-background-elements-for-mobile-games
    # from Ray's cmu_graphics demos
    if app.skyscraper.floor <= 1:
        image = CMUImage(Image.open('../assets/forest.jpeg'))
    elif app.skyscraper.floor == 2:
        image = CMUImage(Image.open('../assets/skyline.jpeg'))
    bgWidth, bgHeight = getImageSize(image)
    drawImage(image, 0, 0, width = bgWidth, height = bgHeight)

def onStep(app):
    if app.paused == False:
        if app.character.jumping == False and app.character.moving == True:
            app.stepsElapsed += 1
        if app.character.moving == False:
            app.character.spriteCount = 2
        if app.character.jumping == True:
            app.stepsElapsed = 0
            app.character.spriteCount = 0
        if app.stepsElapsed >= 6: # sprite updates every 6 frames
            app.character.spriteCount = ((app.character.spriteCount + 1) 
                                         % len(app.character.spriteList))
            app.stepsElapsed = 0
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
            index = 0
            while index < len(app.enemyList):
                # print(f'HEALTH: {app.enemyList[index].health}')
                app.enemyList[index].move()
                app.enemyList[index].isHit() # automatically removes bullets that hit ghost
                # and automatically depeletes health
                index += 1
            index = 0 # reset index at the end
            while index < len(app.bulletList):
                if (app.bulletList[index].x > app.width or
                    app.bulletList[index].x < 0 or
                    app.bulletList[index].y > app.height or
                    app.bulletList[index].y < 0):
                    # removes off-screen bullets
                    app.bulletList.pop(index)
                else: # moves the bullets
                    app.bulletList[index].move()
                    index += 1
            index = 0 # reset index at the end
            app.generalStepCounter += 1
            for saw in app.bladeList:
                if app.generalStepCounter >= 6: # sprite updates every 6 frames
                    saw.spriteCount = ((saw.spriteCount + 1)
                                     % len(saw.spriteList))
                    app.generalStepCounter = 0
                saw.move()
            if app.startCountingShots == True:
                app.stepsPassed += 1
            if app.stepsPassed > 1200: # prevent memory from dying
                app.stepsPassed = 0
            app.dx = 0 # reset dx in case player isn't moving
            # app.character.isHit()
            # app.bullet.isHit()

def onKeyHold(app, keys):
    if app.paused == False:
        if app.skyscraper.floor == 0:
            if 'd' in keys and 'a' not in keys:
                app.character.moving = True
                # character moves right
                app.character.x += app.character.dx
                while app.character.colliding():
                    # makes sure player doesn't go into object or out of bounds
                    app.character.x -= 1
            elif 'a' in keys and 'd' not in keys:
                app.character.moving = True
                # character moves left
                app.character.x -= app.character.dx
                while app.character.colliding():
                    # makes sure player doesn't go into object or out of bounds
                    app.character.x += 1
        elif app.skyscraper.floor >= 1:
            if 'd' in keys and 'a' not in keys:
                app.character.moving = True
                # map moves left to make it appear as if player moves right
                app.dx = app.dxRight
                app.mapX += app.dx
                app.skyscraper.changeCoord()
                while app.character.colliding():
                    app.mapX -= app.dx
                    app.skyscraper.changeCoord()
            elif 'a' in keys and 'd' not in keys:
                app.character.moving = True
                # map moves right to make it appear as if player moves left
                app.dx = app.dxLeft
                app.mapX += app.dx
                app.skyscraper.changeCoord()
                while app.character.colliding():
                    app.mapX -= app.dx
                    app.skyscraper.changeCoord()

def onKeyRelease(app, key):
    if key == 'd' or key == 'a':
        app.character.moving = False
    
def onKeyPress(app, key):
    if app.paused == False:
        if (key == 'w' and app.character.jumping == False and
            not app.character.colliding()):
            app.character.dy = -12
            app.character.jumping = True
        elif (key == 's' and app.skyscraper.floor < 3 and # to enter door
            app.skyscraper.atDoor(app.character.x, app.character.y)):
            app.skyscraper.floor = 1
            app.character.load()
            app.skyscraper.loadFloor()
            app.blade.load()
            # app.loading = True
        elif key == 'j' and app.skyscraper.floor >= 1:
            app.startCountingShots = True
            if app.stepsPassed >= app.attackSpeed:
                app.bullet.spawnPlayerBullet()
                app.stepsPassed = 0
    if key == 'p' and app.paused == False:
        app.paused = True
    elif key == 'p' and app.paused == True:
        app.paused = False

def onMousePress(app, mouseX, mouseY): # for debugging rn, later for selection
    print(mouseX, mouseY)

def main():
    runApp()

main()