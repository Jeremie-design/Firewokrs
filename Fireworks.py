import pygame
import random

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fireworks")
    clock = pygame.time.Clock()

    colors = [
        (255, 179, 186),  #  Pink
        (255, 223, 186),  #  Peach
        (255, 255, 186),  # Yellow
        (186, 255, 201),  #  Mint
        (186, 225, 255),  # Blue
        (221, 160, 221),  # Lavender
        ]
    
    balls = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                balls.append({"x": x, "y": y, "radius": 5, "color": random.choice(colors)})

        for ball in balls:
            ball["y"] -= 2
            ball["radius"] += 0.3

        screen.fill((0, 0, 0))
        for ball in balls:
            pygame.draw.circle(screen, (ball["color"]), (ball["x"], ball["y"]), int(ball["radius"]))
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()