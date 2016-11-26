# Jarvis March O(nh) - Tom Switzer <thomas.switzer@gmail.com>
# updated by Doug Whitley to work with Python 3


def turn(p, q, r):
    """Returns -1, 0, 1 if p,q,r forms a right, straight, or left turn."""
    return (q[0] - p[0])*(r[1] - p[1]) - (r[0] - p[0])*(q[1] - p[1])


def _dist(p, q):
    """Returns the squared Euclidean distance between p and q."""
    dx, dy = q[0] - p[0], q[1] - p[1]
    return dx * dx + dy * dy


def _next_hull_pt(points, p):
    """Returns the next point on the convex hull in CCW from p."""
    q = p
    for r in points:
        t = turn(p, q, r)
        if t < 0 or t == 0 and _dist(p, r) > _dist(p, q):
            q = r
    return q


def convex_hull(points):
    """Returns the points on the convex hull of points in CCW order."""
    hull = [min(points)]
    for p in hull:
        q = _next_hull_pt(points, p)
        if q != hull[0]:
            hull.append(q)
    return hull
