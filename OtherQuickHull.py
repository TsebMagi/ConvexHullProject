'''''
    Quick Hull in Python

    Date: 01/06/2016

    Written by: Grant McEwan

    License: Beer license... you should buy me one if you make anything off this :)

    

    This program produces a set of hull points using a similar method to the quick

    Sort Algorithm, so runs in O(nlogn) time
'''



'''
    When called returns a list of points that forms a convex hull around 
    the listPts Given
'''
def get_hull_points(listPts):

    # get the min, and max from the list of points
    min, max = get_min_max_x(listPts)

    hullpts = quickhull(listPts, min, max)

    hullpts = hullpts + quickhull(listPts, max, min)

    return hullpts 

'''
    Does the sorting for the quick hull sorting algorithm
'''
def quickhull(listPts, min, max):
    left_of_line_pts = get_points_left_of_line(min, max, listPts)

    ptC = point_max_from_line(min, max, left_of_line_pts)

    if len(ptC) < 1:
        return [max]

    hullPts = quickhull(left_of_line_pts, min, ptC)

    hullPts = hullPts + quickhull(left_of_line_pts, ptC, max)

    return hullPts

'''
    Reterns all points that a LEFT of a line start->end
'''


def cross(a, b, o):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])



def get_points_left_of_line(start, end, listPts):
    pts = []

    for pt in listPts:
        if cross(start, end, pt) < 0:
            pts.append(pt)

    return pts

'''
    Returns the maximum point from a line start->end
'''
def point_max_from_line(start, end, points):
    max_dist = 0

    max_point = []

    for point in points:
        if point != start and point != end:
            dist = distance(start, end, point)
            if dist > max_dist:
                max_dist = dist
                max_point = point

    return max_point

def get_min_max_x(list_pts):
    min_x = float('inf')
    max_x = 0
    min_y = 0
    max_y = 0

    for x,y in list_pts:
        if x < min_x:
            min_x = x
            min_y = y
        if x > max_x:
            max_x = x
            max_y = y

    return [min_x,min_y], [max_x,max_y]

'''
    Given a line of start->end, will return the distance that
    point, pt, is from the line.
'''
def distance(start, end, pt): # pt is the point
    x1, y1 = start
    x2, y2 = end
    x0, y0 = pt
    nom = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denom = ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5
    result = nom / denom
    return result