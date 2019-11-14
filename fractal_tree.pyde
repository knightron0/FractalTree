# this is the main driver code

import edge as Edge
import rec 
def setup():
    size(1000, 600)
    colorMode(HSB)


def draw():
    background(255)
    # change second last parameter for different degrees
    # change last parameter for different depths
    root = Edge.edge(width / 2, height, 200, 0, PI/4, 10)
    rec.generate(root)
