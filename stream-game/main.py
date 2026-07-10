import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the display
screen_width = 288
screen_height = 512
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Flappy Bird")

# Load images
background_img = pygame.image.load("background.png").convert()
background_img = pygame.transform.scale(background_img, (screen_width, screen_height))
bird_img = pygame.image.load("bird.png").convert_alpha()
pipe_img = pygame.image.load("pipe.png").convert_alpha()

# Bird properties
bird_x = 50
bird_y = 200
bird_y_movement = 0
bird_gravity = 0.25

# Pipe properties
pipe_width = 70
pipe_height = random.randint(150, 350)
pipe_x = screen_width
pipe_y = random.randint(-200, -50)
pipe_speed = 2

# Score
score = 0
font = pygame.font.Font("freesansbold.ttf", 24)

def display_score():
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    screen.blit(score_text, (10, 10))

def game_over():
    game_over_text = font.render("Game Over", True, (255, 255, 255))
    screen.blit(game_over_text, (screen_width // 2 - game_over_text.get_width() // 2, screen_height // 2 - game_over_text.get_height() // 2))
    pygame.display.update()
    pygame.time.delay(2000)

# Game state
game_started = False

# Game loop
running = True
while running:
    print(bird_y)
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                game_started = True
                bird_y_movement = -6

    if game_started:
        # Update bird
        bird_y_movement += bird_gravity
        bird_y += bird_y_movement

        # Update pipes
        pipe_x -= pipe_speed
        if pipe_x + pipe_width < 0:
            pipe_x = screen_width
            pipe_height = random.randint(150, 350)
            pipe_y = random.randint(-200, -50)
            score += 1

        # Collision detection
        if bird_y < 0 or bird_y + bird_img.get_height() > screen_height:
            #game_over()
            print("gmae aoer")
            #running = False
        if bird_x + bird_img.get_width() > pipe_x and bird_x < pipe_x + pipe_width:
            if bird_y < pipe_y + pipe_height or bird_y + bird_img.get_height() > pipe_y + pipe_height + 100:
                #game_over()
                print("game eover")
                #running = False

    # Draw objects
    screen.blit(background_img, (0, 0))
    screen.blit(bird_img, (bird_x, bird_y))
    screen.blit(pipe_img, (pipe_x, pipe_y))
    screen.blit(pipe_img, (pipe_x, pipe_y + pipe_height + 100))
    display_score()

    # Update display
    pygame.display.update()

    # Set the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()