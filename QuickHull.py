

# 2D cross product of OA and OB vectors, i.e. z-component of their 3D cross product.
# Returns a positive value, if OAB makes a counter-clockwise turn,
# negative for clockwise turn, and zero if the points are collinear.
def cross(a, b, o):
    return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])


# http://stackoverflow.com/questions/27461634/calculate-distance-between-a-point-and-a-line-segment-in-latitude-and-longitude
def distance(p0, p1, p2):  # p3 is the point
    x0, y0 = p0
    x1, y1 = p1
    x2, y2 = p2
    nom = abs((y2 - y1) * x0 - (x2 - x1) * y0 + x2 * y1 - y2 * x1)
    denom = ((y2 - y1)**2 + (x2 - x1) ** 2) ** 0.5
    result = nom / denom
    return result


def quick_hull(points: list):

    # sort the points and remove duplicates
    points = sorted(set(points))
    convex_hull = []
    points_above = []
    points_below = []
    # base case
    if len(points) < 4:
        return points

    # get left and right most points then put them on the hull and remove the points added to the hull from the set
    left_most = points[0]
    right_most = points[-1]
    convex_hull.append(left_most)
    convex_hull.append(right_most)
    points.remove(left_most)
    points.remove(right_most)

    # break remaining points into upper and lower set
    for point in points:
        check = cross(left_most,right_most,point)
        if check > 0:
            points_above.append(point)
        elif check < 0:
            points_below.append(point)

    # call into the uper and lower half recursion
    find_hull(points_above, left_most, right_most, convex_hull)
    find_hull(points_below, right_most, left_most, convex_hull)
    return convex_hull


def find_hull(points: [tuple], l : tuple, r : tuple, convex_hull):

    # local vars
    max_distance = 0
    farthest_point = None
    left_set = []
    right_set = []

    # base case for recursing into list of size 1 or 0
    if len(points) == 0:
        return

    # find farthest one out
    for point in points:
        calc_distance = distance(l, r, point)
        if calc_distance > max_distance:
            farthest_point = point
            max_distance = calc_distance

    # remove point that was just found and add it to hull
    if max_distance > 0:
        points.remove(farthest_point)
        convex_hull.append(farthest_point)
    else:
        return

    # break remaining points into sets
    for point in points:
        if cross(l, farthest_point, point) > 0:
            left_set.append(point)
        elif cross(farthest_point,r,point) > 0:
            right_set.append(point)

    # recurse onto the slip sets
    find_hull(left_set,l,farthest_point,convex_hull)
    find_hull(right_set,farthest_point,r,convex_hull)