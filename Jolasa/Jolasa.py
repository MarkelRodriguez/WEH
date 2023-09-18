import pygame
import random

# Inicializamos Pygame
pygame.init()

# Configuración de la pantalla
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Esquiva el Obstáculo")

# Colores
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Personaje
player_width, player_height = 50, 50
player_x, player_y = (WIDTH - player_width) // 2, HEIGHT - player_height
player_speed = 5

# Obstáculos
obstacle_width, obstacle_height = 50, 50
obstacle_x = random.randint(0, WIDTH - obstacle_width)
obstacle_y = -obstacle_height
obstacle_speed = 3

# Función para dibujar el personaje en la pantalla
def draw_player(x, y):
    pygame.draw.rect(screen, RED, (x, y, player_width, player_height))

# Función para dibujar un obstáculo en la pantalla
def draw_obstacle(x, y):
    pygame.draw.rect(screen, WHITE, (x, y, obstacle_width, obstacle_height))

# Bucle principal del juego
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Control del personaje
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
        player_x += player_speed

    # Mover el obstáculo
    obstacle_y += obstacle_speed

    # Si el obstáculo sale de la pantalla, generamos uno nuevo
    if obstacle_y > HEIGHT:
        obstacle_x = random.randint(0, WIDTH - obstacle_width)
        obstacle_y = -obstacle_height

    # Colisión con el obstáculo
    if player_x < obstacle_x + obstacle_width and player_x + player_width > obstacle_x \
            and player_y < obstacle_y + obstacle_height and player_y + player_height > obstacle_y:
        print("¡Perdiste!")
        running = False

    # Limpiar la pantalla
    screen.fill((0, 0, 0))

    # Dibujar el personaje y el obstáculo
    draw_player(player_x, player_y)
    draw_obstacle(obstacle_x, obstacle_y)

    # Actualizar la pantalla
    pygame.display.update()

# Salir de Pygame
pygame.quit()