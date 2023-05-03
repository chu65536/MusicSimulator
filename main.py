import pygame as pg
import numpy as np
import random

WIDTH = 600
HEIGHT = 300
FPS = 300
N = 25

BLACK = (0, 0, 0)
WHITE = (255, 255 ,255)

# class
class Bar():
    def __init__(self, coords, color, speed, surface):
        self.coords = coords
        self.color = color
        self.surface = surface
        self.goal = coords[3]
        self.speed = speed
    
    def draw(self):
        pg.draw.rect(self.surface, self.color, self.coords)

    def update(self):
        if self.goal == self.coords[3]:
            self.goal = random.randrange(0, SURFACE_HEIGHT)
        if self.goal < self.coords[3]:
            self.coords[1] += self.speed
            self.coords[3] -= self.speed
        if self.goal > self.coords[3]:
            self.coords[1] -= self.speed
            self.coords[3] += self.speed

# window init
pg.init()
pg.mixer.init()
display = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Visualizer")
clock = pg.time.Clock()

# surface init
SURFACE_WIDTH = WIDTH - WIDTH // N
SURFACE_HEIGHT = HEIGHT - HEIGHT // N

display.fill(WHITE)
surface = pg.Surface((SURFACE_WIDTH, SURFACE_HEIGHT))

# Bars
BAR_WIDTH = SURFACE_WIDTH // N
BAR_HEIGHT = SURFACE_HEIGHT // 2

bars = []
random_color = np.array([random.random(), random.random(), random.random()])
for i in range(N):
    coords = [i * BAR_WIDTH, BAR_HEIGHT, BAR_WIDTH, BAR_HEIGHT]
    color = random_color * 255 / N * (i + 1)
    speed = 1
    bar = Bar(coords, color, speed, surface)
    bars.append(bar)

# main cycle
running = True
while running:
    clock.tick(FPS)

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    surface.fill(WHITE)
    for bar in bars:
        bar.update()
        bar.draw()

    display.blit(surface, (WIDTH // N // 2, HEIGHT // N // 2))
    pg.display.flip()

pg.quit()