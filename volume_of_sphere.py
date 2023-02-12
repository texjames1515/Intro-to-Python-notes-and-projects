import math
print('input the radius of a sphere and I will tell you the volume')
r = float(input('radius in cm: '))  # radius
volume = (4/3) * (r ** 3) * math.pi

print('the volume is: ' + str(volume))