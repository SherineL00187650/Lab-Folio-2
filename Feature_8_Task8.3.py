import pygame
import sys

# Initialize pygame
pygame.init()

# Set up display
screen_width, screen_height = 800, 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Camp Creation Mechanic")

# Colors
WHITE = (255, 255, 255)
GREEN = (34, 139, 34)
BROWN = (139, 69, 19)
BLUE = (0, 0, 255)
TENT_COLOR = (184, 134, 11)  # Brownish yellow for tents

# Game variables
camp_score = 0
tents_placed = []

# Camp class for managing tent placements
class Camp:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 50
        self.height = 30

    def draw(self):
        pygame.draw.rect(screen, TENT_COLOR, (self.x, self.y, self.width, self.height))

# UI class for handling camp creation
class CampCreationUI:
    def __init__(self):
        self.camp_location = None
        self.is_placing_camp = False

    def start_placing_camp(self):
        self.is_placing_camp = True

    def place_camp(self, x, y):
        if self.is_placing_camp:
            new_camp = Camp(x - 25, y - 15)  # Center the tent on the mouse click
            tents_placed.append(new_camp)
            global camp_score
            camp_score += 10  # Player earns 10 points for placing a tent
            self.is_placing_camp = False  # Stop placing after one camp is created

    def draw_ui(self):
        font = pygame.font.SysFont(None, 30)
        score_text = font.render(f"Score: {camp_score}", True, BLUE)
        screen.blit(score_text, (10, 10))

# Initialize objects
camp_ui = CampCreationUI()

# Main game loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if camp_ui.is_placing_camp:
                camp_ui.place_camp(mouse_x, mouse_y)

        # Key press events to start the camp placement mode
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Press 'P' to start placing a camp
                camp_ui.start_placing_camp()

    # Draw the UI
    camp_ui.draw_ui()

    # Draw placed tents
    for tent in tents_placed:
        tent.draw()

    # Display message for the user
    if camp_ui.is_placing_camp:
        font = pygame.font.SysFont(None, 40)
        message = font.render("Click to place your camp!", True, BLUE)
        screen.blit(message, (screen_width // 3, screen_height // 2))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
