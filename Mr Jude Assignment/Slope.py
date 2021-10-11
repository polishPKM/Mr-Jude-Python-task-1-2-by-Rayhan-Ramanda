x1 = input('Enter the x-coordinate from point1: ')
y1 = input('Enter the y-coordinate from point1: ')
x2 = input('Enter the x-coordinate from point2:')
y2 = input('Enter the y-coordinate from point2: ')

x1 = float(x1)
y1 = float(y1)
x2 = float(x2)
y2 = float(y2)

dy=y1-y2 
dx=x1-x2
slope=dy/dx

print 
print ("{0:.5f}".format(slope))
#Note : dont use minus again when putting second point if you want the second point remains as negative numbers

