import pygame, random

#use 2d vectors

vector = pygame.math.Vector2

#init pygame
pygame.init()

#set display surface (tile size is 32X32 - 40 tiles wide, 23 tiles high)
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 736
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Zombie Knight")

#Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

#Define classes

class Game():
    """ A class to help manage gameplay """

    def __init__(self):
        """initialize the game"""
        pass

    def update(self):
        """update the game"""
        pass

    def draw(self):
        """draw the game HUD"""
        pass

    def add_zombie(self):
        """add a zombie to the game"""
        pass

    def check_collisions(self):
        """Check collisions that affect gameplay"""
        pass

    def check_round_completion(self):
        """ check if the player survived a night"""
        pass

    def check_game_over(self):
        """ Check to see if the player lost the game """
        pass

    def start_new_round(self):
        """Start a new night"""
        pass
    
    def pause_game(self):
        """Pause the game"""
        pass

    def reset_game(self):
        """Reset the game"""
        pass

class Tile(pygame.sprite.Sprite):
    """A class to represent a 32X32 pixel area in our display"""
    def __init__(self):
        """Initialize the tile"""
        pass

class Player(pygame.sprite.Sprite):
    """ A class that the user can control """
    def __init__(self):
        """ Initialize the player"""
        pass

    def update(self):
        """ update the player"""
        pass
    
    def move(self):
        """ move the player"""
        pass

    def check_collisions(self):
        """ check for collissions with platforms and portals"""
        pass

    def check_animations(self):
        """ check to see if jump / fire animations should run"""
        pass

    def jump(self):
        """ Jump upwards if on a platform"""
        pass

    def fire(self):
        """Fire a 'bullet' from a sword"""
        pass

    def reset(self):
        """ Reset the player's poisition """
        pass

    def animate(self):
        """ animate player actions """
        pass

class Bullet(pygame.sprite.Sprite):
    """ A projective launched by the player """

    def __init__(self):
        """Initialize the bullet"""
        pass

    def update(self):
        """Update the bullet"""
        pass

class Zombie(pygame.sprite.Sprite):
    """ an enemy class that moves across the screen """
    def __init__(self):
        """ Initialize the zombie"""
        pass

    def update(self):
        """ update the zombie"""
        pass
    
    def move(self):
        """ move the zombie"""
        pass

    def check_collisions(self):
        """ check for collissions with platforms and portals"""
        pass

    def check_animations(self):
        """ check to see if jump / fire animations should run"""
        pass

    def animate(self):
        """ animate zombie actions """
        pass        

class RubyMaker(pygame.sprite.Sprite):
    """A tile that is animated. A ruby will be generated here. """

    def __init__(self):
        """Initialize the ruby maker"""
        pass
    
    def update(self):
        """Update the ruby maker"""
        pass

    def animate(self):
        """Animate the ruby maker"""
        pass

class Ruby(pygame.sprite.Sprite):
    """ A class hte player must collect to earn points and health"""

    def __init__(self):
        """Initialize the ruby"""
        pass

    def update(self):
        """Update the ruby"""
        pass

    def move(self):
        """move the ruby"""
        pass

    def check_collisions(self):
            """Check for collisions with platforms and portals"""
            pass

    def animate(self):
            """animate the ruby"""
            pass
    

class Portal(pygame.sprite.Sprite):
    """ A class that if collided with will transport you"""

    def __init__(self):
        """Initialize the portal"""
        pass

    def update(self):
        """Update the portal"""
        pass

    def animate(self):
            """animate the portal"""
            pass


#Load in a background image
background_image = pygame.image.load('images/background.png')
background_image = pygame.transform.scale(background_image, (1280, 736))
background_rect = background_image.get_rect()
background_rect.topleft = (0,0)

#The main game loop
running = True

while running:
    #Check to see if the user wants to quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Blit the background
    display_surface.blit(background_image, background_rect)


    #update display and tick the clock
    pygame.display.update()
    clock.tick(FPS)

#End the game
pygame.quit()


