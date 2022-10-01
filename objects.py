from threading import Thread
import pygame

# this is data for the program, and shouldn't be manually modified
class data:
    display = pygame.Surface
    monitor = Thread
    multithreading = bool
    running = bool
    pixelScale = int

# these are user settings. can be set to whatever
class settings:
    # amount of iterations needed for the fractal
    fractalIterations = 256
    # beginning upscale level
    maxPixelScale = 8
    # ending upscale level
    minPixelScale = 1
    # offset in world coordinates
    offset = (-0.5, 0)
    # the resolution will work best when set to a power of 2
    resolution = (512, 512)
    # zoom level
    scale = 2
    # enable/disable multithreading
    useMultithreading = True
