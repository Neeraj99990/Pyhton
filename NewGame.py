import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Catch the Falling Objects")

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Player settings
player_width = 50
player_height = 50
player_x = screen_width // 2
player_y = screen_height - player_height - 10
player_speed = 7

# Object settings
object_width = 30
object_height = 30
object_speed = 5
object_x = random.randint(0, screen_width - object_width)
object_y = -object_height

# Score
score = 0
font = pygame.font.Font(None, 36)

# Clock
clock = pygame.time.Clock()
fps = 30

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Get key states
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < screen_width - player_width:
        player_x += player_speed

    # Move the falling object
    object_y += object_speed
    if object_y > screen_height:
        object_y = -object_height
        object_x = random.randint(0, screen_width - object_width)

    # Check for collision
    if (player_x < object_x + object_width and
        player_x + player_width > object_x and
        player_y < object_y + object_height and
        player_y + player_height > object_y):
        score += 1
        object_y = -object_height
        object_x = random.randint(0, screen_width - object_width)

    # Draw everything
    screen.fill(black)
    pygame.draw.rect(screen, green, (player_x, player_y, player_width, player_height))
    pygame.draw.rect(screen, red, (object_x, object_y, object_width, object_height))
    
    # Display score
    score_text = font.render(f"Score: {score}", True, white)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(fps)

pygame.quit()
