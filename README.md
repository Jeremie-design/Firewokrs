# Fireworks Simulator

#### Video Demo : [ Not added because I sound corny] 

#### Note before Project 
This entire project was made for CS50P, which I completed not too long ago while I was in high school. The course taught me almost everything I needed to know about Python and has helped me make a lot of cool things. Coding was painful most of the times. Even watching the lectures made it hard, but having some food made it easier. Overall, I am really proud of what I accomplished. My CS50P certificate is also at the bottom.


#### Description

This project is an interactive fireworks simulator built with Python and Pygame. The program opens a plain black window. Clicking anywhere on the window launches a rocket from that spot. The rocket rises for three seconds, trailing a fading line of dim sparks behind it, then bursts into colored particles that fly out in random directions, arc slightly downward under a small simulated gravity, and fade to black over time. Multiple rockets and bursts can be on screen at once, so clicking rapidly produces overlapping fireworks, closer to a real display than a single isolated effect.

The project is split across three files. `project.py` holds all of the program's logic. `test_project.py` contains automated tests, written for pytest that check the project's logic. `requirements.txt` lists pygame, the only external library (`random` and `math` are also used, but are part of the standard library and don't need to be listed).

Inside `project.py`, `main()` runs the actual game loop. It opens the window, waits for mouse clicks and the window-close event, and about sixty times a second, updates every rocket, trail spark, and burst particle currently on screen before redrawing all of them. Everything else in the file is a small, single-purpose function that `main()` calls.

Each firework is three kinds of short-lived objects: a rising rocket, its trailing sparks, and its burst particles. Each represented as a plain dictionary rather than a class, since a dictionary was enough to hold each object's fields (position, color and duration) without the extra overhead of defining a class. 

Each particle also remembers its position from the previous frame, which is what lets it get drawn as a short streak of light instead of a single dot. `lighten_color` brightens a color slightly and is applied to a third of a burst's particles at random, so each explosion has a bit of sparkle rather than being one shade.

The different functions control each part of the firework. `make_rocket` creates the rocket and `update_rocket` moves it, while `make_trail` creates the rocket's trail and `update_trail` moves it. When the rocket explodes, `make_particle` creates the sparks and `update_particle` moves them. Each spark has a random direction and speed, and gravity pulls them down a little each frame, making the sparks curve like a real firework.


The three `draw_` functions are the only functions that use pygame to draw
on the screen. The `make_` and `update_` functions are kept separate and
only work with data like numbers and dictionaries.
This makes testing easier because the seven tested functions do not use
pygame. Pytest can test them directly without opening a window.

Every rocket, trail spark, and particle is discarded the moment it's outlived its purpose, by filtering each list down to only the entries still worth keeping, once per frame. So the program doesn't slowly accumulate invisible, pointless objects the longer it runs.
The goal of this project was to create a simple but fun fireworks simulator that feels natural and responsive. The combination of random colors, directions, speeds, fading particles, and gravity makes each firework slightly different. Multiple fireworks can also be launched at once, allowing the display to build up with each click. This project was really fun and very hard to make, but overall I am really happy with what I made.

![CS50 Certificate for Jeremie Kwapong](https://cs50.harvard.edu/certificates/1a13fbbe-adb0-44f4-85d7-8978b9a206c3.png?size=letter)

