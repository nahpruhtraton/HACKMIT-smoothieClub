# parking_datapoints_function.py
# depreciated- let's move on


# note: since difference in long-lat is so small >> 1 degree
# 1 degree of longitude is ~85km
# 1 degree of latitude is ~110km

import math
def ft_to_km(distance):
    distance = distance * 0.0003048

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
                temp_slope = (temp_y2 - temp_y1)/(temp_x2 - temp_x1)
                # now we have (x1, y1), (x2, y2) and m
                # and can solve for delta_x and delta_y, the distance we need to
                # add for each parking space node
                hypo = math.hypot(temp_x2 - temp_x1, temp_y2 - temp_y1)
                theta = math.atan(temp_slope)
                delta_x = 0.0067056 * math.cos(theta)
                delta_y = 0.0067056 * math.sin(theta)



if __name__ == "__main__":
    # did you know:
    # according to cambridgema.gov, the width of off street parking spaces is required to be 22 ft?
    # 6.42 of <https://www.cambridgema.gov/~/media/Files/CDD/ZoningDevel/Ordinance/zo_article6_1397.ashx>
    space_size = 22
    generate_points(coordinates.txt, space_size)
