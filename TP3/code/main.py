from cmu_graphics import * # cmu graphics module
from PIL import Image # pillow for image processing 
import tower, player, enemy, bullet, spinningBlade, button # classes
import random # modules
def onAppStart(app):
    #----------------#
    # window size, framerate, pause, game over, and general step counter
    app.width = 1200
    app.height = 800
    app.stepsPerSecond = 60
    app.paused = False
    app.gameOver = False
    app.generalStepCounter = 0 # used for animating saw blade
    app.fadeIncrement= 0 # works in tandem with the var above
    #-----------#
    # set coordinates of map
    app.mapX = 0
    app.mapY = 0
    app.dx = 0 # map moves, not player after floor 0
    app.dxLeft = 12
    app.dxRight = -12
    # keep track of stair coordinates
    app.stairCoordsFloor0 = []
    app.stairCoordsFloor1 = []
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
    app.stepsOccurred = 120
    app.interval = 120
    # for limiting attack speed, 5 shots per second
    app.stepsPassed = 12
    app.attackSpeed = 12
    app.startCountingShots = False
    # to stop enemies from spawning continuously
    app.enemySpawnCount = 0
    #-----------------------#
    # instantiate obstacles
    app.blade = spinningBlade.SpinningBlade(0, 0)
    # lists to keep track of them
    app.bladeList = []
    #----------#
    # button for start
    app.button = button.Button(500, 375, 200, 100, 'Start')

def redrawAll(app):
    drawOutsideTowerBG(app)
    if app.skyscraper.floor == -1:
        drawStart(app)
    app.skyscraper.drawTower()
    if 1 <= app.skyscraper.floor <= 3:
        for enemy in app.enemyList:
            enemy.drawEnemy()
        for bullet in app.bulletList:
            bullet.drawBullet()
        for saw in app.bladeList:
            saw.drawBlade()
    if app.skyscraper.floor >= 0:
        app.character.drawPlayer()
    if app.gameOver == True:
        drawGameOver(app)

def drawStart(app):
    drawLabel("Tower To Heaven", app.width // 2, app.height // 2 - 200,
              size = 100, fill = rgb(186, 205, 252))
    app.button.drawButton()
    drawLabel("Use WAD to move, S to enter the door, and J to shoot bullets.",
              app.width // 2, app.height // 2 + 150, size = 20, fill = 'white')

def drawOutsideTowerBG(app):
    # background image sources: https://www.vecteezy.com/vector-art/540991-
    # cartoon-forest-seamless-background-elements-for-mobile-games
    # https://wallup.net/drawing-cityscape-artwork-sky/
    # http://getdrawings.com/get-drawing#simple-mountain-drawing-60.jpg
    # from Ray's cmu_graphics demos
    if app.skyscraper.floor <= 1:
        image = CMUImage(Image.open('../assets/forest.jpeg'))
    elif app.skyscraper.floor == 2:
        image = CMUImage(Image.open('../assets/skyline.jpeg'))
    elif app.skyscraper.floor == 3:
        image = CMUImage(Image.open('../assets/mountain.jpeg'))
    elif app.skyscraper.floor == 4:
        image = CMUImage(Image.open('../assets/clouds.jpeg'))
    bgWidth, bgHeight = getImageSize(image)
    drawImage(image, 0, 0, width = bgWidth, height = bgHeight)

def drawGameOver(app):
    drawRect(0, 0, app.width, app.height, fill = 'black',
             opacity = app.fadeIncrement)
    drawLabel("You died.", app.width / 2, 325, size = 50, bold = True,
              fill = 'crimson', font = 'monospace')

def onStep(app):
    app.generalStepCounter += 1
    if app.paused == False and app.gameOver == False:
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
        if 1 <= app.skyscraper.floor <= 3:
            app.stepsOccurred += 1
            if (len(app.enemyList) < 3 and app.stepsOccurred > app.interval
                and app.enemySpawnCount < 5): # spawns a ghost every so often
                app.stepsOccurred = 0 # resets time
                app.interval = random.randint(180, 420)
                app.enemy.spawn()
                app.enemySpawnCount += 1
            index = 0
            while index < len(app.enemyList):
                app.enemyList[index].move()
                app.enemyList[index].isHit() # deletes bullets that hit ghost
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
            for saw in app.bladeList:
                if saw.touchingPlayer() and app.generalStepCounter % 15 == 0:
                    app.character.health -= 100
                if app.generalStepCounter % 2 == 0: # updates every 2 frames
                    saw.spriteCount = ((saw.spriteCount + 1)
                                     % len(saw.spriteList))
                saw.move()
            if app.generalStepCounter % (60 // app.skyscraper.floor) == 0:
                # increases difficulty by having the ghost damage the player
                # more times per seconds
                app.character.isTouchingEnemy()
            if app.generalStepCounter > 18000:
                app.generalStepCounter = 0
            if app.startCountingShots == True:
                app.stepsPassed += 1
            if app.stepsPassed > 1200: # prevent memory from dying
                app.stepsPassed = 0
            app.dx = 0 # reset dx in case player isn't moving
            if app.character.isDead():
                app.gameOver = True
    if app.gameOver == True and app.fadeIncrement < 100:
        app.fadeIncrement += 1

def onKeyHold(app, keys):
    if app.paused == False and app.gameOver == False:
        if app.skyscraper.floor == 0 or app.skyscraper.floor == 4:
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
        elif 1 <= app.skyscraper.floor <= 3:
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
    if app.paused == False and app.gameOver == False:
        if (key == 'w' and app.character.jumping == False and
            not app.character.colliding()):
            app.character.dy = -18
            app.character.jumping = True
        elif (key == 's' and app.skyscraper.floor <= 3 and # to enter door
            app.skyscraper.atDoor(app.character.x, app.character.y)):
            if (app.skyscraper.floor == 0 or (app.skyscraper.floor > 0 and
                app.enemySpawnCount <= 5 and app.enemyList == [])):
                app.mapX = 0 # reset coords
                app.mapY = 0
                app.skyscraper.floor += 1
                app.character.load()
                app.skyscraper.loadFloor()
                app.bladeList = [] # reset for each floor
                app.enemySpawnCount = 0
                spinningBlade.SpinningBlade.lastX = 300
                spinningBlade.SpinningBlade.floatingLastX = 300
                numberOfBlades = 0
                if app.skyscraper.floor == 1:
                    numberOfBlades = 3
                elif app.skyscraper.floor == 2:
                    numberOfBlades = 8
                elif app.skyscraper.floor == 3:
                    numberOfBlades = 19
                for i in range(numberOfBlades):
                    app.blade.load()
        elif key == 'j' and 1 <= app.skyscraper.floor <= 3:
            app.startCountingShots = True
            if app.stepsPassed >= app.attackSpeed:
                app.bullet.spawnPlayerBullet()
                app.stepsPassed = 0
    if key == 'p' and app.paused == False and app.gameOver == False:
        app.paused = True
    elif key == 'p' and app.paused == True and app.gameOver == False:
        app.paused = False

def onMousePress(app, mouseX, mouseY): # for pressing buttons
    if (app.button.x <= mouseX <= app.button.x + app.button.width and
        app.button.y <= mouseY <= app.button.y + app.button.height and
        app.skyscraper.floor == -1):
        app.skyscraper.floor = 0
        app.character.load()
        app.skyscraper.loadFloor()

def main():
    runApp()

main()