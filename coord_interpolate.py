def coord_interpolate(start: tuple, end: tuple): -> List
    delta = 0.000668767523134
    slope = (start[1] - end[1])/(start[0] - end[0])
    delta_x = delta / (slope + 1)
    delta_y = delta - delta_x
    results = [start]
    intermediate = list(start)
    while intermediate[0] < end[0] and intermediate[1] < end[1]:
        intermediate[0] += delta_x
        intermediate[1] += delta_y
        results.append(intermediate)
    return results
