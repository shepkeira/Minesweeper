"""
 Program created from base on
 http://programarcadegames.com/index.php?chapter=array_backed_grids&lang=en

 Creator: Keira
"""
import pygame
import main
import Help_Page
import constants


def start():

    pygame.init()

    WINDOW_SIZE = [constants.SCREEN_WIDTH, constants.SCREEN_WIDTH]
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
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()

                    if 75 < pos[0] < 175 and 25 < pos[1] < 55:
                        print("Easy")
                        main.begin(1)
                    if 75 < pos[0] < 175 and 75 < pos[1] < 105:
                        print("Medium")
                        main.begin(2)
                    if 75 < pos[0] < 175 and 125 < pos[1] < 155:
                        print("Hard")
                        main.begin(3)
                    if 75 < pos[0] < 175 and 175 < pos[1] < 205:
                        print("Help")
                        Help_Page.help_page()

        screen.fill(constants.BLACK)

        pygame.draw.rect(screen, constants.LIGHT_BLUE, [75, 25, 100, 30])
        screen.blit(font.render("Easy", True, constants.WHITE), [75, 25])
        pygame.draw.rect(screen, constants.LIGHT_BLUE, [75, 75, 100, 30])
        screen.blit(font.render("Medium", True, constants.WHITE), [75, 75])
        pygame.draw.rect(screen, constants.LIGHT_BLUE, [75, 125, 100, 30])
        screen.blit(font.render("Hard", True, constants.WHITE), [75, 125])
        pygame.draw.rect(screen, constants.LIGHT_BLUE, [75, 175, 100, 30])
        screen.blit(font.render("Help", True, constants.WHITE), [75, 175])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    pygame.quit()


start()
