from cmath import sqrt
from random import random

def magXY(x1, y1, x2, y2):
    diffX = x2 - x1
    diffY = y2 - y1
    return sqrt(diffX * diffX + diffY * diffY).real
def magXYZ(x1, y1, z1, x2, y2, z2):
    diffX = x2 - x1
    diffY = y2 - y1
    diffZ = z2 - z1
    return sqrt(diffX * diffX + diffY * diffY + diffZ * diffZ).real

def normalizeColor(color):
    mag = magXYZ(0, 0, 0, color[0], color[1], color[2]) / 255
    return (color[0] / mag, color[1] / mag, color[2] / mag)

def randomColor():
    return (randomInt(255), randomInt(255), randomInt(255))

def randomInt(max):
    return int(random() * max)
