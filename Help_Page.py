"""
 Program created from base on
 http://programarcadegames.com/index.php?chapter=array_backed_grids&lang=en

 Creator: Keira
"""
import pygame
import constants


def help_page():

    SCREEN_HEIGHT = 255
    SCREEN_WIDTH = 255

    pygame.init()

    WINDOW_SIZE = [SCREEN_WIDTH, SCREEN_WIDTH]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("MINESWEEPER")

    # Set Up Text
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    GAME_OVER = font.render("GAME OVER", True, constants.WHITE)

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

        screen.fill(constants.BLACK)

        screen.blit(font.render("This is the help page", True, constants.WHITE), [75, 25])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()
