import pygame
import random
import math

FUSE_TIME = 190          # duration units before a rocket bursts
BURST_FADE_TIME = 40     # how long burst particles take to fully fade
TRAIL_LIFETIME = 20      # how long a rising rocket's trail dot lingers
PARTICLE_COUNT = 30      # sparks per burst
GRAVITY = 0.05           # slight downward pull on burst sparks

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
    
def draw_rocket(screen, rocket):
    pygame.draw.circle(screen, rocket["color"], (rocket["x"], rocket["y"]), 4)

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
    