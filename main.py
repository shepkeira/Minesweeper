"""
 Program created from base on
 http://programarcadegames.com/index.php?chapter=array_backed_grids&lang=en

 Creator: Keira
"""
import pygame
import board
import constants
import levels


def begin(level):
    things = levels.get_level_things(level)
    SIZE = things[0]
    mines = things[1]

    # This sets the WIDTH and HEIGHT of each grid location
    WIDTH = 20
    HEIGHT = 20

    # This sets the margin between each cell
    MARGIN = 5

    # create grid holding information
    grid = []
    for row in range(SIZE):
        # Add an empty array that will hold each cell
        # in this row
        grid.append([])
        for column in range(SIZE):
            grid[row].append(0)  # Append a cell

    # create grid holding display information
    grid_display = []
    for row in range(SIZE):
        # Add an empty array that will hold each cell
        # in this row
        grid_display.append([])
        for column in range(SIZE):
            grid_display[row].append(0)  # Append a cell

    grid = board.set_mines(grid, mines)

    grid = board.set_nums(grid, SIZE)

    open_areas = board.set_open_areas(grid, SIZE)

    # Initialize pygame
    pygame.init()

    # Set the HEIGHT and WIDTH of the screen

    SCREEN_HEIGHT = (HEIGHT + MARGIN) * SIZE + MARGIN
    SCREEN_WIDTH = (WIDTH + MARGIN) * SIZE + MARGIN

    WINDOW_SIZE = [constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT]
    screen = pygame.display.set_mode(WINDOW_SIZE)

    # Set title of screen
    pygame.display.set_caption("MINESWEEPER")

    mine_image = pygame.image.load("mine.png").convert()
    mine_image = pygame.transform.scale(mine_image, (WIDTH, HEIGHT))

    flag_image = pygame.image.load("flag.png").convert()
    flag_image = pygame.transform.scale(flag_image, (WIDTH, HEIGHT))

    # Set Up Text
    # Select the font to use, size, bold, italics
    font = pygame.font.SysFont('Calibri', 25, True, False)

    # Render the text. "True" means anti-aliased text.
    # Black is the color. The variable BLACK was defined
    # above as a list of [0, 0, 0]
    # Note: This line creates an image of the letters,
    # but does not put it on the screen yet.
    GAME_OVER = font.render("GAME OVER", True, constants.WHITE)
    WIN = font.render("WIN", True, constants.WHITE)

    # Set game over and win variables to False
    game_over = False
    win = False

    # Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop
            if win or not game_over:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        # User clicks the mouse. Get the position
                        pos = pygame.mouse.get_pos()
                        # Change the x/y screen coordinates to grid coordinates
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        # Set that location to one
                        if 0 <= row < SIZE and 0 <= column < SIZE:
                            grid_display[row][column] = 1
                        # if click in square in open area open whole open area
                        for area in open_areas:
                            for square in area:
                                if [row, column] == square:
                                    for each in area:
                                        grid_display[each[0]][each[1]] = 1
                    elif event.button == 3:  # right click sets flag
                        # User clicks the mouse. Get the position
                        pos = pygame.mouse.get_pos()
                        # Change the x/y screen coordinates to grid coordinates
                        column = pos[0] // (WIDTH + MARGIN)
                        row = pos[1] // (HEIGHT + MARGIN)
                        if 0 <= row < SIZE and 0 <= column < SIZE:
                            if grid_display[row][column] == 0:
                                # Set that location to one
                                grid_display[row][column] = 2

        # check if all mines are flagged
        win = True
        for square in mines:
            if grid_display[square[0]][square[1]] != 2:
                win = False

        # Set the screen background
        screen.fill(constants.BLACK)

        # Draw the grid
        for row in range(SIZE):
            for column in range(SIZE):
                color = constants.BLUE
                if grid_display[row][column] == 1:
                    color = constants.LIGHT_BLUE
                pygame.draw.rect(screen,
                                 color,
                                 [(MARGIN + WIDTH) * column + MARGIN,
                                  (MARGIN + HEIGHT) * row + MARGIN,
                                  WIDTH,
                                  HEIGHT])
        # Change if clicked
        for row in range(SIZE):
            for column in range(SIZE):
                if grid_display[row][column] == 1:
                    if grid[row][column] != 0:
                        if grid[row][column] != 9:
                            text = font.render(str(grid[row][column]), True, constants.BLACK)
                            screen.blit(text, [(MARGIN + WIDTH) * column + MARGIN,
                                               (MARGIN + HEIGHT) * row + MARGIN])
                        else:  # hit mine
                            screen.blit(mine_image, [(MARGIN + WIDTH) * column + MARGIN,
                                                     (MARGIN + HEIGHT) * row + MARGIN])
                            # display if game over
                            screen.blit(GAME_OVER, [WIDTH / 2, HEIGHT / 2])
                            game_over = True
                if grid_display[row][column] == 2:
                    screen.blit(flag_image, [(MARGIN + WIDTH) * column + MARGIN,
                                             (MARGIN + HEIGHT) * row + MARGIN])

        # display if win
        if win:
            screen.blit(WIN, [WIDTH / 2, HEIGHT / 2])

        # Limit to 60 frames per second
        clock.tick(60)

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

    # Be IDLE friendly. If you forget this line, the program will 'hang'
    # on exit.
    # pygame.quit()
    # GUI.start()
