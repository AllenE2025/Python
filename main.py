import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My First Pygame")

# Set up clock for FPS
clock = pygame.time.Clock()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player setup
player_pos = [750, 550]
player_size = 50
player_speed = 5

projectiles = []
projectile_speed = 10
projectile_size = 10

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)

    # Handle key input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] and player_pos[0] > 0:
        player_pos[0] -= player_speed
    if keys[pygame.K_d] and player_pos[0] < WIDTH - player_size:
        player_pos[0] += player_speed
    if keys[pygame.K_w] and player_pos[1] > 0:
        player_pos[1] -= player_speed
    if keys[pygame.K_s] and player_pos[1] < HEIGHT - player_size:
        player_pos[1] += player_speed

    if keys[pygame.K_SPACE]:

        bullet_x = player_pos[0] + player_size // 2 - projectile_size // 2
        bullet_y = player_pos[1]
        projectiles.append([bullet_x, bullet_y])

    for p in projectiles:
        p[1] -= projectile_speed

    projectiles = [p for p in projectiles if p[1] > -projectile_size]

    # Clear screen
    screen.fill(BLACK)

    # Draw player
    pygame.draw.rect(screen, WHITE, (*player_pos, player_size, player_size))

    for p in projectiles:
        pygame.draw.rect(screen, RED, (*p, projectile_size, projectile_size))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
