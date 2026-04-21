class Point(tuple):
    def __new__(cls, x, y):
        return super(Point, cls).__new__(cls, (x, y))

    def __init__(self, x, y):
        self.x = self[0]
        self.y = self[1]

class ShapeTransforms:
    @staticmethod
    def translate(preimage:Point,deltaX=0,deltaY=0):
        image = Point(preimage.x + deltaX,preimage.y+deltaY)
        return image
    
    @staticmethod
    def midPoint(x1,x2):
        return (x1 + x2) // 2
    
