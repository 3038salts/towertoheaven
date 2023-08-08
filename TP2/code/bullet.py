from cmu_graphics import *
import random
class Bullet:
    def __init__(self, x, y, dx, dy):
        self.modifiedX = self.x = x #when spawned, should appear to the right or left of player
        #we can choose this depending on direction the player is walking,
        #where the enemy is facing, or mouseX, mouseY
        self.modifiedY = self.y = y
        self.dx = dx
        self.dy = dy
        self.width = 32
        self.height = 16
    
    def drawBullet(self):
        color = rgb(174, 128, 215)
        # print("bullet", self.modifiedX, self.modifiedY)
        # print("player", app.character.x, app.character.y)
        drawRect(self.modifiedX, self.modifiedY, self.width, self.height, fill = color, align = 'center')

    def spawnPlayerBullet(self):
        if app.dx < 0: # player is moving right
            # appears to the right of player
            x = app.character.x + app.character.width // 2
            # print("moving right", x)
        elif app.dx > 0: # player is moving left
            # appears to the left of player
            x = app.character.x - app.character.width // 2
            # print("moving left", x)
        else: # player is standing still
            # appears at the center of player
            x = app.character.x
            # print("not moving", x)
        y = app.character.y # character center for y
        closestEnemyDistance = None
        closestEnemy = None
        if len(app.enemyList) != 0:
            for enemy in app.enemyList:
                gap = distance(app.character.x, app.character.y, app.enemy.modifiedX,
                                    app.enemy.modifiedY)
                if closestEnemyDistance == None or gap < closestEnemyDistance:
                    closestEnemyDistance = gap
                    closestEnemy = enemy
            if closestEnemy.modifiedX > app.character.x: #enemy to the right
                dx = 4
            elif closestEnemy.modifiedX < app.character.x: #enemy to the left
                dx = -4
            else: #if the player doesn't evade the ghost for some reason
                # method from https://docs.python.org/3/library/random.html
                dx = random.choice([-1, 1])
            if closestEnemy.modifiedY < app.character.y: #enemy above
                dy = -4
            elif closestEnemy.modifiedY > app.character.y: #enemy below
                dy = 4
            else: #if the player doesn't evade the ghost for some reason
                # method from https://docs.python.org/3/library/random.html
                dy = random.choice([-1, 1])
            # print("spawn 2", x, y)
            app.bulletList.append(Bullet(x, y, dx, dy))
    
    def spawnEnemyBullet(self):
        pass

    def move(self):
        self.x += self.dx + app.dx
        # print(app.dx)
        self.y += self.dy
        self.modifiedX = self.x
        self.modifiedY = self.y
    
    def hit(self):
        pass

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)