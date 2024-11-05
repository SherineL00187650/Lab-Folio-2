import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Satori Mountain Camping Feature")

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Campfire class for creating campfire objects
class Campfire:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = 20
        self.is_active = False  # Campfire is initially inactive

    def draw(self):
        color = RED if self.is_active else BROWN
        pygame.draw.circle(screen, color, (self.x, self.y), self.radius)

    def activate(self):
        self.is_active = True

    def deactivate(self):
        self.is_active = False

# Tree class for creating tree objects in the environment
class Tree:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 50

    def draw(self):
        pygame.draw.rect(screen, GREEN, (self.x, self.y, self.width, self.height))

# Player class for controlling the player
class Player:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 30
        self.height = 30
        self.color = BLUE
        self.speed = 5

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def draw(self):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

# Initialize objects
player = Player(100, 100)
campfire = Campfire(400, 300)
trees = [Tree(200, 400), Tree(600, 500), Tree(300, 200)]
camp_spots = [(400, 300), (500, 350), (600, 250)]  # Placeholder for camping spots

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.move(-player.speed, 0)
    if keys[pygame.K_RIGHT]:
        player.move(player.speed, 0)
    if keys[pygame.K_UP]:
        player.move(0, -player.speed)
    if keys[pygame.K_DOWN]:
        player.move(0, player.speed)

    # Draw environment elements
    for tree in trees:
        tree.draw()
    
    campfire.draw()

    # Draw camping spots (interactive zones)
    for spot in camp_spots:
        pygame.draw.rect(screen, GREEN, (spot[0], spot[1], 50, 50), 2)  # Draw as a simple square

    player.draw()

    # Interactions (campfire activation)
    if (player.x + player.width // 2 > campfire.x - campfire.radius and
        player.x + player.width // 2 < campfire.x + campfire.radius and
        player.y + player.height // 2 > campfire.y - campfire.radius and
        player.y + player.height // 2 < campfire.y + campfire.radius):
        campfire.activate()

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
