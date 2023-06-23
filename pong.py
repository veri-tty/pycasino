import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 400
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pong")

# Define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the paddles
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 60
PADDLE_VELOCITY = 5
paddle1 = pygame.Rect(50, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)
paddle2 = pygame.Rect(WIDTH - 50 - PADDLE_WIDTH, HEIGHT // 2 - PADDLE_HEIGHT // 2, PADDLE_WIDTH, PADDLE_HEIGHT)

# Set up the ball
BALL_RADIUS = 10
BALL_VELOCITY_X = 3
BALL_VELOCITY_Y = 3
ball = pygame.Rect(WIDTH // 2 - BALL_RADIUS // 2, HEIGHT // 2 - BALL_RADIUS // 2, BALL_RADIUS, BALL_RADIUS)
ball_velocity = [random.choice([-1, 1]) * BALL_VELOCITY_X, random.choice([-1, 1]) * BALL_VELOCITY_Y]

# Set up the game clock
clock = pygame.time.Clock()

# Set up the points counter
player_score = 0
computer_score = 0
font = pygame.font.Font(None, 36)

# Function to display the points on the screen
def display_scores():
    player_text = font.render("Player: " + str(player_score), True, WHITE)
    computer_text = font.render("Computer: " + str(computer_score), True, WHITE)
    win.blit(player_text, (50, 10))
    win.blit(computer_text, (WIDTH - 200, 10))

# Function to reset the game
def reset_game():
    global player_score, computer_score, BALL_VELOCITY_X, BALL_VELOCITY_Y
    player_score = 0
    computer_score = 0
    paddle1.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    paddle2.y = HEIGHT // 2 - PADDLE_HEIGHT // 2
    ball.center = (WIDTH // 2, HEIGHT // 2)
    BALL_VELOCITY_X = 3
    BALL_VELOCITY_Y = 3
    ball_velocity[0] = random.choice([-1, 1]) * BALL_VELOCITY_X
    ball_velocity[1] = random.choice([-1, 1]) * BALL_VELOCITY_Y

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move player paddle
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and paddle1.y > 0:
        paddle1.y -= PADDLE_VELOCITY
    if keys[pygame.K_s] and paddle1.y < HEIGHT - PADDLE_HEIGHT:
        paddle1.y += PADDLE_VELOCITY

    # Move enemy paddle (AI)
    if ball.y < paddle2.y and paddle2.y > 0:
        paddle2.y -= PADDLE_VELOCITY
    if ball.y > paddle2.y + PADDLE_HEIGHT and paddle2.y < HEIGHT - PADDLE_HEIGHT:
        paddle2.y += PADDLE_VELOCITY

    # Move ball
    ball.x += ball_velocity[0]
    ball.y += ball_velocity[1]

    # Check ball collision with paddles
    if ball.colliderect(paddle1) or ball.colliderect(paddle2):
        ball_velocity[0] = -ball_velocity[0]

    # Check ball collision with walls
    if ball.y < 0 or ball.y > HEIGHT - BALL_RADIUS:
        ball_velocity[1] = -ball_velocity[1]

    # Check if the ball goes out of bounds
    if ball.x < 0:
        computer_score += 1
        if computer_score == 10:
            # Computer wins
            reset_game()
        else:
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_velocity[0] = random.choice([-1, 1]) * BALL_VELOCITY_X
            ball_velocity[1] = random.choice([-1, 1]) * BALL_VELOCITY_Y
            BALL_VELOCITY_X += 0.5
            BALL_VELOCITY_Y += 0.5
    elif ball.x > WIDTH - BALL_RADIUS:
        player_score += 1
        if player_score == 10:
            # Player wins
            reset_game()
        else:
            ball.center = (WIDTH // 2, HEIGHT // 2)
            ball_velocity[0] = random.choice([-1, 1]) * BALL_VELOCITY_X
            ball_velocity[1] = random.choice([-1, 1]) * BALL_VELOCITY_Y
            BALL_VELOCITY_X += 0.5
            BALL_VELOCITY_Y += 0.5

    # Draw game objects
    win.fill(BLACK)
    pygame.draw.rect(win, WHITE, paddle1)
    pygame.draw.rect(win, WHITE, paddle2)
    pygame.draw.ellipse(win, WHITE, ball)
    pygame.draw.aaline(win, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    display_scores()

    # Update the game display
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Quit the game
pygame.quit()