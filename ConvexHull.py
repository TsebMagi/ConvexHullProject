# Doug Whitley CS350
# Fall 2016
# Convex Hull Testing Program

import MonotoneChain
import QuickHull
import random
import time
import OtherQuickHull

random.seed(time.clock())
points = []
points_2 = [(0, 0), (0, 1), (1, 0), (1, 1)]
if __name__ == '__main__':
    # open file for storing results
    # run testing 10 times on 10 random inputs
    for num in range(0, 1000):
        points.append((random.randint(0 , 100), random.randint(0 , 100)))

    print(points)
    q_points = points
    m_points = points
    q_points = OtherQuickHull.get_hull_points(q_points)
    m_points = MonotoneChain.convex_hull(m_points)

    print ("Outputs!")
    print("Quick Hull: ")
    print(q_points)
    print("Monotone Chain: ")
    print(m_points)
