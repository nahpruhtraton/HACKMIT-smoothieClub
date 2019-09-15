def coord_interpolate(start: tuple, end: tuple):
    delta = 0.000668767523134
    distance = ((start[0] - end[0])**2 + (start[1] - end[1])**2)**(1/2)
    num_stops = distance / delta
    slope = (start[1] - end[1])/(start[0] - end[0])
    delta_x = delta / (slope + 1)
    delta_y = delta - delta_x
    print(start)
    intermediate = list(start)
    while num_stops and intermediate[0] < end[0] and intermediate[1] < end[1]:
        intermediate[0] += delta_x
        intermediate[1] += delta_y 
        print(tuple(intermediate))
        num_stops -= 1
