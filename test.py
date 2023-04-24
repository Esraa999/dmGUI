import pygame
pygame.init()

# Create a Pygame window
screen = pygame.display.set_mode((640, 480))

video = pygame.movie.Movie('video.mp4')

# Play the video
video.set_display(screen, pygame.Rect(0, 0, 640, 480))
video.play()

# Loop until the user closes the window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            video.stop()
            pygame.quit()
            exit()

    # Update the screen
    pygame.display.update()
