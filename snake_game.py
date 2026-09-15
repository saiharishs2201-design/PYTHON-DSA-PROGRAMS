"""
Simple Snake Game in Python using pygame.

Controls:
    Arrow keys - move the snake
    R - restart after game over
    Q / Esc - quit

Install dependency (if needed):
    pip install pygame
"""

import pygame
import random
import sys

# ---------- Setup ----------
pygame.init()

WIDTH, HEIGHT = 600, 400
BLOCK = 20
SPEED = 10  # frames per second (snake speed)

WHITE = (255, 255, 255)
BLACK = (10, 10, 10)
GREEN = (0, 200, 0)
RED = (200, 30, 30)
GRAY = (40, 40, 40)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
font = pygame.font.SysFont("consolas", 28)


def random_food(snake):
    """Place food on a cell not occupied by the snake."""
    while True:
        pos = (
            random.randrange(0, WIDTH, BLOCK),
            random.randrange(0, HEIGHT, BLOCK),
        )
        if pos not in snake:
            return pos


def draw_grid():
    for x in range(0, WIDTH, BLOCK):
        pygame.draw.line(screen, GRAY, (x, 0), (x, HEIGHT))
    for y in range(0, HEIGHT, BLOCK):
        pygame.draw.line(screen, GRAY, (0, y), (WIDTH, y))


def draw_snake(snake):
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (*segment, BLOCK, BLOCK))


def draw_food(food):
    pygame.draw.rect(screen, RED, (*food, BLOCK, BLOCK))


def show_score(score):
    text = font.render(f"Score: {score}", True, WHITE)
    screen.blit(text, (10, 10))


def game_over_screen(score):
    screen.fill(BLACK)
    msg1 = font.render(f"Game Over! Score: {score}", True, WHITE)
    msg2 = font.render("Press R to Restart or Q to Quit", True, WHITE)
    screen.blit(msg1, (WIDTH // 2 - msg1.get_width() // 2, HEIGHT // 2 - 30))
    screen.blit(msg2, (WIDTH // 2 - msg2.get_width() // 2, HEIGHT // 2 + 10))
    pygame.display.flip()

    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_q, pygame.K_ESCAPE):
                    pygame.quit()
                    sys.exit()
                if event.key == pygame.K_r:
                    waiting = False


def main():
    while True:
        # Initial snake: 3 segments, moving right
        snake = [(100, 100), (80, 100), (60, 100)]
        direction = (BLOCK, 0)
        food = random_food(snake)
        score = 0

        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP and direction != (0, BLOCK):
                        direction = (0, -BLOCK)
                    elif event.key == pygame.K_DOWN and direction != (0, -BLOCK):
                        direction = (0, BLOCK)
                    elif event.key == pygame.K_LEFT and direction != (BLOCK, 0):
                        direction = (-BLOCK, 0)
                    elif event.key == pygame.K_RIGHT and direction != (-BLOCK, 0):
                        direction = (BLOCK, 0)
                    elif event.key in (pygame.K_q, pygame.K_ESCAPE):
                        pygame.quit()
                        sys.exit()

            # Move snake
            head_x, head_y = snake[0]
            new_head = (head_x + direction[0], head_y + direction[1])

            # Check wall collision
            if not (0 <= new_head[0] < WIDTH and 0 <= new_head[1] < HEIGHT):
                running = False
                break

            # Check self collision
            if new_head in snake:
                running = False
                break

            snake.insert(0, new_head)

            # Check food collision
            if new_head == food:
                score += 1
                food = random_food(snake)
            else:
                snake.pop()  # remove tail if no food eaten

            # Draw everything
            screen.fill(BLACK)
            draw_grid()
            draw_snake(snake)
            draw_food(food)
            show_score(score)
            pygame.display.flip()
            clock.tick(SPEED)

        game_over_screen(score)


if __name__ == "__main__":
    main()
