import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 400, 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Create the game window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Catch the Falling Object")

# Player
player = pygame.Rect(WIDTH // 2 - 25, HEIGHT - 50, 50, 50)

# Objects
object_width = 30
object_height = 30
object_x = random.randint(0, WIDTH - object_width)
object_y = 0

# Game loop
clock = pygame.time.Clock()
score = 0

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move the player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= 5
    if keys[pygame.K_RIGHT]:
        player.x += 5

    # Move the falling object
    object_y += 5

    # Check if the player catches the object
    if player.colliderect(pygame.Rect(object_x, object_y, object_width, object_height)):
        object_x = random.randint(0, WIDTH - object_width)
        object_y = 0
        score += 1

    # Check if the object reaches the bottom
    if object_y > HEIGHT:
        object_x = random.randint(0, WIDTH - object_width)
        object_y = 0

    # Clear the screen
    screen.fill(WHITE)

    # Draw the player and the falling object
    pygame.draw.rect(screen, RED, player)
    pygame.draw.rect(screen, RED, (object_x, object_y, object_width, object_height))

    # Display the score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, RED)
    screen.blit(score_text, (10, 10))

    pygame.display.update()

    # Control game speed
    clock.tick(30)

# Quit the game
pygame.quit()
