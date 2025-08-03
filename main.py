import pygame
import sys
import random

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
BROWN = (150, 75, 0)

# Player setup
player_pos = [750, 550]
player_size = 50
player_speed = 5

# Projectile setup
projectiles = []
projectile_speed = 10
projectile_size = 10
can_shoot = True  # For single press shooting

# Structure (platform) setup
structure_width = 200
structure_height = 30
structure_x = (WIDTH - structure_width) // 2
structure_y = (HEIGHT - structure_height) // 2
structure_rect = pygame.Rect(structure_x, structure_y, structure_width, structure_height)

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

            # Recalculate structure position after resizing
            structure_x = (WIDTH - structure_width) // 2
            structure_y = (HEIGHT - structure_height) // 2
            structure_rect = pygame.Rect(structure_x, structure_y, structure_width, structure_height)

        # Detect key up for spacebar to reset shooting
        if event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            can_shoot = True

    # Create player rect
    player_rect = pygame.Rect(player_pos[0], player_pos[1], player_size, player_size)

    # Movement + Collision
    keys = pygame.key.get_pressed()
    new_pos = player_pos[:]

    if keys[pygame.K_a] and player_pos[0] > 0:
        new_pos[0] -= player_speed
    if keys[pygame.K_d] and player_pos[0] < WIDTH - player_size:
        new_pos[0] += player_speed
    if keys[pygame.K_w] and player_pos[1] > 0:
        new_pos[1] -= player_speed
    if keys[pygame.K_s] and player_pos[1] < HEIGHT - player_size:
        new_pos[1] += player_speed

    new_rect = pygame.Rect(*new_pos, player_size, player_size)
    if not new_rect.colliderect(structure_rect):
        player_pos = new_pos

    # Shoot only once per key press
    if keys[pygame.K_SPACE] and can_shoot:
        bullet_x = player_pos[0] + player_size // 2 - projectile_size // 2
        bullet_y = player_pos[1]
        projectiles.append([bullet_x, bullet_y])
        can_shoot = False

    # Update projectile positions and remove on collision with structure
    updated_projectiles = []
    for p in projectiles:
        p[1] -= projectile_speed
        projectile_rect = pygame.Rect(*p, projectile_size, projectile_size)

        if not projectile_rect.colliderect(structure_rect) and p[1] > -projectile_size:
            updated_projectiles.append(p)

    projectiles = updated_projectiles

    # Clear screen
    screen.fill(BLACK)

    # Draw structure
    pygame.draw.rect(screen, BROWN, structure_rect)

    # Draw player
    pygame.draw.rect(screen, WHITE, (*player_pos, player_size, player_size))

    # Draw bullets
    for p in projectiles:
        pygame.draw.rect(screen, RED, (*p, projectile_size, projectile_size))

    # Update display
    pygame.display.flip()

# Quit Pygame
pygame.quit()
sys.exit()
