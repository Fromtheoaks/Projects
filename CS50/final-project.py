import pygame, sys, random

# Ball animation function: Handles ball movement and collisions
def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score

    # Move the ball
    ball.x += ball_speed_x
    ball.y += ball_speed_y

    # Check for collisions with the top and bottom walls
    if ball.top <= 0 or ball.bottom >= screen_height:
        ball_speed_y *= -1

    # Check for collisions with the left and right walls (scoring events)
    if ball.left <= 0:
        # Ball hits the left wall, increase opponent's score and restart ball to the center.
        opponent_score += 1
        ball_restart()
    elif ball.right >= screen_width:
        # Ball hits the right wall, increase player's score and restart ball to the center.
        player_score += 1
        ball_restart()

    # Check for collisions with the player and the opponent paddles
    if ball.colliderect(player) or ball.colliderect(opponent):
        # Change ball direction based on its current horizontal position
        if ball_speed_x > 0:  # Moving right
            ball.right = min(player.left, opponent.left) - 1
        else:  # Moving left
            ball.left = max(player.right, opponent.right) + 1
        ball_speed_x *= -1


# Player animation function: Handles player paddle movement and boundary checking
def player_animation():
    player.y += player_speed
    # Keep the player paddle within the screen boundaries
    player.top = max(player.top, 0)
    player.bottom = min(player.bottom, screen_height)


# Opponent animation function: Handles opponent paddle movement and follows the ball
def opponent_animation():
    if opponent.top < ball.y:
        opponent.top += opponent_speed
    if opponent.bottom > ball.y:
        opponent.bottom -= opponent_speed
    # Keep the opponent paddle within the screen boundaries
    opponent.top = max(opponent.top, 0)
    opponent.bottom = min(opponent.bottom, screen_height)


# Ball restart function: Resets the ball to the center and gives it a random direction
def ball_restart():
    global ball_speed_x, ball_speed_y
    ball.center = (screen_width / 2, screen_height / 2)
    ball_speed_y *= random.choice((1, -1))
    ball_speed_x *= random.choice((1, -1))


# Function to display the scores on the screen
def display_scores():
    font = pygame.font.Font(None, 74)
    player_text = font.render(str(player_score), True, light_grey)
    opponent_text = font.render(str(opponent_score), True, light_grey)
    screen.blit(player_text, (screen_width - 150, 50))
    screen.blit(opponent_text, (50, 50))


# Function to display the game over message and end the game
def game_over(winner_text):
    font = pygame.font.Font(None, 100)
    text = font.render(winner_text, True, light_grey)
    text_rect = text.get_rect(center=(screen_width / 2, screen_height / 2))
    screen.blit(text, text_rect)
    pygame.display.flip()
    pygame.time.delay(2000)

    # Pause for 2 seconds before quitting the game
    pygame.quit()
    sys.exit()


# General setup
pygame.init()
clock = pygame.time.Clock()

# Scoring variables
player_score = 0
opponent_score = 0
max_score = 5  # The game ends when a player reaches this score

# Setting up the main window
screen_width = 1150
screen_height = 800
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Pong CS50')

# Game rectangles
ball = pygame.Rect(screen_width / 2 - 15, screen_height / 2 - 15, 30, 30)
player = pygame.Rect(screen_width - 20, screen_height / 2 - 70, 10, 140)
opponent = pygame.Rect(10, screen_height / 2 - 70, 10, 140)

bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)

ball_speed_x = 7 * random.choice((1, -1))
ball_speed_y = 7 * random.choice((1, -1))
player_speed = 0
opponent_speed = 7

while True:
    # Handling input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player_speed += 7
            if event.key == pygame.K_UP:
                player_speed -= 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player_speed -= 7
            if event.key == pygame.K_UP:
                player_speed += 7

    ball_animation()
    player_animation()
    opponent_animation()

    # Check for collisions with the goal
    if ball.left <= 0:
        player_score += 1
        ball_restart()
    elif ball.right >= screen_width:
        opponent_score += 1
        ball_restart()

    # Check for game over condition
    if player_score >= max_score:
        game_over("Player wins!")
    elif opponent_score >= max_score:
        game_over("Opponent wins!")

    # Visuals
    screen.fill(bg_color)
    pygame.draw.rect(screen, light_grey, player)
    pygame.draw.rect(screen, light_grey, opponent)
    pygame.draw.ellipse(screen, light_grey, ball)
    pygame.draw.aaline(screen, light_grey, (screen_width / 2, 0), (screen_width / 2, screen_height))
    display_scores()

    # Updating the window
    pygame.display.flip()
    clock.tick(60)
