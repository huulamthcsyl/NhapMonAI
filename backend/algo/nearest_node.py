def nearest_node(point, coords):
    """
    Find the nearest node to a point and return the corresponding node label

    ### Parameters
    ----------
    node : tuple
        The coordinates of a point
    coords : list
        A list of coordinates of points

    ### Returns
    -------
    tuple
        The coordinates of the nearest node
    """
    dist = float("inf")
    nearest_node = None
    lat, long = point
    for y, x in coords:
        euclidean_distance = (lat - y) ** 2 + (long - x) ** 2
        if euclidean_distance < dist:
            dist = euclidean_distance
            nearest_node = (y, x)
    return nearest_node