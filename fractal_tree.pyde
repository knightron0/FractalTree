import edge as Edge
import rec 
def setup():
    size(600, 600)
    colorMode(HSB)


def draw():
    background(255)
    root = Edge.edge(width / 2, height, 200, 0, map(mouseX, 0, width, 0, PI/2))
    rec.generate(root)
