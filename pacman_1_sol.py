import pygame, sys, random, time
from pygame.locals import K_a, K_d, K_w, K_s, QUIT
import os
pygame.init()

# Constants
WIDTH = 630
BOTTOM_BAR_HEIGHT = 50
HEIGHT = 726
TILES_WIDE = 30
TILES_HIGH  = 33
TILE_WIDTH = WIDTH // TILES_WIDE
TILE_HEIGHT = HEIGHT // TILES_HIGH
BLACK = (0,0,0)
RED = (255,0,0)
WHITE = (255,255,255)
CLOCK = pygame.time.Clock()
BOARD_COUNTER = 5
SPRITE_WIDTH = 30

# Board
# 0 = empty black rectangle, 1 = dot, 2 = big dot, 3 = vertical line,
# 4 = horizontal line, 5 = top right, 6 = top left, 7 = bot left, 8 = bot right
# 9 = gate 
board = [
[6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5],
[3, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 6, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 2, 3, 0, 0, 3, 1, 3, 0, 0, 0, 3, 1, 3, 3, 1, 3, 0, 0, 0, 3, 1, 3, 0, 0, 3, 2, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 5, 1, 3, 7, 4, 4, 5, 0, 3, 3, 0, 6, 4, 4, 8, 3, 1, 6, 4, 4, 4, 4, 8, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 6, 4, 4, 8, 0, 7, 8, 0, 7, 4, 4, 5, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[8, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 9, 9, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 7],
[4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
[4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 0, 3, 0, 0, 0, 0, 0, 0, 3, 0, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4],
[5, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 7, 4, 4, 4, 4, 4, 4, 8, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 6],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 0, 0, 0, 0, 0, 3, 1, 3, 3, 0, 6, 4, 4, 4, 4, 4, 4, 5, 0, 3, 3, 1, 3, 0, 0, 0, 0, 0, 3],
[3, 6, 4, 4, 4, 4, 8, 1, 7, 8, 0, 7, 4, 4, 5, 6, 4, 4, 8, 0, 7, 8, 1, 7, 4, 4, 4, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 5, 1, 6, 4, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 4, 5, 1, 6, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 5, 3, 1, 7, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 8, 1, 3, 6, 4, 8, 1, 3, 3],
[3, 3, 2, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 2, 3, 3],
[3, 7, 4, 5, 1, 3, 3, 1, 6, 5, 1, 6, 4, 4, 4, 4, 4, 4, 5, 1, 6, 5, 1, 3, 3, 1, 6, 4, 8, 3],
[3, 6, 4, 8, 1, 7, 8, 1, 3, 3, 1, 7, 4, 4, 5, 6, 4, 4, 8, 1, 3, 3, 1, 7, 8, 1, 7, 4, 5, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 3, 3, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 3, 1, 6, 4, 4, 4, 4, 8, 7, 4, 4, 5, 1, 3, 3, 1, 6, 4, 4, 8, 7, 4, 4, 4, 4, 5, 1, 3, 3],
[3, 3, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 7, 8, 1, 7, 4, 4, 4, 4, 4, 4, 4, 4, 8, 1, 3, 3],
[3, 3, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 3, 3],
[3, 7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8, 3],
[7, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 4, 8]
         ]

class Player:
    def __init__(self) -> None:
        self.width = SPRITE_WIDTH
        self.height = SPRITE_WIDTH
        path_to_image = os.path.join(os.path.dirname(__file__),"sprites","pacman","pacman.png")
        image = pygame.image.load(path_to_image).convert()
        self.img = pygame.transform.scale(image,size=(self.width,self.height))
        self.rect = pygame.Rect(0,0,self.width,self.height)
        self.rect.centerx = 15 * TILE_WIDTH
        self.rect.centery = (24 * TILE_HEIGHT) + 10
        self.speed = 5
        # direction = 0,1,2,3 corresponds to Left, Right, Up, Down
        self.direction = 1
        self.score = 0
        self.powered_up = False
        self.power_up_length = 7 # seconds
        self.power_up_timer = 0
        self.previous_time = 0
    
    def move(self):
        ## TO BE DONE BY STUDENTS ##
        # set direction
        keys = pygame.key.get_pressed()

        horizontal = (self.direction == 0) or (self.direction == 1)
        vertical = (self.direction == 2) or (self.direction == 3)

        # Processing inputs and checking if allowed to move in desired direction.
        lower = 7 
        upper = 13
        if horizontal:
            # Attempting to turn left or right while currently going left or right
            if keys[K_a]:
                self.direction = 0
            if keys[K_d]:
                self.direction = 1
            # Attempting to turn up or down at a junction
            # Imagine a tile has index 0..20. You must be within 3 pixels of the center 10.5 to turn at a junction
            if lower <= self.rect.centerx % TILE_WIDTH <= upper:
                if keys[K_w]:
                        self.direction = 2
                if keys[K_s]:
                        self.direction = 3
        if vertical:
            # Attempting to turn left or right at a junction
            if lower <= self.rect.centery % TILE_HEIGHT <= upper:
                if keys[K_a]:
                    self.direction = 0
                if keys[K_d]:
                    self.direction = 1
            # Attempting to turn up or down while currently going up or down
            if keys[K_w]:
                    self.direction = 2
            if keys[K_s]:
                    self.direction = 3
        
        # Process direction for Left, Right, Up and Down
        if self.direction == 0:
            self.rect.centerx -= self.speed
        if self.direction == 1:
            self.rect.centerx += self.speed
        if self.direction == 2:
            self.rect.centery -= self.speed
        if self.direction == 3:
            self.rect.centery += self.speed

        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.left > WIDTH:
            self.rect.right = 0
        ## END OF STUDENT CODE ##

    def draw(self,screen: pygame.Surface):
        ## TO BE DONE BY STUDENTS ##
        screen.blit(self.img,self.rect)
        pygame.draw.circle(screen,'blue',self.rect.center,3)
        ## END OF STUDENT CODE ##
    
    def actions(self, board):
        ## TO BE DONE BY STUDENTS ##
        # Eating pellets
        if 0 < (self.rect.centerx  // TILE_WIDTH) < (TILES_WIDE - 1):
            tile_x = self.rect.centerx // TILE_WIDTH
            tile_y = self.rect.centery // TILE_HEIGHT
            if board[tile_y][tile_x] == 1:
                self.score += 10
                board[tile_y][tile_x] = 0
            if board[tile_y][tile_x] == 2:
                self.score += 50
                self.powered_up = True
                self.power_up_timer = self.power_up_length
                self.previous_time = time.time()
                board[tile_y][tile_x] = 0

        # Reducing the timer
        if self.powered_up:
            if self.power_up_timer > 0:
                now = time.time()
                delta = now - self.previous_time
                self.power_up_timer -= delta
                self.previous_time = now
            else:
                self.powered_up = False
        ## END OF STUDENT CODE ##

    def die(self):
        print("DEAD")

    def eat_ghost(self):
        self.score += 200
   
def to_tile(x,y):
    return x // TILE_WIDTH, y //TILE_HEIGHT

def draw_board(screen: pygame.Surface, show_powerup):
    wall_colour = WHITE
    food_colour = WHITE
    wall_background = BLACK
    for row in range(TILES_HIGH):
        for col in range(TILES_WIDE):
            if board[row][col] == 0:
                pygame.draw.rect(screen,BLACK,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
            elif board[row][col] == 1:
                radius = 2
                pygame.draw.rect(screen,BLACK,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
                pygame.draw.circle(screen,food_colour,(col*TILE_WIDTH+TILE_WIDTH/2,row*TILE_HEIGHT+TILE_HEIGHT/2),radius)
            elif board[row][col] == 2 and show_powerup:
                radius = 8
                pygame.draw.circle(screen,food_colour,(col*TILE_WIDTH+TILE_WIDTH/2,row*TILE_HEIGHT+TILE_HEIGHT/2),radius)
            elif board[row][col] == 3:
                # Background
                pygame.draw.rect(screen,wall_background,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
                # Foreground
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT, 0.4 * TILE_WIDTH, TILE_HEIGHT))
            elif board[row][col] == 4:
                # Background
                pygame.draw.rect(screen,wall_background,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT, TILE_WIDTH, TILE_HEIGHT))
                # Foreground
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT + (0.3 * TILE_HEIGHT), TILE_WIDTH, 0.4 * TILE_HEIGHT))
            # top right
            elif board[row][col] == 5:
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT + (0.3 * TILE_WIDTH),0.4*TILE_WIDTH,0.7*TILE_HEIGHT+1))
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT + (0.3 * TILE_WIDTH),0.7*TILE_WIDTH,0.4*TILE_HEIGHT))
            # top left
            elif board[row][col] == 6:
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT + (0.3 * TILE_WIDTH),0.4*TILE_WIDTH,0.7*TILE_HEIGHT+1))
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT + (0.3 * TILE_WIDTH),0.7*TILE_WIDTH+1,0.4*TILE_HEIGHT))
            # bottom left
            elif board[row][col] == 7:
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT-1, 0.4*TILE_WIDTH,0.7*TILE_HEIGHT))
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT + (0.3 * TILE_WIDTH),0.7*TILE_WIDTH+1,0.4*TILE_HEIGHT))
            # bottom right
            elif board[row][col] == 8:
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT-1,0.4*TILE_WIDTH,0.7*TILE_HEIGHT))
                pygame.draw.rect(screen,wall_colour,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT + (0.3 * TILE_WIDTH),0.7*TILE_WIDTH,0.4*TILE_HEIGHT))

def main():
    screen = pygame.display.set_mode((WIDTH,HEIGHT + BOTTOM_BAR_HEIGHT))
    player = Player()
    powerup_blink_interval = 0.1
    powerup_blink_timer = powerup_blink_interval
    show_powerup = True
    score_font_obj = pygame.font.SysFont("Consolas",18,bold=False)
    font_obj = pygame.font.SysFont("Consolas",36,bold=True)
    game_is_running = True
    time_delta = 0
    ## TO BE DONE BY STUDENTS ##
    while game_is_running:
        
        # Handle inputs
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        # Moving pieces
        player.move()
        player.actions(board)
        
        # Render background
        screen.fill(BLACK)

        # Render board
        draw_board(screen, show_powerup)
        if powerup_blink_timer > 0:
            powerup_blink_timer -= time_delta
        else:
            show_powerup = not show_powerup
            powerup_blink_timer = powerup_blink_interval
        
        # Render player and ghosts
        player.draw(screen)
        
        # Draw place for score and other content
        pygame.draw.rect(screen,RED,pygame.Rect(0,HEIGHT,WIDTH,BOTTOM_BAR_HEIGHT))
        text = score_font_obj.render(f"score:{player.score}", True, 'white')
        screen.blit(text, pygame.Rect(20,HEIGHT,WIDTH*0.4,BOTTOM_BAR_HEIGHT))
        pygame.display.update()
        time_delta = CLOCK.tick(60)
        time_delta = time_delta / 1000

    ## END OF STUDENT CODE ##
main()