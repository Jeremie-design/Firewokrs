import pygame
import random
import math

FUSE_TIME = 190          # duration before a rocket bursts
BURST_FADE_TIME = 40     # how long burst particles take to fade
TRAIL_LIFETIME = 20      # how long a rising rockets trail 
PARTICLE_COUNT = 30      # sparks per burst
GRAVITY = 0.05           # slight downward pull on burst sparks


COLORS = [
    (255, 179, 186),  # Pink
    (255, 223, 186),  # Peach
    (255, 255, 186),  # Yellow
    (186, 255, 201),  # Mint
    (186, 225, 255),  # Blue
    (221, 160, 221),  # Lavender
    (255, 105, 180),  # Hot Pink
    (255, 165, 0),    # Orange
    (0, 191, 255),    # Deep Sky Blue
    (124, 252, 0),    # Lawn Green
    (255, 20, 147),   # Deep Pink
    (255, 69, 0),     # Red-Orange
    (0, 255, 127),    # Spring Green
    (138, 43, 226),   # Blue Violet
    (255, 140, 0),    # Dark Orange
]

def make_rocket(x, y):
    return {"x": x, "y": y, "color": random.choice(COLORS), "duration": 0}

