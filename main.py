x1 = int(input('x1: '))
y1 = int(input('y1: '))
x2 = int(input('x2: '))
y2 = int(input('y2: '))

#slope intercept form (y=mx+b)
SlopeY = y2-y1
print("SlopeY: ")
print(SlopeY)
SlopeX = x2-x1
print("SlopeX: ")
print(SlopeX)
Slope = SlopeY/SlopeX
b = y1-(Slope*x1)
print("y-intercept: ",b)
print("equation:  y =","(",SlopeY,"/",SlopeX,")X+", b)

#mid point
mid_x = x2-x1
mid_y = y2-y1
print('midpoint:  ',  '(' , mid_x, '/2,' , mid_y, '/2 )' )
