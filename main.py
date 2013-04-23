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



def initial_u(x,t, u0, u1):
    """
     the u function only at time t = 0
     x - x value
     t-  time value
     uo - initial boundary condition u(0, t)
     u1 - initial boundary condition u(1,t)
    """
    if (x == 0):
        return u0
    elif (x == 1):
        return u1
    else:
        return f(x) # we know u(x,0) = f(x)

def u(x,t):
    """
        The exact solution to the model problem for n=1
        u(x,t) = exp(-pi^2 * t) * sin(pi * x)
    """
    return exp(-pi * pi * t) * sin(pi * x)


def print_x_pts(x_pts):
    """
        Debug method.
        Outputs all values in array.
    """
    size = len(x_pts)
    for i in range(size):
        print "%d/%d %f" % (i,size, x_pts[i])

def print_two_x_pts(x_pts, x_pts2):
    """
        Debug method.
        Outputs all points in two arrays side by side.
    """
    size = len(x_pts)
    print "x_pts = %d | %d" %(len(x_pts), len(x_pts2))
    for i in range(size):
        if (x_pts[i] < 0 or x_pts2[i] < 0):
            print "%d/%d %f | %f" % (i,size, x_pts[i], x_pts2[i])
def get_starting_x_pts(h, sigma, u0, u1):
    """
        Gets the initial array of x-pts at time t=0
        h - x spacing being used.
        sigma - ratio of k/(h^2)
        u0 - initial boundary conditions value u(0,t)
        u1 - initial boundary conditions value u(1,t)
    """
    ans = []
    num_x_pts = int(ceil(1/ h))
    for i in xrange(num_x_pts + 1): # Plus one to include the very last x-point.
        x = i * h
        new_val = initial_u(x, 0, u0, u1)
        ans.append(new_val)
    return ans

def get_exact_x_pts(t,h):
    """ Gets the points as represented by the function f(x)
        h - x spacing being used
    """
    ans = []
    num_x_pts = int(ceil(1/h))
    for i in xrange(num_x_pts + 1): # Plus one to include the very last x-point
        x = i * h
        val = u(x,t)
        ans.append(val)
    return ans


def move_x_pts_forward(curr_x_pts, sigma, u0, u1):
    """
        Moves forward from the current line to the next one in time.
        curr_x_pts - all the values at the current time
        sigma - ratio of k/(h^2) where:
                    k = the delta/amount in time to go forwards by
                    h = the delta in x-pts (i.e. the x-spacing value).
        u0 - initial boundary conditions value u(0,t)
        u1 - initial boundary conditions value u(1,t)
    """
    num_x_pts = len(curr_x_pts)
    ans = []
    for i in xrange(num_x_pts):
        if  i == 0: # First Point is fixed by boundary condition u0
            ans.append(u0)
            continue
        if  i == num_x_pts - 1: # Last Point is also fixed by the boundary conition u1
            ans.append(u1)
            continue

        # We apply the formula for u(x, t+k) which lets us move forward in time
        # The exact formula is:
        #   x(x,t+k) = sigma*u(x+h,t) + (1-2*sigma)*u(x,t) + sigma*u(x-h,t)

        new_val = sigma*curr_x_pts[i+1] + (1-2*sigma)*curr_x_pts[i] + sigma*curr_x_pts[i-1]
        ans.append(new_val)
    return ans

def plot_x_pts(y_points, h, fname, curr_step, autolimit=False, show=False):
    """
        Plots the given Points and saves it to a file with given name.
    """
    size = len(y_points)
    x_points = []
    for i in range(size):
        val = i * h
        x_points.append(val)

    fig = figure()
    fig.suptitle('Visualizing Temperatures at %s' % (str(curr_step)), fontsize=14, fontweight='bold')
    plt.xlabel('X - Space')
    plt.ylabel('U - Temperature')
    if autolimit == False:
        plt.ylim([-1.0,1.0])
    plt.plot(x_points, y_points, 'ro')
    if show:
        plt.show()
    else:
        fig.savefig('%s' % fname)


def plot_pts(pts, h, t):
    plot_x_pts(pts, h, "", t, True)

def simulate(h, k, run_time, u0, u1):
    """
        Solves the PDE for a vibrating string by using the explicit method.
        It returns all the y-values of the string throughout duration specified.

        run_time - For How Long we are supposed simulate the string motion. It should be an integer > 0.
        h - the delta in x-points (i.e. the x-point spacing) to be used.
        k - the delta in time. (i.e. how much we go ahead in time in one step).
        u0 - initial boundary conditions value u(0,t)
        u1 - initial boundary conditions value u(1,t)
    """
    num_steps_forward = int(ceil(run_time / k))
    pts_array = []
    sigma  = k / (h * h)
    initial_x_pts = get_starting_x_pts(h, sigma, u0, u1)


    print "sigma = %f" % sigma

    pts_array.append(initial_x_pts)

    for i in xrange(num_steps_forward):
        curr_x_pts = pts_array[i]
        new_x_pts = move_x_pts_forward(curr_x_pts, sigma, u0, u1)
        pts_array.append(new_x_pts)

    return pts_array


def get_diff_vector(a1, a2):
    """
        Gets absolute vector difff between two arrays
        a1 - array 1
        a2 - array 2
        Array must have the same length.
    """
    ans = []
    if len(a1) != len(a2):
        print ("Length of errors not equal. quitting")
        exit(-1)
    for i in xrange(len(a1)):
        diff = abs(a1[i] - a2[i])
        ans.append(diff)
    return ans

def get_vector_norm(vector):
    total = 0
    for i in vector:
        total += i * i
    return sqrt(total)


def do_required_plots(all_pts, times, run_time, h, k):
    num_steps = int(ceil(run_time / k))
    counter = 0
    for t in times:
        t_stepno = int(ceil( (float(t)/run_time) * num_steps))
        pts = all_pts[t_stepno]
        fname = "required_graph%d.png" % counter
        fname2 = "required_graph_autoscale%d.png" % counter
        title = "time t = %f" % t
        print "Plotting required graph %d" % counter
        plot_x_pts(pts, h, fname, title)
        plot_x_pts(pts, h, fname2, title, True)
        counter += 1

def compute_errors(all_pts, times, run_time, h, k):
    """
        all_pts - array with all points at all computed times
        times - the times to coompute the error.
        run_time - total run time of system.
        h - delta in space
        k - delta in time
    """

    num_steps = int(ceil(run_time / k))
    ans = []
    for t in times:
        t_stepno = int(ceil( (float(t)/run_time) * num_steps))
        computed_xs = all_pts[t_stepno]
        exact_xs = get_exact_x_pts(t, h)
        diff_xs = get_diff_vector(computed_xs, exact_xs)
        err_norm = get_vector_norm(diff_xs)
        ans.append(err_norm)
    return ans


def do_all_plots(points, h, graph_rate):
    counter = 0
    graph_counter  = 1
    print 'Graph Rate = %d' % graph_rate
    for x_pts in points:
        if counter % graph_rate == 0:
            print "Plotting graph # %d" % graph_counter
            fname = "graph%d.png" % graph_counter
            fname2 = "graph_autoscale%d.png" % graph_counter
            title = "time step no %d" % counter
            plot_x_pts(x_pts, h, fname, title)
            plot_x_pts(x_pts, h, fname2, title, True)
            graph_counter += 1
        counter += 1

def do_main(h,k,run_time,graph_rate, u0, u1):
    """
        h - x-width
        k - time-width
        run_time - duration of simulation
        graph_rate - plot graph every "graph_rate" steps.
        u0 - initial boundary condition value u(0,t)
        u1 - initial boundary condition value u(1,t)
    """
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
    do_main(h,k,run_time,graph_rate, u0, u1)
    #main()