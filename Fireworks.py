import pygame

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fireworks")
    clock = pygame.time.Clock()

    clicks = []


    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            if event.type == pygame.MOUSEBUTTONDOWN:
                clicks.append(event.pos)

        screen.fill("black")
        for position in clicks:
            pygame.draw.circle(screen, "white", position, 5)

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()