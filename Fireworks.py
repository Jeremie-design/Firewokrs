import pygame
import random


time = 240
fade_time = 40

def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fireworks")
    clock = pygame.time.Clock()

    colors = [
       (0, 255, 255),  # Cyan
        (255, 0, 255),  # Magenta
        (255, 255, 0),  # Yellow
        (255, 165, 0),  # Orange
        (0, 128, 0),    # Green
        (0, 0, 255),    # Blue
        (255, 0, 0)     # Red  
        
        ]

    balls = []
    trails = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                balls.append({"x": x, "y": y, "radius": 7, "color": random.choice(colors), "duration": 0, "fade": 1})

        for ball in balls:
            ball["duration"] += 2
            ball["y"] -= 2
            if ball["duration"] < time:
                trails.append({"x": ball["x"], "y": ball["y"], "duration": 0})
            else:
                ball["radius"] += 1.5
                burst_duration = ball["duration"] - time
                ball["fade"] = max(0, 1 - burst_duration / fade_time)

        new_trails = []

        for trail in trails:
            trail["duration"] += 1
            if trail["duration"] < 20:
                new_trails.append(trail)
        trails = new_trails

        screen.fill((0, 0, 0))

        for trail in trails:
            fade = 1 - (trail["duration"] / 20)
            brightness = int(180 * fade)
            pygame.draw.circle(screen, (brightness, brightness, brightness), (trail["x"], trail["y"]), 3)

        for ball in balls:
            r, g, b = ball["color"]
            faded_color = (int(r * ball["fade"]), int(g * ball["fade"]), int(b * ball["fade"]))
            pygame.draw.circle(screen, faded_color, (ball["x"], ball["y"]), int(ball["radius"]))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()