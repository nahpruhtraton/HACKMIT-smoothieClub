# parking_datapoints_function.py
def generate_points(file, parking_width):
    with open(file) as coordinateFile:
        for line in coordinateFile:
            if '#' not in line:
                # lines are written as x1, y1 ; x2, y2
                x_y = line.split(';')
                # x_y = ['x1, y2' , 'x2, y2']
                x_y1 = x_y[0]
                x_y2 = x_y[1]
                pair1 = x_y1.split(',')
                pair2 = x_y2.split(',')

                temp_x1 = pair1[0]
                temp_y1 = pair1[1]
                temp_x2 = pair2[0]
                temp_y2 = pair2[1]
                tempSlope = (temp_y2 - temp_y1)/(temp_x2 - temp_x1)
                # now we have (x1, y1), (x2, y2) and m

    slopeList.append[tempSlope]

if __name__ == "__main__":
    slopeList = []
    # did you know: according to cambridgema.gov, the width of
    # off street parking spaces is required to be 22 ft?
    space_size = 22
    generate_points(coordinates.txt, space_size)
