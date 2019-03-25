import sys
import math
import random
import pygame
from tkinter import *
from neuron import Neuron

numberOfPoints = 2000

neuron = Neuron(2)

radius_range = [100, 110]
distance = -50

points = []
for i in range(0, numberOfPoints):
    r = random.random()
    theta = random.random() * 2 * math.pi
    points.append([r, theta])


def getMofifiedPoints(points):
    newPoints = []
    for point in points:
        if point[1] > math.pi:
            newPoints.append([
                (radius_range[0] + point[0]*(radius_range[1] - radius_range[0]))*math.cos(point[1]), (radius_range[0] + point[0]*(radius_range[1] - radius_range[0]))*math.sin(point[1]) - distance/2, 1])
        else:
            newPoints.append([
                (radius_range[0] + point[0]*(radius_range[1] - radius_range[0]))*math.cos(point[1]) + (radius_range[0] + radius_range[1])/2, (radius_range[0] + point[0]*(radius_range[1] - radius_range[0]))*math.sin(point[1]) + distance/2, 0])
    return newPoints


def train():
    neuron.train(getMofifiedPoints(points), 1)

pygame.init()

master = Tk()

r1Slider = Scale(master, from_=1, to=20,
                 orient=HORIZONTAL, label='Radius Start')
r1Slider.pack()
r1Slider.set(10)

r2Slider = Scale(master, from_=1, to=20,
                 orient=HORIZONTAL, label='Radius End')
r2Slider.pack()
r2Slider.set(11)

distanceSlider = Scale(master, from_=-10, to=10,
                       orient=HORIZONTAL, label='Distance')
distanceSlider.pack()
distanceSlider.set(5)

trainButton = Button(master, text="Train",
                     command=train)
trainButton.pack()

size = width, height = 500, 500
black = 0, 0, 0
center = [250, 250]

screen = pygame.display.set_mode(size)

while True:
    master.update()
    radius_range[0] = r1Slider.get()*10
    radius_range[1] = r2Slider.get()*10
    distance = distanceSlider.get()*10

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    screen.fill(black)

    xyPoints = getMofifiedPoints(points)

    pygame.draw.line(screen, (0, 255, 0), [0, (-neuron.w[1] * (-250) + neuron.w[0])/neuron.w[2] + center[1]], [
                     500, (-neuron.w[1] * (250) + neuron.w[0])/neuron.w[2] + center[1]])

    for x in xyPoints:
        color = (0, 255, 255)
        if neuron.activate(x) and x[2] == 1:
            color = (255, 0, 0)
        elif not neuron.activate(x) and x[2] == 0:
            color = (0, 0, 255)
        elif neuron.activate(x) and x[2] == 0:
            color = (255, 0, 255)
        pygame.draw.circle(screen, color, [int(
            x[0] + center[0]), int(x[1]+center[1])], 1)
    pygame.display.flip()
