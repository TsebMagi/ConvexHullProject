# Graham Scan - Tom Switzer <thomas.switzer@gmail.com>
# updated to use python 3 by Doug Whitley

import functools


def turn(p, q, r):
    return (q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1])


def _keep_left(hull, r):
    while len(hull) > 1 and (turn(hull[-2], hull[-1], r) < 1):
            hull.pop()
    if not len(hull) or hull[-1] != r:
        hull.append(r)
    return hull


def convex_hull(points):
    """Returns points on convex hull of an array of points in CCW order."""
    points = sorted(points)
    l = functools.reduce(_keep_left, points, [])
    u = functools.reduce(_keep_left, reversed(points), [])
    return l.extend(u[i] for i in range(1, len(u) - 1)) or l