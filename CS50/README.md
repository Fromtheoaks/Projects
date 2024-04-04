# pongcs50.py 
#### Video Demo:  <https://youtu.be/22UjENO3H80>

Introduction

My goal for this project was to creat a simple yet logic Pong retro game from cero using Python pygame library. I love to do this kinda of projects and it give me a good amount of pieces for the educational puzzle.

# Pong CS50

This is a simple Pong game implemented in Python using the Pygame library. The game involves two paddles (one controlled by the player and the other controlled by the computer) and a ball that bounces between them. The objective of the game is to score points by getting the ball past the opponent's paddle.

## Prerequisites

- Python 3.x
- Pygame library (`pip install pygame`)

## How to Play

1. Run the Python script `pongcs50.py`.
2. The game window will appear, and the match will start automatically.
3. The player can control their paddle using the **UP** and **DOWN** arrow keys.
4. Each time the ball passes the opponent's paddle, the player scores a point.
5. The game will continue until one of the players reaches the maximum score (default is 5).
6. The match will end, and a message will be displayed indicating the winner.

## Game Controls

- **UP Arrow**: Move the player's paddle up
- **DOWN Arrow**: Move the player's paddle down
- **Close Window**: Click the close button (X) on the window to exit the game

## Game Rules

- If the ball collides with the top or bottom of the window, it will bounce in the opposite direction.
- If the ball collides with the left or right wall, the opponent scores a point, and the ball restarts from the center.
- If the ball collides with a paddle, it changes direction based on its horizontal position, simulating a realistic bounce.

## Scoring

- The game starts with both the player's and opponent's scores set to 0.
- Each time the ball passes the opponent's paddle and hits the left wall, the player gains one point.
- Similarly, if the ball passes the player's paddle and hits the right wall, the opponent gains one point.
- The first player to reach the maximum score (default is 5) wins the game.

## Game Over

- When a player reaches the maximum score, the game will end, and a message will be displayed to announce the winner.
- The game window will automatically close after a 2-second delay.

## Customization

- You can modify the `max_score` variable to set a different maximum score for the game.
- The game speed and paddle speed can be adjusted by changing the relevant variables.

## Acknowledgments

This game is inspired by the classic Pong game and is an implementation based on the CS50 Introduction to Game Development course.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
