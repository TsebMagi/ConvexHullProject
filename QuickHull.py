"""
QuickHull Object

This object manages the threads created
by each iteration of QuickHull

Author: Jared Siraco
"""
# imports
from math import sqrt

# custom imports
import Triangles

triList = []


def quickHullStart(points):  # Setup for the QuickHull Algorithm
    maxY = -1
    minY = float('inf')
    for p in points:  # getting highest and lowest points (r, q)
        if p[1] > maxY:
            maxY = p[1]
            q = p
        if p[1] < minY:
            minY = p[1]
            r = p

    points.remove(r)
    points.remove(q)
    hull = r + q

    [set0, set1] = Triangles.splitPoints(r, q, q,
                                         points)  # Spliting points in half by a line with the Highest and lowest points

    quickHullAlg(set0, r, q)
    quickHullAlg(set1, r, q)

    #added to base code
    return triList


def quickHullAlg(points, r, q):
    furthestPoint = []  # In the inital call q and r two points with the highest and lowest y value
    maxdist = -1

    if points == []:
        return

    if len(points) == 1:
        furthestPoint = points

    for p in points:
        temp = sqrt((r[0] - p[0]) ** 2 + (r[1] - p[1]) ** 2) + sqrt(
            (q[0] - p[0]) ** 2 + (q[1] - p[1]) ** 2)  # distance of p from q and p added together
        if (temp > maxdist):
            furthestPoint = p  # finds the furthest point from the line r, q
            maxdist = temp

    if (furthestPoint == []):
        return
    points.remove(furthestPoint)

    triangle = r + q + furthestPoint
    triList.append(triangle)  # adding a triangle to the set to print out

    [set0, set1] = Triangles.splitPoints(r, furthestPoint, q, points)
    [set0, set2] = Triangles.splitPoints(q, furthestPoint, r, points)

    quickHullAlg(set1, r, furthestPoint)
    quickHullAlg(set2, furthestPoint, q)
