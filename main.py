pip install pygame
import pygame
import sys

# 1. Setup and Constants
pygame.init()
WIDTH, HEIGHT = 640, 480
TILE_SIZE = 32
FPS = 60

# Colors
GREEN = (50, 168, 82)
BLUE = (50, 50, 200)
DARK_GREEN = (30, 100, 30)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tiny Zelda Style Game")
clock = pygame.time.Clock()

# 2. Map Layout (T = Tree/Obstacle, P = Player Start)
MAP = [
    "TTTTTTTTTTTTTTTTTTTT",
    "T                  T",
    "T    TTTTTTT       T",
    "T    T     T       T",
    "T    T     T       T",
    "T    TTTTTTT       T",
    "T                  T",
    "T       P          T",
    "T                  T",
    "TTTTTTTTTTTTTTTTTTTT",
]

# 3. Game Objects
class Player:
    def __init__(self):
        self.x, self.y = 0, 0
        self.find_start_pos()
        self.rect = pygame.Rect(self.x * TILE_SIZE, self.y * TILE_SIZE, TILE_SIZE, TILE_SIZE)

    def find_start_pos(self):
        for row_idx, row in enumerate(MAP):
            if 'P' in row:
                self.y = row_idx
                self.x = row.index('P')

    def move(self, dx, dy):
        new_x = self.x + dx
        new_y = self.y + dy
        # Collision Check: Only move if not hitting 'T'
        if MAP[new_y][new_x] != 'T':
            self.x = new_x
            self.y = new_y
        self.rect.x = self.x * TILE_SIZE
        self.rect.y = self.y * TILE_SIZE

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

# Initialize Player
player = Player()

# 4. Main Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP: player.move(0, -1)
            elif event.key == pygame.K_DOWN: player.move(0, 1)
            elif event.key == pygame.K_LEFT: player.move(-1, 0)
            elif event.key == pygame.K_RIGHT: player.move(1, 0)

    # Drawing
    screen.fill(GREEN)
    for row_idx, row in enumerate(MAP):
        for col_idx, tile in enumerate(row):
            if tile == 'T':
                rect = pygame.Rect(col_idx * TILE_SIZE, row_idx * TILE_SIZE, TILE_SIZE, TILE_SIZE)
                pygame.draw.rect(screen, DARK_GREEN, rect)
    
    player.draw()
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
sys.exit()
