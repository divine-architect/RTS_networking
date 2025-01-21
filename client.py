import pygame

pygame.init()
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
units = [pygame.Rect(100, 100, 40, 40), pygame.Rect(300, 200, 40, 40)]
selected = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                clicked = [u for u in units if u.collidepoint(event.pos)]
                if clicked:
                    selected = clicked
                else:
                    selected = []

    screen.fill((30, 30, 30))
    for unit in units:
        color = (0, 255, 0) if unit in selected else (255, 0, 0)
        pygame.draw.rect(screen, color, unit)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
