import pygame

pygame.init()

screen = pygame.display.set_mode((1200, 800))
clock = pygame.time.Clock()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (
            event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
        ):
            running = False
            break

    screen.fill("Black")
    clock.tick(60)


pygame.quit()
