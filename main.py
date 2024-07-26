# PyGame template.
 
# Import standard modules.
import sys
 
# Import non-standard modules.
import pygame
from pygame.locals import *
 
def update(dt):
  # dt is the amount of time passed since last frame.
  # Update the game
  
  # Go through events that are passed to the script by the window.
  for event in pygame.event.get():

    if event.type == QUIT:
      pygame.quit()
      sys.exit() 
    # Handle other events as you wish.
 
def draw(screen):

  screen.fill((0, 0, 0)) # Fill the screen with black.
  # Redraw screen here.
  
  
  pygame.display.flip() # Flip the display so that the things we drew actually show up.
 
def runPyGame():
  # Initialise PyGame.
  pygame.init()
  
  # Set up the clock. This will tick every frame and thus maintain a relatively constant framerate. Hopefully.
  fps = 60.0
  fpsClock = pygame.time.Clock()
  
  # Set up the window.
  width, height = 640, 480
  screen = pygame.display.set_mode((width, height))
  
  # screen is the surface representing the window.
  # PyGame surfaces can be thought of as screen sections that you can draw onto.
  # You can also draw surfaces onto other surfaces, rotate surfaces, and transform surfaces.
  
  # Main game loop.
  dt = 1/fps # dt is the time since last frame.
  while True:
    update(dt)
    draw(screen)
    
    dt = fpsClock.tick(fps)

runPyGame()