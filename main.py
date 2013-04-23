from math import ceil, pi, sin, exp, sqrt

try:
    import matplotlib.pyplot as plt
    from matplotlib.pyplot import figure
    import sys
except ImportError:
    print('Dependency MatplotLib Is Missing. Please Install it and try again Exiting ...')
    exit(-1)


__author__ = 'Jervis Muindi'
# Date: April 2013
# Numerical Analysis and Algorithms
# Homework 9

def f(x):
    """
        This is the function describing the initial state of system.
        You can change it something else (i.e. redefine it) if you'd like to solve a different problem.
    """
    return sin(pi * x)









def do_main(x0):
    """
        Main program code..
        x0 - initial x-point.
    """
    print 'Using Initial X-value : %s' % str(x0)
    print 'Simulating and Solving PDE System for duration of %s' % run_time
    print 'k (time-width) = %f' % k
    print 'h (x-width) = %f' % h
    print 'Run Time = %f ' % run_time
    print 'Graph rate = %f' % graph_rate
    pts_array = simulate(h,k,run_time, u0, u1)
    print "We did this many steps : %d " % len(pts_array)
    print "Plotting Results ..."
    do_all_plots(pts_array, h, graph_rate)

    times = [0.2, 0.4, 0.6, 0.8, 1.0]
    print "----------------------------"
    print "Plotting Required graphs..."
    do_required_plots(pts_array, times, run_time, h, k)
    print "All plots done"

    print 'Errors in Computed Approx Solution: '
    errors = compute_errors(pts_array, times, run_time, h, k)
    i = 0
    for err in errors:
        print "At t = %f, L2-norm of error vector is  %f " % (times[i], err)
        i += 1


def usage():
    print '**************'
    print 'Partial ODE solver and grapher for the model problem of a vibrating string: '
    print 'Usage: '
    print 'python main.py [x-width] [t-width] [total_time] [graph_rate] '
    print '     x-width : amount of x-spacing between points'
    print '     t-width: delta in time to be applied in a single step forward'
    print '     total_time: amount of time be used in simulating the system'
    print '     graph_rate: A graph should be drawn/plotted every "graph_rate" steps'
    print '\nExample: python main.py 0.01 0.01 2 10\n'
    print 'Note: 1) All input values should be positive numeric values. '
    print '      2) Graphing ability is dependent on MatplotLib being installed'

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def valid_inputs(h,k,total_time, graph_rate):
    if (not is_number(h) or h < 0):
        'h value must be a positive number : %s' % str(h)
        return False
    if (not is_number(k) or k < 0):
        'k value must be a positive number: %s' % str(k)
        return False
    if (not is_number(total_time) or total_time < 0):
        'Time T must be a positive number: %s' % str(total_time)
        return False
    if (not is_number(graph_rate) or graph_rate < 0) :
        'Graph Rate p must be a positive number: %s' % graph_rate
        return False
    return True

def main():
    arg_count = len(sys.argv) - 1
    if arg_count != 4:
        usage()
    else:
        h = sys.argv[1]
        k = sys.argv[2]
        total_time = sys.argv[3]
        graph_rate = sys.argv[4]
        if not valid_inputs(h,k,total_time,graph_rate):
            print 'Invalid Inputs detected'
            print '************************'
            usage()
            exit(-1)
        else:
            do_main(float(h),float(k),float(total_time),float(graph_rate))


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