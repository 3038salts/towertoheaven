from cmu_graphics import *
import random
class Bullet:
    def __init__(self, x, y, dx, dy, width, height):
        self.modifiedX = self.x = x #when spawned, should appear to the right or left of player
        #we can choose this depending on direction the player is walking,
        #where the enemy is facing, or mouseX, mouseY
        self.modifiedY = self.y = y
        self.dx = dx
        self.dy = dy
        self.width = width
        self.height = height
    
    def drawBullet(self):
        color = rgb(174, 128, 215)
        drawRect(self.modifiedX, self.modifiedY, self.width, self.height, fill = color, align = 'center')

    def spawnPlayerBullet(self):
        if app.dx < 0: # player is moving right
            # appears to the right of player
            x = app.character.x + app.character.width // 2
        elif app.dx > 0: # player is moving left
            # appears to the left of player
            x = app.character.x - app.character.width // 2
        else: # player is standing still
            # appears at the center of player
            x = app.character.x
        y = app.character.y # character center for y
        closestEnemyDistance = None
        closestEnemy = None
        if len(app.enemyList) != 0:
            for enemy in app.enemyList:
                gap = distance(app.character.x, app.character.y, enemy.modifiedX,
                                    enemy.modifiedY)
                if closestEnemyDistance == None or gap < closestEnemyDistance:
                    closestEnemyDistance = gap
                    closestEnemy = enemy
            if closestEnemy.modifiedX > app.character.x: #enemy to the right
                dx = 7
            elif closestEnemy.modifiedX < app.character.x: #enemy to the left
                dx = -7
            else: #if the player doesn't evade the ghost for some reason
                # method from https://docs.python.org/3/library/random.html
                dx = random.choice([-4, 4])
            if (closestEnemy.modifiedY - closestEnemy.height // 2 <=
                app.character.y <= closestEnemy.modifiedY +
                closestEnemy.height // 2): # similar enough y
                dy = 0
            elif closestEnemy.modifiedY < app.character.y: # enemy above
                dy = -2
            elif closestEnemy.modifiedY > app.character.y: # enemy below
                dy = 2
            else: #if the player doesn't evade the ghost for some reason
                # method from https://docs.python.org/3/library/random.html
                dy = random.choice([-4, 4])
            width = 32
            height = 16
            app.bulletList.append(Bullet(x, y, dx, dy, width, height))

    def move(self):
        self.x += self.dx + app.dx
        self.y += self.dy
        self.modifiedX = self.x
        self.modifiedY = self.y

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)