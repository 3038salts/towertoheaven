class Bullet:
    def __init__(self):
        self.x = 0 #when spawned, should appear to the right or left of player
        #we can choose this depending on direction the player is walking,
        #where the enemy is facing, or mouseX, mouseY
        self.y = 0
        self.dx = 0
        self.dy = 0
    
    def spawn(self):
        pass

    def hit(self):
        pass