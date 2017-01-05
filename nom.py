import pygame

WINWIDTH, WINHEIGHT = 640, 360

if __name__ == "__main__":

    pygame.init()
    window = pygame.display.set_mode((WINWIDTH, WINHEIGHT))

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.update()
