import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up screen
WIDTH, HEIGHT = 1920, 1020
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("My First Pygame")

# Set up clock for FPS
clock = pygame.time.Clock()

# Player setup
player_size = 250
player_pos = [WIDTH // 2 - player_size // 2, HEIGHT - player_size - 20]
player_speed = 10
player_img = pygame.image.load("./img/rocket.png").convert_alpha()
player_img = pygame.transform.scale(player_img, (player_size, player_size))

# Projectile setup
projectile_size = 50
projectile_speed = 10
projectile_img = pygame.image.load("./img/projectile.png").convert_alpha()
projectile_img = pygame.transform.scale(projectile_img, (projectile_size, projectile_size))
projectiles = []
can_shoot = True  # Only allow shooting once per spacebar press

# Background setup
background_img = pygame.image.load("./img/background.jpg").convert()
background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

# Game loop
running = True
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.w, event.h
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            background_img = pygame.transform.scale(background_img, (WIDTH, HEIGHT))

        elif event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
            can_shoot = True

    keys = pygame.key.get_pressed()
    new_pos = player_pos[:]

    # Movement (prevent going off-screen)
    if keys[pygame.K_a] and player_pos[0] > 0:
        new_pos[0] -= player_speed
    if keys[pygame.K_d] and player_pos[0] < WIDTH - player_size:
        new_pos[0] += player_speed
    if keys[pygame.K_w] and player_pos[1] > 0:
        new_pos[1] -= player_speed
    if keys[pygame.K_s] and player_pos[1] < HEIGHT - player_size:
        new_pos[1] += player_speed

    player_pos = new_pos

    # Shooting logic (only once per key press)
    if keys[pygame.K_SPACE] and can_shoot:
        bullet_x = player_pos[0] + player_size // 2 - projectile_size // 2
        bullet_y = player_pos[1]
        projectiles.append([bullet_x, bullet_y])
        can_shoot = False

    # Move projectiles
    projectiles = [ [p[0], p[1] - projectile_speed] for p in projectiles if p[1] > -projectile_size ]

    # Draw everything
    screen.blit(background_img, (0, 0))                            # Background
    screen.blit(player_img, player_pos)                            # Player
    for p in projectiles:
        screen.blit(projectile_img, p)                             # Bullets
    pygame.display.flip()

# Quit
pygame.quit()
sys.exit()
