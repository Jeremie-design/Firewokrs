
from project import (
    make_rocket,
    update_rocket,
    make_particle,
    update_particle,
    fade_fraction,
    is_expired,
    COLORS,
    FUSE_TIME,
    BURST_FADE_TIME,
    TRAIL_LIFETIME,
    GRAVITY,
)


def test_make_rocket():
    rocket = make_rocket(100, 200)

    assert rocket["x"] == 100
    assert rocket["y"] == 200
    assert rocket["duration"] == 0
    assert rocket["color"] in COLORS


def test_update_rocket():
    rocket = {
        "x": 100,
        "y": 200,
        "color": COLORS[0],
        "duration": 0,
    }

    update_rocket(rocket)

    assert rocket["y"] == 198
    assert rocket["duration"] == 2


def test_make_particle():
    particle = make_particle(70, 80)

    assert particle["x"] == 70
    assert particle["y"] == 80
    assert particle["duration"] == 0
    assert particle["color"] in COLORS

    speed = (particle["dx"] ** 2 + particle["dy"] ** 2) ** 0.5
    assert 2 <= speed <= 6


def test_update_particle():
    particle = {
        "x": 10,
        "y": 20,
        "dx": 3,
        "dy": 4,
        "color": COLORS[0],
        "duration": 0,
    }

    update_particle(particle)

    assert particle["x"] == 13
    assert particle["y"] == 24
    assert particle["dy"] == 4 + GRAVITY
    assert particle["duration"] == 1


def test_fade_fraction():
    assert fade_fraction(0, 20) == 1
    assert fade_fraction(10, 20) == 0.5
    assert fade_fraction(20, 20) == 0
    assert fade_fraction(30, 20) == 0


def test_is_expired():
    assert is_expired(0, 20) is False
    assert is_expired(19, 20) is False
    assert is_expired(20, 20) is True
    assert is_expired(25, 20) is True


def test_rocket_expiration():
    rocket = {
        "x": 100,
        "y": 200,
        "color": COLORS[0],
        "duration": FUSE_TIME - 2,
    }

    update_rocket(rocket)

    assert rocket["duration"] == FUSE_TIME
    assert is_expired(rocket["duration"], FUSE_TIME)


def test_particle_expiration():
    particle = {
        "x": 10,
        "y": 20,
        "dx": 3,
        "dy": 4,
        "color": COLORS[0],
        "duration": BURST_FADE_TIME - 1,
    }

    update_particle(particle)

    assert particle["duration"] == BURST_FADE_TIME
    assert is_expired(particle["duration"], BURST_FADE_TIME)


def test_trail_expiration():
    duration = TRAIL_LIFETIME

    assert is_expired(duration, TRAIL_LIFETIME) is True