# Doug Whitley CS350
# Fall 2016
# Convex Hull Testing Program

import MonotoneChain
import QuickHull
import random
import time

random.seed(time.ctime())
points = []
if __name__ == '__main__':
    # open file for storing results
    for num in range(0, 100000):
        points.append((random.randint(-100000 , 100000), random.randint(-100000 , 100000)))

    print(points)
    q_points = points
    m_points = points
    q_points = QuickHull.quick_hull(q_points)
    m_points = MonotoneChain.convex_hull(m_points)

    print ("Outputs!")
    print("Quick Hull: ")
    print(q_points)
    print("Monotone Chain: ")
    print(m_points)
