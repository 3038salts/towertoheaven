from cmu_graphics import *
class Bullet:
    def __init__(self, x, y, dx, dy):
        self.x = 0 #when spawned, should appear to the right or left of player
        #we can choose this depending on direction the player is walking,
        #where the enemy is facing, or mouseX, mouseY
        self.y = 0
        self.dx = 0
        self.dy = 0
    
    def drawBullet(self);

    def spawnPlayerBullet(self):
        if app.dx < 0: # player is moving right
            # appears to the right of player
            x = app.character.x + app.character.width // 2
        elif app.dx > 0: #player is moving left
            # appears to the left of player
            x = app.character.x - app.character.width // 2
        else: #player is standing still
            #appears center of player
            x = app.character.x
        y = app.character.y #character center for y
        closestEnemyDistance = None
        closestEnemy = None
        if len(app.enemyList) != 0:
            for enemy in app.enemyList:
                distance = distance(app.character.x, app.character.y, app.enemy.x,
                                    app.enemy.y)
                if distance == None or distance < closestEnemyDistance:
                    closestEnemyDistance = distance
                    closestEnemy = enemy
            if closestEnemy.x > app.character.x: #enemy to the right
                dx = 2
            elif closestEnemy.x < app.character.x: #enemy to the left
                dx = -2
            else: #if the player doesn't evade the ghost for some reason
                # method from https://docs.python.org/3/library/random.html
                dx = random.choice([-1, 1])
            if closestEnemy.y < app.character.y: #enemy below
                dy = 2
            elif closestEnemy.y > app.character.y: #enemy above
                dy = -2
            else: #if the player doesn't evade the ghost for some reason
                # method from https://docs.python.org/3/library/random.html
                dy = random.choice([-1, 1])
            app.bulletList.append(Bullet(x, y, dx, dy))
    
    def spawnEnemyBullet(self):
        pass

    def hit(self):
        pass

    @staticmethod
    def distance(x1, y1, x2, y2):
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** (1/2)