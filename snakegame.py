import pygame
import random

# Initialize Pygame
pygame.init()

# Initialize the mixer for sound
pygame.mixer.init(frequency=22050, size=-16, channels=2)

# Load the sound effect
try:
    eat_sound = pygame.mixer.Sound('eat_sound.wav')  # Ensure the sound file is in the same directory
    eat_sound.set_volume(1.0)  # Set volume to maximum
except pygame.error as e:
    print(f"Error loading sound: {e}")
    eat_sound = None  # Set to None if the sound fails to load

# Set up the game window
width, height = 600, 600 
game_screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("SNAKE_GAME")

# Initialize snake position and movement
snake_x, snake_y = width // 2, height // 2
change_x, change_y = 0, 0

# Initialize food position
food_x, food_y = random.randrange(0, width // 10) * 10, random.randrange(0, height // 10) * 10
clock = pygame.time.Clock()

# Initialize snake body
snake_body = [(snake_x, snake_y)]

def display_snake_and_food():
    global snake_x, snake_y, food_x, food_y
    snake_x = (snake_x + change_x) % width
    snake_y = (snake_y + change_y) % height

    # Check for collision with the left and right borders only
    if snake_x < 5 or snake_x >= width - 5:
        print("GAME OVER!! You hit the border!")
        pygame.quit()
        quit()

    snake_body.append((snake_x, snake_y))

    # Check if the snake has eaten the food
    if food_x == snake_x and food_y == snake_y:
        if eat_sound:  # Play the sound effect only if it was loaded successfully
            eat_sound.stop()  # Stop any currently playing sound
            eat_sound.play()  # Play the sound effect
            print("Playing eat sound!")  # Debugging output
        food_x, food_y = random.randrange(0, width // 10) * 10, random.randrange(0, height // 10) * 10
    else:
        del snake_body[0]

    game_screen.fill((0, 0, 0))  # Fill the screen with black

    # Draw food
    pygame.draw.rect(game_screen, (255, 255, 255), (food_x, food_y, 10, 10))  # Draw food

    # Draw snake body
    for index, (x, y) in enumerate(snake_body):
        if index == len(snake_body) - 1:  # Draw the head
            pygame.draw.circle(game_screen, (0, 255, 0), (x + 5, y + 5), 10)  # Head
        else:  # Draw the body segments
            pygame.draw.circle(game_screen, (0, 200, 0), (x + 5, y + 5), 8)  # Body segments

    # Draw red borders (only left and right)
    pygame.draw.rect(game_screen, (255, 0, 0), (0, 0, 5, height))  # Left border
    pygame.draw.rect(game_screen, (255, 0, 0), (width - 5, 0, 5, height))  # Right border

    pygame.display.update()  # Update the display

while True:
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                change_x = -10
                change_y = 0
            elif event.key == pygame.K_RIGHT:
                change_x = 10
                change_y = 0
            elif event.key == pygame.K_UP:
                change_y = -10
                change_x = 0
            elif event.key == pygame.K_DOWN:
                change_y = 10
                change_x = 0

    display_snake_and_food()
    clock.tick(15)  # Control the game speed