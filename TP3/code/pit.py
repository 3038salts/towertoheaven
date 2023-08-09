import math
class Pit():
    def __init__(self):
        self.modifiedX = self.x = 0
        self.modifiedY = self.y = 0
    
    def drawPit(self):
        pass

    def loadPit(self):
        pass

    def touchingPlayer(self):
        if (self.modifiedX + self.width // 2 > # pit right over player left
            app.character.x - app.character.width // 2
            and self.modifiedX - (self.width // 2) < # pit left over player right
            app.character.x + app.character.width // 2
            and rounded(self.modifiedY - (self.height // 2)) <
            # pit top over player bottom 
            app.character.y + app.character.height // 2
            and rounded(self.modifiedY + (self.height // 2)) >
            app.character.y - app.character.width // 2):
            # pit bottom over player top
            return True
        return False