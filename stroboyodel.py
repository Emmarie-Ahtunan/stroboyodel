import pygame
import math

# Initialize Pygame
pygame.init()

# Set the screen dimensions (not relevant for sound)
width, height = 800, 600
screen = pygame.display.set_mode((width, height))

# Set the clock for controlling the frame rate
clock = pygame.time.Clock()

# Set the frequency and duration for each sound
frequency = 440
duration = 100  # in milliseconds

# Main loop
running = True
x = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Calculate the sound frequency based on your formula
    sound_frequency = int(440 + 220 * math.sin(x**2))

    # Play the sound
    pygame.mixer.Sound(frequency, duration).play()

    # Update the x value for the next iteration
    x += 0.01

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
