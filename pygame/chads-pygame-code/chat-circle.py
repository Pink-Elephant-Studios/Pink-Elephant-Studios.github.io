import pygame
import sys
import random
import math

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
PLAYER_RADIUS = 20
FOOD_RADIUS = 10
ENEMY_RADIUS = 30
PLAYER_SPEED = 5
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Circle Eater")

# Initialize player position
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2

# Create initial food and enemy circles
food_circles = [(random.randint(FOOD_RADIUS, SCREEN_WIDTH - FOOD_RADIUS),
                 random.randint(FOOD_RADIUS, SCREEN_HEIGHT - FOOD_RADIUS))
                for _ in range(10)]

enemy_circles = [(random.randint(ENEMY_RADIUS, SCREEN_WIDTH - ENEMY_RADIUS),
                  random.randint(ENEMY_RADIUS, SCREEN_HEIGHT - ENEMY_RADIUS))
                 for _ in range(5)]

def draw_circles():
    screen.fill(WHITE)
    pygame.draw.circle(screen, GREEN, (player_x, player_y), PLAYER_RADIUS)
    for food in food_circles:
        pygame.draw.circle(screen, RED, food, FOOD_RADIUS)
    for enemy in enemy_circles:
        pygame.draw.circle(screen, BLUE, enemy, ENEMY_RADIUS)

def main():
    global player_x, player_y  # Declare player_x and player_y as global variables
    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            player_x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            player_x += PLAYER_SPEED
        if keys[pygame.K_UP]:
            player_y -= PLAYER_SPEED
        if keys[pygame.K_DOWN]:
            player_y += PLAYER_SPEED

        # Check for collisions
        for food in food_circles[:]:
            distance = math.hypot(food[0] - player_x, food[1] - player_y)
            if distance < PLAYER_RADIUS + FOOD_RADIUS:
                food_circles.remove(food)
                food_circles.append((random.randint(FOOD_RADIUS, SCREEN_WIDTH - FOOD_RADIUS),
                                     random.randint(FOOD_RADIUS, SCREEN_HEIGHT - FOOD_RADIUS)))

        for enemy in enemy_circles:
            distance = math.hypot(enemy[0] - player_x, enemy[1] - player_y)
            if distance < PLAYER_RADIUS + ENEMY_RADIUS:
                pygame.quit()
                sys.exit()

        draw_circles()
        pygame.display.update()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
