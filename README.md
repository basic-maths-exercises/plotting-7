# Vectorized functions

In the last exercise, you should have seen how the `np.linspace` function makes generating the array of x-values for our graph much simpler.  You will have written a program like the one shown on the left here and thus reduced the number of lines of code down from 8 to 7.  In this exercise,  you are going to learn how to reduce the number of lines of codes further by focussing on how the array of y-values is computed.  In other words, we are going to consider this bit of code:

````
yvalues = np.zeros(500)
for i in range(500) : yvalues[i] = np.sin( xvalues[i] )
````

The reason why we have to write a for loop to compute all the sine values here is hopefully obvious.  Sine is a function of a single real variable so we cannot pass an array of values to this function and get a result that is meaningful.  What would it mean to take the "sine" of a list of numbers?  Well, let's try it.  Replace the code in the cell on the left with the following code:

````
import matplotlib.pyplot as plt
import numpy as np

xvalues = np.linspace( -np.pi, np.pi, 500 )
yvalues = np.sin(xvalues)

plt.plot( xvalues, yvalues, "k-" )
plt.savefig( "sine.png" )
````

Given what you know about the sine function and the output that the code above produces what does `np.sin` do when an array of angles is passed to it? 

To complete the exercise use what you have learned to write a program to plot the sine, the cosine and the tangent of x as a function of x for x in the range from ![](https://render.githubusercontent.com/render/math?math=-2\pi) to ![](https://render.githubusercontent.com/render/math?math=%2B2\pi).   You should NOT need to write any for loops in your function.  You should use a continuous line to draw the curves and 1000 grid points.  The first of these gridpoints should be at ![](https://render.githubusercontent.com/render/math?math=-2\pi) and the last of them should be at ![](https://render.githubusercontent.com/render/math?math=%2B2\pi).

------
A word of caution here: numpy functions act on matrices in a way that is different to the way we might express things in mathematics.  As an example, if A is a matrix and we write exp(A) (i.e. take the exponential of A) in a mathematical proof we CANNOT achieve the same result by doing np.exp(A), where A is a matrix in python.  This distinction is somewhat beyond the scope of this module but it is important to bear in mind in future.   
