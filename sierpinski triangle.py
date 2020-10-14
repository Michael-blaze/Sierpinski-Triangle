import pygame
import math
import sys
import time

sys.setrecursionlimit(10000)

pygame.init()

height = 680
width = 680

win = pygame.display.set_mode((width, height))

pygame.display.set_caption("sierpinski triangle")

red = (255, 0, 0)
yellow = (255, 255, 0)
green = (0, 255, 0)
light_blue = (0, 255, 255)
black = (0, 0, 0)
white = (255, 255, 255)


win.fill(white)

coordinates = [[0, height], [width // 2, 0], [width, height]]


def middle_point(pointA, pointB):
    return [(pointA[0] + pointB[0]) // 2, (pointA[1] + pointB[1]) // 2]


def middle_triangle_coord(coordinates):
    up_left_corner = middle_point(coordinates[0], coordinates[1])
    up_right_corner = middle_point(coordinates[1], coordinates[2])
    down_corner = middle_point(coordinates[0], coordinates[2])
    return [up_left_corner, up_right_corner, down_corner]


def distance(pointA, pointB):
    return math.sqrt((pointA[0] - pointB[0]) ** 2 + (pointB[1] - pointB[1]) ** 2)


# def serpinski_triangle(color, coordinates):
#     if distance(coordinates[0], coordinates[1]) >= 1.5:
#         middle_triangle = middle_triangle_coord(coordinates)
#         pygame.draw.polygon(win, color, middle_triangle)
#         pygame.display.update()
#         # time.sleep(0.1)
#         serpinski_triangle(color, [coordinates[0], middle_triangle[0], middle_triangle[2]])
#         serpinski_triangle(color, [middle_triangle[0], coordinates[1], middle_triangle[1]])
#         serpinski_triangle(color, [middle_triangle[2], middle_triangle[1], coordinates[2]])


q = []

def serpinski_triangle(coordinates):
    if distance(coordinates[0], coordinates[1]) >= 40:
        middle_triangle = middle_triangle_coord(coordinates)
        q.append([middle_triangle, distance(middle_triangle[0], middle_triangle[1])])

        serpinski_triangle([coordinates[0], middle_triangle[0], middle_triangle[2]])
        serpinski_triangle([middle_triangle[0], coordinates[1], middle_triangle[1]])
        serpinski_triangle([middle_triangle[2], middle_triangle[1], coordinates[2]])


pygame.draw.polygon(win, red, coordinates)
serpinski_triangle(coordinates)

def sort_second(val):
    return val[1]


q.sort(key = sort_second, reverse = True)

# num_of_triangles = 1

# while len(q) > 0:
#     for i in range(num_of_triangles):
#         if len(q) > 0:
#             pygame.draw.polygon(win, black, q[0][0])
#             q.pop(0)

#     num_of_triangles = num_of_triangles * 3

#     pygame.display.update()
#     time.sleep(0.3)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    pygame.draw.polygon(win, red, coordinates)
    pygame.display.update()
    time.sleep(0.3)
    serpinski_triangle(coordinates)

    q.sort(key = sort_second, reverse = True)
    num_of_triangles = 1

    while len(q) > 0:
        for i in range(num_of_triangles):
            if len(q) > 0:
                pygame.draw.polygon(win, black, q[0][0])
                q.pop(0)

        num_of_triangles = num_of_triangles * 3

        pygame.display.update()
        time.sleep(0.3)
