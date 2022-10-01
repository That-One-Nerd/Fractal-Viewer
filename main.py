from objects import *
from useful import *

from threading import Thread
import pygame

def main():
    try:
        print("Initializing...")
        data.multithreading = settings.useMultithreading
        data.running = True
        pygame.init()
        pygame.display.set_mode(settings.resolution)
        data.display = pygame.display.get_surface()
        data.pixelScale = int(pow(2, settings.maxPixelScale - 1))

        if settings.useMultithreading: beginMultithreading()

        print("Ready")

        minPixelScale = int(pow(2, settings.minPixelScale - 1))
        while data.running and data.pixelScale >= minPixelScale:
            render()
            if not data.multithreading: pygame.display.update()
            getInputs()
            data.pixelScale /= 2

        data.multithreading = False
        pygame.display.update()
        while data.running:
            getInputs()
    finally:
        print("Closing...")
        if settings.useMultithreading: endMultithreading()
        pygame.quit()

# begins any threads required for multithreading
def beginMultithreading():
    print("Beginning multithreading")
    data.monitor = Thread(target=m_Monitor)
    data.monitor.start()

# kills all threads other than the main thread
def endMultithreading():
    print("Ending multithreading")
    data.multithreading = False
    data.monitor.join()

# a monitor to constantly update the screen.
# only used in multithreading.
def m_Monitor():
    while data.multithreading:
        pygame.display.update()

# gets pygame inputs
def getInputs():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            data.running = False
            return

# renders a screen of fractal
def render():
    for y in range(int(settings.resolution[1] / data.pixelScale)):
        if data.multithreading:
            pygame.draw.rect(data.display, (0, 0, 0), (0, y * data.pixelScale, settings.resolution[0], data.pixelScale))
            pygame.draw.rect(data.display, (255, 255, 255), (0, (y + 1) * data.pixelScale, settings.resolution[0], data.pixelScale))
        for x in range(int(settings.resolution[0] / data.pixelScale)):
            unit = pixelsToUnits(x * data.pixelScale, y * data.pixelScale)
            pygame.draw.rect(data.display, getColor(unit[0], unit[1]), (x * data.pixelScale, y * data.pixelScale, data.pixelScale, data.pixelScale))
        getInputs()

# converts a given display pixel into the proper world coordinates.
# this is where the zoom and offset are factored in.
def pixelsToUnits(x, y):
    fX = x / settings.resolution[0]
    fY = y / settings.resolution[1]
    fX = fX * 2 - 1
    fY = fY * 2 - 1
    fX *= settings.scale
    fY *= settings.scale
    fX += settings.offset[0]
    fY += settings.offset[1]
    return (fX, fY)

# gets a color for a given coordinate.
# this function is just a handler for fractalContains()
def getColor(x, y):
    insideColor = (0, 0, 0)
    outsideColor = (0, 0, 255)

    val = fractalContains(x, y)
    if val == -1: return insideColor
    
    percent = val / settings.fractalIterations
    percent = sqrt(percent).real
    return(outsideColor[0] * percent, outsideColor[1] * percent, outsideColor[2] * percent)

# returns -1 if the point x + yi is contained in the fractal, otherwise
# it returns how many iterations it took to be determined outside.
# this is also where you can modify the recursive function
def fractalContains(x, y):
    c = complex(x, y)
    x = c
    for i in range(settings.fractalIterations):
        x = x * x + c
        if x.__abs__() >= 2: return i
    return -1

if __name__ == "__main__": main()
