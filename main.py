
#takes user input
#the 'int' makes every input an integer as apposed to a String (strings are simply text that cannot be used in math )
y1 = int(input('y1: '))
x1 = int(input('x1: '))
y2 = int(input('y2: '))
x2 = int(input('x2: '))

#normally you would just use one varible for this but i used 3 simply for compatability with older versions of python
SlopeY = y2-y1
print("SlopeY: ")
print(SlopeY)
SlopeX = x2-x1
print("SlopeX: ")
print(SlopeX)
#the final step to solving for slope and
Slope = SlopeY/SlopeX
#since we are solving for slope we are putting the b on the left side and letting python work its magic
b = y1-(Slope*x1)
print(b)
print"equation:  y = ","(",SlopeY,"/",SlopeX,")","X +",b
