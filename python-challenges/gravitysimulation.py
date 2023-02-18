import pygame
import random
import math

pygame.init()

window_size = (840, 580)

screen = pygame.display.set_mode(window_size)

pygame.display.set_caption("Particle Simulation")

class Particle:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass
        self.vx = random.uniform(-1, 1)
        self.vy = random.uniform(-1, 1)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        self.radius = int(mass)

    def update(self):
        self.x += self.vx
        self.y += self.vy

particles = []

for i in range(10):
    x = random.uniform(0, 640)
    y = random.uniform(0, 480)
    mass = random.uniform(1, 10)
    particle = Particle(x, y, mass)
    particles.append(particle)

def attraction(particle1, particle2):
    dx = particle2.x - particle1.x
    dy = particle2.y - particle1.y
    distance = math.sqrt(dx**2 + dy**2)

    force = (particle1.mass * particle2.mass) / distance**2

    acceleration = force / particle1.mass

    dvx = acceleration * dx / distance
    dvy = acceleration * dy / distance

    particle1.vx += dvx
    particle1.vy += dvy

def collision(particle1, particle2):
    dx = particle2.x - particle1.x
    dy = particle2.y - particle1.y
    distance = math.sqrt(dx**2 + dy**2)

    if distance < particle1.radius + particle2.radius:
        total_mass = particle1.mass + particle2.mass
        particle1.vx = (particle1.mass * particle1.vx + particle2.mass * particle2.vx) / total_mass
        particle1.vy = (particle1.mass * particle1.vy + particle2.mass * particle2.vy) / total_mass
        particle2.vx = (particle1.mass * particle1.vx + particle2.mass * particle2.vx) / total_mass
        particle2.vy = (particle1.mass * particle1.vy + particle2.mass * particle2.vy) / total_mass


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for particle in particles:
        for other in particles:
            if particle != other:
                attraction(particle, other)
        for other in particles:
            if particle != other:
                collision(particle, other)
        particle.update()

    screen.fill((255, 255, 255))

    for particle in particles:
        pygame.draw.circle(screen, particle.color, (int(particle.x), int(particle.y)), particle.radius)

    pygame.display.flip()

pygame.quit()
