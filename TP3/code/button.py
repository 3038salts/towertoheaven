from cmu_graphics import * # cmu graphics module
class Button:
    def __init__(self, x, y, width, height, text):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    def drawButton(self):
        drawRect(self.x, self.y, self.width, self.height, fill = rgb(252, 200, 186))
        drawLabel(self.text, self.x + self.width // 2, self.y + self.height // 2, size = 30)