import pygame
import math

# Initialize Pygame
pygame.init()

# Función para medir distancia entre dos puntos
def distance(p1, p2):
    return math.hypot(p2[0] - p1[0], p2[1] - p1[1])

# Verifica si el centro de un rectángulo está dentro del FOV circular
def is_in_fov_circle(player_pos, rect, radius):
    return distance(player_pos, rect.center) <= radius

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Colors
BLACK = (0, 0, 0)
GRAY = (100, 100, 100)
RED = (255, 0, 0)

# Player setup
player_pos = [0, 0]
FOV_RADIUS = 150

# Obstacles
obstacles = [
    pygame.Rect(200, 200, 100, 100),
    pygame.Rect(500, 400, 150, 50)
]

# Game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]: player_pos[1] -= 5
    if keys[pygame.K_s]: player_pos[1] += 5
    if keys[pygame.K_a]: player_pos[0] -= 5
    if keys[pygame.K_d]: player_pos[0] += 5

    # Drawing
    screen.fill(BLACK)

    # Dibujar obstáculos visibles dentro del FOV, Y en nuestro caso ABSOLUTAMENTE TODO
    for obstacle in obstacles:
        if is_in_fov_circle(player_pos, obstacle, FOV_RADIUS):
            pygame.draw.rect(screen, RED, obstacle)

    # Dibujar máscara negra con agujero circular
    dark_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    dark_surface.fill((0, 0, 0, 220))
    pygame.draw.circle(dark_surface, (255, 255, 255, 180), player_pos, FOV_RADIUS)
    screen.blit(dark_surface, (0, 0))

    # Dibujar jugador
    pygame.draw.circle(screen, RED, player_pos, 10)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()

