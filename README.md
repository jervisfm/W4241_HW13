Jervis Muindi   
Numerical Algorithms and Complexity    
April 2013
Homework 13

Introduction
============
This project contains code that implement a general purpose polynomial root-finding solver using both Newton iteration (with convergence of order 2) and a 3-point iteration given below: 

	x_(i+1) = x_i -u(x_i) + (u(x_i) * f(x_i - u(x_i))) / ( 2*f(x_i - u(x_i))  - f(x_i) )

where u(x_i) is defined as follows: 

	u(x_i) = f(x_i) / f'(x_i)



How to Run
==========
python main.py [x-width] [t-width] [total_time] [graph_rate]  
     x-width : amount of x-spacing between points   
     t-width: delta in time to be applied in a single step forward   
     total_time: amount of time be used in simulating the system   
     graph_rate: A graph should be drawn/plotted every "graph_rate" steps    


Example:    

`python main.py 0.01 0.01 2 10`   


Sample Output
============
Below is some sample output obtained from running the script. 




