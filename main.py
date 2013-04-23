from math import ceil, pi, sin, exp, sqrt

import sys



__author__ = 'Jervis Muindi'
# Date: April 2013
# Numerical Analysis and Algorithms
# Homework 13

def f(x):
    """
        The function we're finding roots for.
        You can change it something else (i.e. redefine it) if you'd like to solve a different problem.
        Remember to also update the df(x) derivative function as well.
    """
    return float((x ** 20) - 1)

def df(x):
    """
        This is the derivative of the function we're finding roots for
    """
    return float(20 * (x ** 19))


def next_x_netwon(x):
    """
        Finds the next number using netwon iteration formula
    """
    return x - (f(x) / df(x))

def u(x):
    """
        Ratio of f(x) and f'(x) - i.e. f(x) / f'(x)
    """
    return f(x) / df(x)

def next_point_iteration(x):
    """
        Finds the next number usign 3-point iteration Formula.

        3-point iteration is defined as follows:
	    x_(i+1) = x_i -u(x_i) + (u(x_i) * f(x_i - u(x_i))) / ( 2*f(x_i - u(x_i))  - f(x_i) )

        where u(x_i) is:
	        u(x_i) = f(x_i) / f'(x_i)
    """
    a = x
    b = u(x)
    numerator = u(x) * f(x - u(x))
    denominator = 2 * f(x - u(x)) - f(x)

    return a - b + numerator / denominator




def do_main(x0):
    """
        Main program code..
        x0 - initial x-point.
    """
    print 'Using Initial X-value : %s' % str(x0)
    print 'Finding Roots using both Newton Iteration and 3-point Iteration'
    x = 2
    print "f(%d) = %f | f'(%d) = %f" % (x, f(x), x, df(x))

    


def usage():
    print '**************'
    print 'General Root Solver : '
    print 'Usage: '
    print 'python main.py [x0]'
    print '     x0 : initial x-point to use.'
    print '\nExample: python main.py 0.98 \n'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def valid_inputs(x0):
    if not is_number(x0):
        'x-value must be a number : %s' % str(x0)
        return False
    else:
        return True

def main():
    arg_count = len(sys.argv) - 1
    if arg_count != 1:
        usage()
    else:
        x0 = sys.argv[1]
        if not valid_inputs(x0):
            print 'Invalid Input detected'
            print '************************'
            usage()
            exit(-1)
        else:
            do_main(x0)


if __name__ == '__main__':
    h = 10 ** (-1)
    #k = 0.5 * 10 ** (-2)
    k = h
    run_time = 1
    graph_rate = 10
    u0 = u1 = 0
    x0 = 0.98
    do_main(x0)
    #main()