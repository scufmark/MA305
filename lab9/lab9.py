#!/usr/bin/env python3
import numpy as np
import matplotlib.pyplot as plt

'''
=========================================
Piers Chapman - 20NOV18: Lab 9
Purpose: This lab receives an input from
two graphs and plots points according to
the data received.
=========================================
'''


#Get the slope
def slope(x,y,n):
	slope = 0
	x_sum = np.sum(x)
	y_sum = np.sum(y)
	xy_sum = 0
	x2_sum = 0
	for i in range(n):
		xy_sum += x[i]*y[i]
	for i in range(n):
		x2_sum += x[i]**2
	slope = ((n*xy_sum-x_sum*y_sum)/(n*x2_sum-((x_sum)**2)))
	return slope

#Determine the intercept
def intercept(x,y,m):
	y_bar = np.mean(y)
	x_bar = np.mean(x)
	return y_bar - m*x_bar

#Perform the sum of squares... thing
def sumSquares(x,y,p1,n):
	sum = 0
	for i in range(n):  
		z=np.polyval(p1,x[i])
		sum += (y[i]-z)**2
	return sum
#Get the standard error
def stdErr(s,n):
	return np.sqrt((s/(n-2)))
	
#Pull data from the file. Skip the first three rows.
x1,y1,x2,y2,x3,y3,x4,y4 = np.loadtxt('data9.txt',skiprows=3,unpack=True)

#plt.plot(x1,y1,'o')
#plt.show()

#Line of best fit
p1=np.polyfit(x1,y1,1)
p2=np.polyfit(x2,y2,1)
p3=np.polyfit(x3,y3,1)
p4=np.polyfit(x4,y4,1)


#Calculate and print data
print()
n = len(x1)
x1y1_slope = slope(x1,y1,n)
x1y1_inter = intercept(x1,y1,x1y1_slope)
x1y1_sumSq = sumSquares(x1,y1,p1,n)
x1y1_stdEr = stdErr(x1y1_sumSq,n)
print('x1y1 Slope:{0:2.5f} Intercept:{1:2.5f} Sum of Squares:{2:2.5f} StdError:{3:2.5f}'.format(x1y1_slope,x1y1_inter,x1y1_sumSq,x1y1_stdEr))


x2y2_slope = slope(x2,y2,n)
x2y2_inter = intercept(x2,y2,x2y2_slope)
x2y2_sumSq = sumSquares(x2,y2,p2,n)
x2y2_stdEr = stdErr(x2y2_sumSq,n)
print('x2y2 Slope:{0:2.5f} Intercept:{1:2.5f} Sum of Squares:{2:2.5f} StdError:{3:2.5f}'.format(x2y2_slope,x2y2_inter,x2y2_sumSq,x2y2_stdEr))

x3y3_slope = slope(x3,y3,n)
x3y3_inter = intercept(x3,y3,x3y3_slope)
x3y3_sumSq = sumSquares(x3,y3,p3,n)
x3y3_stdEr = stdErr(x3y3_sumSq,n)
print('x3y3 Slope:{0:2.5f} Intercept:{1:2.5f} Sum of Squares:{2:2.5f} StdError:{3:2.5f}'.format(x3y3_slope,x3y3_inter,x3y3_sumSq,x3y3_stdEr))

x4y4_slope = slope(x4,y4,n)
x4y4_inter = intercept(x4,y4,x4y4_slope)
x4y4_sumSq = sumSquares(x4,y4,p4,n)
x4y4_stdEr = stdErr(x4y4_sumSq,n)
print('x4y4 Slope:{0:2.5f} Intercept:{1:2.5f} Sum of Squares:{2:2.5f} StdError:{3:2.5f}'.format(x4y4_slope,x4y4_inter,x4y4_sumSq,x4y4_stdEr))

print()

#GrApHiNg TiMe

z1=np.polyval(p1,x1)
fig=plt.figure()
plt.plot(x1,y1,'o',x1,z1,'-')
plt.legend(['Data','Line of Best Fit'],loc='best')
plt.title('Least squares fit of a straight line for data set A')
plt.xlabel('$X_1$')
plt.ylabel('$Y_1$')
plt.show()
fig.savefig('figure_1.pdf')


z2=np.polyval(p2,x2)
fig=plt.figure()
plt.plot(x2,y2,'o',x2,z2 ,'-')
plt.legend(['Data','Line of Best Fit'],loc='best')
plt.title('Least squares fit of a straight line for data set A')
plt.xlabel('$X_2$')
plt.ylabel('$Y_2$')
plt.show()
fig.savefig('figure_2.pdf')


z3=np.polyval(p3,x3)
fig=plt.figure()
plt.plot(x3,y3,'o',x3,z3 ,'-')
plt.legend(['Data','Line of Best Fit'],loc='best')
plt.title('Least squares fit of a straight line for data set A')
plt.xlabel('$X_3$')
plt.ylabel('$Y_3$')
plt.show()
fig.savefig('figure_3.pdf')


z4=np.polyval(p4,x4)
fig=plt.figure()
plt.plot(x4,y4,'o',x4,z4,'-')
plt.legend(['Data','Line of Best Fit'],loc='best')
plt.title('Least squares fit of a straight line for data set A')
plt.xlabel('$X_4$')
plt.ylabel('$Y_4$')
plt.show()
fig.savefig('figure_4.pdf')
