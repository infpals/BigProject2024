# Author: Ethan Cheam Kai Jun
# Email: ethan.cheam123@gmail.com
import random
import os
import pygame
from pygame.locals import K_a, K_d, K_w, K_s, QUIT, K_SPACE
pygame.init()

# Maze is 630 pixels wide, 726 pixels tall. 50 pixel tall bar at bottom to display score and debug information.
WIDTH = 630
HEIGHT = 726
BOTTOM_BAR_HEIGHT = 50
# Maze is 30 tiles wide and 33 tiles high.
TILES_WIDE = 30
TILES_HIGH = 33
# Each tile is 21 pixels wide and tall
TILE_WIDTH = WIDTH // TILES_WIDE
TILE_HEIGHT = HEIGHT // TILES_HIGH
# RGB Codes for colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
CLOCK = pygame.time.Clock()
# Number of normal and power pellets
NUM_PELLETS = 246
PLAYER_SPEED = 5
SPRITE_WIDTH = 30
SPRITE_HEIGHT = 30
# 0 = empty black rectangle, 1 = dot, 2 = big dot, 3 = vertical line,
# 4 = horizontal line, 5 = top right, 6 = top left, 7 = bottom left, 8 = bottom right
# 9 = ghost house gate
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
        # Loading pacman sprite and creating rect
        path_to_image = os.path.join(os.path.dirname(
            __file__), "sprites", "pacman", "pacman.png")
        image = pygame.image.load(path_to_image).convert()
        self.img = pygame.transform.scale(
            image, size=(SPRITE_WIDTH, SPRITE_HEIGHT))
        self.rect = pygame.Rect(0, 0, SPRITE_WIDTH, SPRITE_HEIGHT)

        # Start position
        self.rect.centerx = 15 * TILE_WIDTH
        self.rect.centery = (24 * TILE_HEIGHT) + 10
        self.speed = PLAYER_SPEED
        # direction = 0,1,2,3 corresponds to Left, Right, Up, Down
        self.direction = 1
        self.pellets_eaten = 0
        self.score = 0
        self.powered_up = False
        self.power_up_length = 7  # seconds
        self.power_up_timer = 0
        self.ghost_list = None

        self.alive = True

    def move(self):
        """Get input from user, react to walls of the maze and move the rect"""
        wall = wall_check(self.rect.centerx, self.rect.centery,
                          look_ahead=15, can_enter_gate=False)
        # When currently colliding with a wall, move the player so that they do not phase into the wall and are properly aligned with junctions.
        if wall[self.direction]:
            this_tile_x, this_tile_y = to_tile(
                self.rect.centerx, self.rect.centery)
            self.rect.centerx = this_tile_x * TILE_WIDTH + (TILE_WIDTH // 2)
            self.rect.centery = this_tile_y * TILE_HEIGHT + (TILE_HEIGHT // 2)
        # Booleans recording is pacman is moving along Left-Right (horizontal) or Up-Down (vertical)
        horizontal = (self.direction == 0) or (self.direction == 1)
        vertical = (self.direction == 2) or (self.direction == 3)

        # Processing inputs and checking if allowed to move in desired direction.
        keys = pygame.key.get_pressed()
        lower_bound = 7
        upper_bound = 13
        # Currently going left or right
        if horizontal:
            # Attempting to turn left or right
            if keys[K_a] and (not wall[0]):
                self.direction = 0
            if keys[K_d] and (not wall[1]):
                self.direction = 1
            # Attempting to turn up or down at a junction
            # Imagine a tile has index 0..20. You must be within 3 pixels of the center 10.5 to turn at a junction
            if lower_bound <= (self.rect.centerx % TILE_WIDTH) <= upper_bound:
                if keys[K_w] and not wall[2]:
                    self.direction = 2
                if keys[K_s] and not wall[3]:
                    self.direction = 3
        # Currently going up or down
        if vertical:
            # Attempting to turn left or right at a junction
            if lower_bound <= self.rect.centery % TILE_HEIGHT <= upper_bound:
                if keys[K_a] and (not wall[0]):
                    self.direction = 0
                if keys[K_d] and (not wall[1]):
                    self.direction = 1
            # Attempting to turn up or down
            if keys[K_w] and not wall[2]:
                self.direction = 2
            if keys[K_s] and not wall[3]:
                self.direction = 3

        # Move sprite based on direction
        if self.direction == 0 and not wall[0]:
            self.rect.centerx -= self.speed
        if self.direction == 1 and not wall[1]:
            self.rect.centerx += self.speed
        if self.direction == 2 and not wall[2]:
            self.rect.centery -= self.speed
        if self.direction == 3 and not wall[3]:
            self.rect.centery += self.speed

        # Looping around the edge of the board through the portal
        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.left > WIDTH:
            self.rect.right = 0

    def draw(self, screen: pygame.Surface):
        """Draws player sprite onto the current rect of the player"""
        screen.blit(self.img, self.rect)

    def actions(self, time_delta):
        """Eat pellets and power pellets and handle powered up timer"""
        tile_x, tile_y = to_tile(self.rect.centerx, self.rect.centery)
        if 0 <= (tile_x) <= (TILES_WIDE - 1):
            if board[tile_y][tile_x] == 1:
                self.score += 10
                board[tile_y][tile_x] = 0
                self.pellets_eaten += 1
            elif board[tile_y][tile_x] == 2:
                self.score += 50
                board[tile_y][tile_x] = 0
                self.powered_up = True
                self.power_up_timer = self.power_up_length
                self.pellets_eaten += 1

                for ghost in self.ghost_list:
                    ghost.frighten()

        # Reducing the timer.
        if self.powered_up:
            if self.power_up_timer > 0:
                self.power_up_timer -= time_delta
            else:
                # Powerup has ended
                self.powered_up = False
                for ghost in self.ghost_list:
                    ghost.unfrighten()

    def die(self):
        self.alive = False

    def eat_ghost(self):
        self.score += 200


class Ghost:
    def __init__(self):
        # Loading sprites
        folder_path = os.path.join(
            os.path.dirname(__file__), "sprites", "blinky")
        # images contains sprites for looking up/down/left/right, frightened and dead
        self.images = []
        for i in range(10):
            self.images.append(pygame.image.load(
                os.path.join(folder_path, f"ghost{i}.png")).convert())
            self.images[i] = pygame.transform.scale(
                self.images[i], (SPRITE_WIDTH, SPRITE_HEIGHT))

        # Rect
        self.rect = pygame.Rect(0, 0, SPRITE_WIDTH, SPRITE_HEIGHT)
        self.speed = 2
        # direction = 0,1,2,3 corresponds to Left, Right, Up, Down
        self.direction = 1
        self.target_direction = 1

        # Key tiles
        self.previous_tile = (12, 15)
        self.house_tile = (13, 15)
        self.leave_house_tile = (14, 12)
        self.target_tile = self.leave_house_tile

        # Spawn in the house
        self.rect.centerx = TILE_WIDTH * self.house_tile[0]
        self.rect.centery = TILE_HEIGHT * self.house_tile[1]
        self.mode = "in_house"

        self.stay_in_house_length = 3
        self.house_timer = self.stay_in_house_length

    def get_valid_directions(self, this_tile_x, this_tile_y):
        """Returns list of tuples (tile_x,tile_y) for valid tiles and direction (0,1,2,3) leading to each valid tile"""
        if 0 < this_tile_x < (TILES_WIDE - 1):
            # We only check when not in portal
            # look_directions are 0, 1, 2, 3
            look_directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]
            valid_directions = []
            tile_list = []
            # Check which tiles around me are not walls or the previous tile. Consider ghost house gate a valid tile.
            for i in range(4):
                stepx = this_tile_x + look_directions[i][0]
                stepy = this_tile_y + look_directions[i][1]
                if not (2 < board[stepy][stepx] < 9):
                    if (stepx, stepy) != self.previous_tile:
                        valid_directions.append(i)
                        tile_list.append((stepx, stepy))
            return tile_list, valid_directions
        return [], []

    def set_frightened_direction(self, this_tile_x, this_tile_y):
        """Ghosts move to a random valid direction at junctions when frightened"""
        _, valid_directions = self.get_valid_directions(
            this_tile_x, this_tile_y)
        # We don't change direction when going though the portal
        if valid_directions != []:
            self.target_direction = random.choice(valid_directions)

    def in_house(self, x, y):
        tile_x, tile_y = to_tile(x, y)
        return 12 <= tile_x <= 17 and 14 <= tile_y <= 16

    def go_target_tile(self, this_tile_x, this_tile_y):
        """Get direction that leads ghost to tile that is closest to target_tile"""
        tile_options, valid_directions = self.get_valid_directions(
            this_tile_x, this_tile_y)
        best_distance = float('inf')
        for i in range(len(valid_directions)):
            # Euclidean distance but without square root for computational efficiency
            distance = (self.target_tile[0] - tile_options[i][0]
                        )**2 + (self.target_tile[1] - tile_options[i][1])**2
            if distance < best_distance:
                self.target_direction = valid_directions[i]
                best_distance = distance

    def move(self):
        """Move rect based on target_direction and interact with maze walls"""
        if self.mode == "dead" or self.mode == "leave_house":
            wall = wall_check(self.rect.centerx,
                              self.rect.centery, look_ahead=15, can_enter_gate=True)
        else:
            wall = wall_check(self.rect.centerx,
                              self.rect.centery, look_ahead=15, can_enter_gate=False)

        # When currently colliding with a wall (necessary to prevent Ghost getting stuck inside a wall)
        if wall[self.direction]:
            self.rect.centerx = (self.rect.centerx //
                                 TILE_WIDTH) * TILE_WIDTH + (TILE_WIDTH // 2)
            self.rect.centery = (
                self.rect.centery // TILE_HEIGHT) * TILE_HEIGHT + (TILE_HEIGHT // 2)

        horizontal = (self.direction == 0) or (self.direction == 1)
        vertical = (self.direction == 2) or (self.direction == 3)

        # Processing inputs and checking if allowed to move in desired direction.
        lower = 7
        upper = 13
        if horizontal:
            # Attempting to turn left or right while currently going left or right
            if self.target_direction == 0 and (not wall[0]):
                self.direction = 0
            if self.target_direction == 1 and (not wall[1]):
                self.direction = 1
            # Attempting to turn up or down at a junction
            # Imagine a tile has index 0..20. You must be within 3 pixels of the center 10.5 to turn at a junction
            if lower <= self.rect.centerx % TILE_WIDTH <= upper:
                if self.target_direction == 2 and not wall[2]:
                    self.direction = 2
                if self.target_direction == 3 and not wall[3]:
                    self.direction = 3
        if vertical:
            # Attempting to turn left or right at a junction
            if lower <= self.rect.centery % TILE_HEIGHT <= upper:
                if self.target_direction == 0 and (not wall[0]):
                    self.direction = 0
                if self.target_direction == 1 and (not wall[1]):
                    self.direction = 1
            # Attempting to turn up or down while currently going up or down
            if self.target_direction == 2 and not wall[2]:
                self.direction = 2
            if self.target_direction == 3 and not wall[3]:
                self.direction = 3

        # Process direction for Left, Right, Up and Down
        if self.direction == 0 and not wall[0]:
            self.rect.centerx -= self.speed
        if self.direction == 1 and not wall[1]:
            self.rect.centerx += self.speed
        if self.direction == 2 and not wall[2]:
            self.rect.centery -= self.speed
        if self.direction == 3 and not wall[3]:
            self.rect.centery += self.speed

        if self.rect.right < 0:
            self.rect.left = WIDTH
        if self.rect.left > WIDTH:
            self.rect.right = 0

    def reverse_direction(self):
        reverse = [1, 0, 3, 2]
        self.direction = reverse[self.direction]

    def frighten(self):
        """This method is called once when pacman eats a power pellet"""
        if self.mode != "dead":
            self.mode = "frightened"
            # Traditionally, the ghost reverses direction upon entering frightened mode
            self.reverse_direction()

    def unfrighten(self):
        """This method is called once when pacman ends his powered up state"""
        if self.mode == "frightened" and not self.in_house(self.rect.centerx, self.rect.centery):
            self.mode = "chase"
        elif self.mode == "in_house":
            self.mode = "leave_house"
            self.target_tile = self.leave_house_tile

    def update(self, player: Player, time_delta):
        """Select target_tile based on mode and players position and handle timers, collisions and movement"""
        pacman_x, pacman_y = player.rect.centerx, player.rect.centery
        pacman_tile_x, pacman_tile_y = to_tile(pacman_x, pacman_y)
        this_tile_x, this_tile_y = to_tile(
            self.rect.centerx, self.rect.centery)
        # Ghost traditionally only decides where to go when stepping into new tile
        if (this_tile_x, this_tile_y) != self.previous_tile:
            if self.mode == "chase":
                self.target_tile = (pacman_tile_x, pacman_tile_y)

            elif self.mode == "frightened":
                self.set_frightened_direction(this_tile_x, this_tile_y)

            elif self.mode == "dead":
                if (this_tile_x, this_tile_y) == self.target_tile:
                    self.mode = "in_house"
                    self.house_timer = self.stay_in_house_length

            elif self.mode == "in_house":
                if self.house_timer <= 0:
                    self.mode = "leave_house"
                    self.target_tile = self.leave_house_tile

            elif self.mode == "leave_house":
                if (this_tile_x, this_tile_y) == self.leave_house_tile:
                    self.mode = "chase"

            if self.mode != "frightened":
                self.go_target_tile(this_tile_x, this_tile_y)
            self.previous_tile = (this_tile_x, this_tile_y)

        # Timers
        if self.house_timer > 0:
            self.house_timer -= time_delta
        # Collisions
        if (this_tile_x == pacman_tile_x) and (this_tile_y == pacman_tile_y):
            self.process_collision(player)
        self.move()

    def process_collision(self, player: Player):
        # Ghost has no interaction with player when dead
        if self.mode != "dead":
            if player.powered_up:
                self.mode = "dead"
                self.target_tile = self.house_tile
                player.eat_ghost()
            else:
                player.die()

    def draw(self, window: pygame.Surface):
        if self.mode == "frightened":
            window.blit(self.images[4], self.rect)
        elif self.mode == "dead":
            window.blit(self.images[self.direction+6], self.rect)
        else:
            window.blit(self.images[self.direction], self.rect)
        target_debug = pygame.rect.Rect(
            self.target_tile[0] * TILE_WIDTH, self.target_tile[1] * TILE_HEIGHT, 21, 21)
        pygame.draw.rect(window, 'red', target_debug)        


def to_tile(x, y):
    """Converts pixel position of center of game object to tile position"""
    return x // TILE_WIDTH, y // TILE_HEIGHT


def draw_board(screen: pygame.Surface, show_powerup):
    """Draws the board"""
    wall_colour = WHITE
    food_colour = WHITE
    for row in range(TILES_HIGH):
        for col in range(TILES_WIDE):
            if board[row][col] == 1:
                radius = 2
                pygame.draw.circle(screen, food_colour, (col*TILE_WIDTH +
                                   TILE_WIDTH/2, row*TILE_HEIGHT+TILE_HEIGHT/2), radius)
            # big dot
            elif board[row][col] == 2 and show_powerup:
                radius = 8
                pygame.draw.circle(screen, food_colour, (col*TILE_WIDTH +
                                   TILE_WIDTH/2, row*TILE_HEIGHT+TILE_HEIGHT/2), radius)
            # vertical line
            elif board[row][col] == 3:
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT, 0.4 * TILE_WIDTH, TILE_HEIGHT))
            # horizontal line
            elif board[row][col] == 4:
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT + (0.3 * TILE_HEIGHT), TILE_WIDTH, 0.4 * TILE_HEIGHT))
            # top right
            elif board[row][col] == 5:
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT + (0.3 * TILE_WIDTH), 0.4*TILE_WIDTH, 0.7*TILE_HEIGHT+1))
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT + (0.3 * TILE_WIDTH), 0.7*TILE_WIDTH, 0.4*TILE_HEIGHT))
            # top left
            elif board[row][col] == 6:
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT + (0.3 * TILE_WIDTH), 0.4*TILE_WIDTH, 0.7*TILE_HEIGHT+1))
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT + (0.3 * TILE_WIDTH), 0.7*TILE_WIDTH+1, 0.4*TILE_HEIGHT))
            # bottom left
            elif board[row][col] == 7:
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT-1, 0.4*TILE_WIDTH, 0.7*TILE_HEIGHT))
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT + (0.3 * TILE_WIDTH), 0.7*TILE_WIDTH+1, 0.4*TILE_HEIGHT))
            # bottom right
            elif board[row][col] == 8:
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH + (0.3 * TILE_WIDTH), row*TILE_HEIGHT-1, 0.4*TILE_WIDTH, 0.7*TILE_HEIGHT))
                pygame.draw.rect(screen, wall_colour,
                                 pygame.Rect(col*TILE_WIDTH, row*TILE_HEIGHT + (0.3 * TILE_WIDTH), 0.7*TILE_WIDTH, 0.4*TILE_HEIGHT))


def wall_check(x, y, look_ahead, can_enter_gate):
    """Returns 4 booleans indicating if there is a wall Left, Right, Up and Down"""
    this_tile_x, this_tile_y = to_tile(x, y)

    if 0 < (this_tile_x) < (TILES_WIDE - 1):
        walls = [False, False, False, False]
        left_tile_x, _ = to_tile(x - look_ahead, y)
        right_tile_x, _ = to_tile(x + look_ahead, y)
        _, up_tile_y = to_tile(x, y - look_ahead)
        _, down_tile_y = to_tile(x, y + look_ahead)
        if can_enter_gate:
            if 2 < board[this_tile_y][left_tile_x] < 9:
                walls[0] = True
            if 2 < board[this_tile_y][right_tile_x] < 9:
                walls[1] = True
            if 2 < board[up_tile_y][this_tile_x] < 9:
                walls[2] = True
            if 2 < board[down_tile_y][this_tile_x] < 9:
                walls[3] = True
        else:
            if board[this_tile_y][left_tile_x] > 2:
                walls[0] = True
            if board[this_tile_y][right_tile_x] > 2:
                walls[1] = True
            if board[up_tile_y][this_tile_x] > 2:
                walls[2] = True
            if board[down_tile_y][this_tile_x] > 2:
                walls[3] = True
    else:
        walls = [False, False, True, True]
    return walls


def gameover_screen(screen:pygame.Surface, win, font_obj:pygame.font.SysFont, small_font_obj:pygame.font.SysFont, player_score):
    # Printing YOU WON or YOU LOST
    if win:
        gameover_text = font_obj.render(f"YOU WON", True, 'white', 'blue')
    else:
        gameover_text = font_obj.render(f"YOU LOST", True, 'white', 'blue')
    message_pos = pygame.Rect(0, 0, gameover_text.get_width(),
                              gameover_text.get_height())
    message_pos.center = (WIDTH/2, HEIGHT / 2)

    # Printing score just below the WIN/LOSS Message
    score_pos = message_pos.copy()
    score_pos.centery += gameover_text.get_height()
    score_text = font_obj.render(f"score {player_score}", True, 'white', 'red')

    press_text = small_font_obj.render(
        f"Press space to return to menu", True, 'white', 'blue')
    press_text_position = score_pos.copy()
    press_text_position.centery += score_text.get_height()
    screen.blit(gameover_text, message_pos)
    screen.blit(score_text, score_pos)
    screen.blit(press_text,press_text_position)
    pygame.display.update()

    # Keep showing message until player presses space.
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN and event.key == K_SPACE:
                return
        CLOCK.tick(60)


def menu(screen: pygame.Surface, big_font_obj:pygame.font.SysFont, small_font_obj):
    
    screen.fill(BLACK)
    pacman_text = big_font_obj.render(f"PACMAN", True, 'yellow', 'blue')
    pacman_text_position = pygame.Rect(0, 0, pacman_text.get_width(),
                                       pacman_text.get_height())
    pacman_text_position.center = (WIDTH/2, HEIGHT / 2)
    screen.blit(pacman_text, pacman_text_position)

    press_text = small_font_obj.render(
        f"Press any key to start", True, 'white', 'red')
    press_text_position = pygame.Rect(
        0, 0, press_text.get_width(), press_text.get_height())
    press_text_position.center = (WIDTH/2, HEIGHT/2 + pacman_text.get_height())
    screen.blit(press_text, press_text_position)
    pygame.display.update()
    # Game starts when player presses any key
    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                return
        CLOCK.tick(60)


def main():
    screen = pygame.display.set_mode((WIDTH, HEIGHT + BOTTOM_BAR_HEIGHT))
    pygame.font
    # Set up fonts
    small_font_obj = pygame.font.SysFont("Consolas", 18, bold=False)
    big_font_obj = pygame.font.SysFont("Consolas", 36, bold=True)
    while True:
        # Setting up the game
        # Set up player and ghosts
        player = Player()
        blinky = Ghost()
        ghost_list = [blinky]
        player.ghost_list = ghost_list
        # Set up timers
        powerup_blink_interval = 0.1
        powerup_blink_timer = powerup_blink_interval
        show_powerup = True
        time_delta = 0

        menu(screen, big_font_obj, small_font_obj)
        # Game loop
        win = False
        game_is_running = True
        while game_is_running:
            # Handle inputs
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()

            # Moving pieces
            player.move()
            player.actions(time_delta)
            for ghost in ghost_list:
                ghost.update(player, time_delta=time_delta)

            # Win and loose condition
            if not player.alive:
                game_is_running = False
            # Check if ate all power pellets
            elif player.pellets_eaten == NUM_PELLETS:
                win = True
                game_is_running = False

            # Rendering
            # Render background
            screen.fill(BLACK)

            # Render board
            draw_board(screen, show_powerup)

            # Blinking power pellets
            if powerup_blink_timer > 0:
                powerup_blink_timer -= time_delta
            else:
                show_powerup = not show_powerup
                powerup_blink_timer = powerup_blink_interval

            # Render player and ghosts
            player.draw(screen)
            for ghost in ghost_list:
                ghost.draw(screen)

            # Draw place for score and other content
            # Draw score bar
            pygame.draw.rect(screen, RED, pygame.Rect(
                0, HEIGHT, WIDTH, BOTTOM_BAR_HEIGHT))
            score_text = small_font_obj.render(
                f"score:{player.score}", True, 'white')
            screen.blit(score_text, pygame.Rect(
                20, HEIGHT, WIDTH*0.4, BOTTOM_BAR_HEIGHT))

            # Debugging information for ghosts
            a = ghost.target_direction
            text = small_font_obj.render(f"target_dir:{a}", True, 'white')
            screen.blit(text, pygame.Rect(
                20, HEIGHT+20, WIDTH*0.4, BOTTOM_BAR_HEIGHT))
            b = ghost.direction
            text = small_font_obj.render(f"dir:{b}", True, 'white')
            screen.blit(text, pygame.Rect(150, HEIGHT +
                        20, WIDTH*0.4, BOTTOM_BAR_HEIGHT))
            x, y = ghost.target_tile
            text = small_font_obj.render(f"tile:{(x,y)}", True, 'white')
            screen.blit(text, pygame.Rect(220, HEIGHT +
                        20, WIDTH*0.4, BOTTOM_BAR_HEIGHT))
            mode = ghost.mode
            p = player.powered_up
            text = small_font_obj.render(
                f"mode:{mode} power up:{p}", True, 'white')
            screen.blit(text, pygame.Rect(350, HEIGHT +
                        20, WIDTH*0.4, BOTTOM_BAR_HEIGHT))

            # Update the display
            pygame.display.update()
            time_delta = CLOCK.tick(60)
            time_delta = time_delta / 1000

        gameover_screen(screen, win, big_font_obj, small_font_obj, player.score)


if __name__ == "__main__":
    main()
