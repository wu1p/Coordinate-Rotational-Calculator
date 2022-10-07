# flip sign
def flip_sign(number):
    if number > 0:
        return (int('-' + str(number)));
    else:
        return (abs(number))
# flip_sign(y)

# counter clock-wise 90
def rotatecw90(cor1, cor2):
    return print('Rotate clock-wise 90 = ' + '[(' + str(cor2) + ', ' + str(flip_sign(cor1)) + ')]')
# rotatecw90(-1, 2)

# Rotate 180
def rotate180(cor1, cor2):
    return print('Rotate 180 = ' + '[(' + str(flip_sign(cor1)) + ', ' + str(flip_sign(cor2)) + ')]');
# rotate180(-1, 2)

# Rotate clock-wise 270
def rotatecw270(cor1, cor2):
    return print('Rotate clock-wise 270 = ' + '[(' + str(flip_sign(cor2)) + ', ' + str(cor1) + ')]');
# rotatecw270(-1,2)

# Rotate counter clock-wise 90
def rotateccw90(cor1, cor2):
    return print('Rotate counter clock-wise 90 = ' + '[(' + str(flip_sign(cor2)) + ',' + str(cor1) + ')]')
# rotateccw90(-1, 2)

# Rotate counter clock-wise 270
def rotateccw270(cor1, cor2):
    return print('Rotate counter clock-wise 270 = ' + '[(' + str(cor2) + ',' + str(flip_sign(cor1)) + ')]')
# rotateccw270(-1, 2)

# All rotations
def rotations(cor1, cor2):
    print('______________________________________________________')
    print('Clock-wise rotations')
    print('')
    rotatecw90(cor1, cor2)
    rotate180(cor1, cor2)
    rotatecw270(cor1, cor2)
    print('------------------------------------------------------')
    print('Counter clock-wise rotations')
    print('')
    rotateccw90(cor1, cor2)
    rotate180(cor1, cor2)
    rotateccw270(cor1, cor2);
    print('______________________________________________________')
# rotations(90, -42)
rotations(int(input('X Coordinate: ')), int(input('Y Coordinate: ')))
input('Press ENTER to exit')
