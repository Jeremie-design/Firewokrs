# Need to import this later 
#ss
#hjsjs 
#hhshwb

import pygame
import random
import math

FUSE_TIME = 190         
BURST_FADE_TIME = 40     
TRAIL_LIFETIME = 20      
PARTICLE_COUNT = 30      
GRAVITY = 0.05           

COLORS = [
    (255, 179, 186),  # Pink
    (255, 223, 186),  # Peach
    (255, 255, 186),  # Yellow
    (186, 255, 201),  # Mint
    (186, 225, 255),  # Blue
    (221, 160, 221),  # Lavender
]


def make_rocket(x, y):
    return {"x": x, "y": y, "color": random.choice(COLORS), "duration": 0}


def update_rocket(rocket):
    rocket["duration"] += 2
    rocket["y"] -= 2


def make_particle(x, y):
    angle = random.uniform(0, 2 * math.pi)
    speed = random.uniform(2, 6)
    return {
        "x": x,
        "y": y,
        "dx": speed * math.cos(angle),
        "dy": speed * math.sin(angle),
        "color": random.choice(COLORS),
        "duration": 0,
    }


def update_particle(particle):
    particle["x"] += particle["dx"]
    particle["y"] += particle["dy"]
    particle["dy"] += GRAVITY
    particle["duration"] += 1


def fade_fraction(duration, max_duration):
    return max(0, 1 - duration / max_duration)


def is_expired(duration, max_duration):
    return duration >= max_duration


def draw_trail(screen, trail):
    fade = fade_fraction(trail["duration"], TRAIL_LIFETIME)
    brightness = int(180 * fade)
    pygame.draw.circle(screen, (brightness, brightness, brightness), (trail["x"], trail["y"]), 3)


def draw_rocket(screen, rocket):
    pygame.draw.circle(screen, rocket["color"], (rocket["x"], rocket["y"]), 4)


def draw_particle(screen, particle):
    fade = fade_fraction(particle["duration"], BURST_FADE_TIME)
    r, g, b = particle["color"]
    faded_color = (int(r * fade), int(g * fade), int(b * fade))
    tail_x = particle["x"] - particle["dx"] * 2
    tail_y = particle["y"] - particle["dy"] * 2
    pygame.draw.line(screen, faded_color, (int(tail_x), int(tail_y)), (int(particle["x"]), int(particle["y"])), 3)


def main():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Fireworks")
    clock = pygame.time.Clock()

    rockets = []
    trails = []
    particles = []

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos
                rockets.append(make_rocket(x, y))

        still_rising = []
        for rocket in rockets:
            update_rocket(rocket)
            if is_expired(rocket["duration"], FUSE_TIME):
                for _ in range(PARTICLE_COUNT):
                    particles.append(make_particle(rocket["x"], rocket["y"]))
            else:
                trails.append({"x": rocket["x"], "y": rocket["y"], "duration": 0})
                still_rising.append(rocket)
        rockets = still_rising

        for trail in trails:
            trail["duration"] += 1
        trails = [trail for trail in trails if not is_expired(trail["duration"], TRAIL_LIFETIME)]

        for particle in particles:
            update_particle(particle)
        particles = [p for p in particles if not is_expired(p["duration"], BURST_FADE_TIME)]

        screen.fill((0, 0, 0))
        for trail in trails:
            draw_trail(screen, trail)
        for rocket in rockets:
            draw_rocket(screen, rocket)
        for particle in particles:
            draw_particle(screen, particle)
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()