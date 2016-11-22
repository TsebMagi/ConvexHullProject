# Doug Whitley CS350
# Fall 2016
# Convex Hull Testing Program

import QuickHull
import random

points = []

if __name__ == '__main__':
    #open file for storing results
    #run testing 10 times on 10 random inputs
    for num in range(0, 10):
        for num in range(0,10):
            points.append((num-1,num+1))


point_return = QuickHull.quickHullStart(points)
print(points)
print(point_return)