# Doug Whitley CS350
# Fall 2016
# Convex Hull Testing Program

import MonotoneChain
import QuickHull
import JarvisMarch
import random
import time

random.seed(time.ctime())
points = []

if __name__ == '__main__':
    # open file for storing results
    output = open('output2.txt','w')
    for num in range(1, 31):
        print("Run ", num)
        for i in range(0, num* 10000):
            points.append((random.randint(-100000, 100000), random.randint(-100000 , 100000)))

        q_points = points
        m_points = points
        j_points = points

        q_time = 0
        m_time = 0
        j_time = 0

        # Time the Quick Hull
        start_time = time.time() * 1000
        QuickHull.quick_hull(q_points)
        end_time = time.time() * 1000
        q_time = end_time - start_time

        # Time the Quick Hull
        start_time = time.time() * 1000
        MonotoneChain.convex_hull(m_points)
        end_time = time.time() * 1000
        m_time = end_time - start_time

        # Time the Quick Hull
        start_time = time.time() * 1000
        JarvisMarch.convex_hull(j_points)
        end_time = time.time() * 1000
        j_time = end_time - start_time

        header_string = "input size "+ (num*10000).__str__() +"\n"
        QuickHull_string = "Quick Hull , input Size "+ (num*10000).__str__()+ "," + q_time.__str__() +"\n"
        MonotoneChain_string = "Monotone Chain , input Size "+ (num*10000).__str__()+ "," + m_time.__str__() + "\n"
        Jarvis_March_string = "Jarvis_March , input Size "+ (num*10000).__str__() + "," + j_time.__str__() + "\n"
        output.write(header_string)
        output.write(QuickHull_string)
        output.write(MonotoneChain_string)
        output.write(Jarvis_March_string)
    output.close()
    print("Done!")