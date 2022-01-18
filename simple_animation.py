# Simple Animation with PyGame, Isaiah Stevens, 1/4/22, 1:14PM, v0,0

import pygame, sys, time
from pygame.locals import *

# Setup PyGame
pygame.inti()

# Setup the Window
WINDOWWIDTH = 400
WINDOWHEIGHT = 400
windowSurface = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT), 0, 32)
pygame.display.set_caption('Animation Example!')

# Setup the  direction variables.
DOWNLEFT = 'downleft'
DOWNRIGHT = 'downright'
UPLEFT = 'upleft'
UPRIGHT = 'upright'

MOVESPEED = 4
