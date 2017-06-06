'''
Draw the trajectory of a body in projectile motion
'''

from matplotlib import pyplot as plt
import math

def draw_graph(x,y):
    plt.plot(x,y)
    plt.xlabel('x-coordinate')
    plt.ylabel('y-coordinate')
    plt.title('Projectile motion of a ball')

def frange(start, final, interval):
    ns = []
    while start < final:
        ns.append(start)
        start += interval

    return ns

def draw_trajectory(u, theta):
    theta = math.radians(theta)
    g = 9.8

    # Time of flight
    t_flight = 2*u*math.sin(theta)/g
    # Find time intervals
    intervals = frange(0, t_flight, 0.001)

    # coords
    xs = []
    ys = []
    for t in intervals:
        xs.append(u*math.cos(theta)*t)
        ys.append(u*math.sin(theta)*t - 0.5*g*t*t)

    draw_graph(xs,ys)

if __name__ == '__main__':
    try:
        u = float(input("Enter initial velocity (m/s): "))
        theta = float(input("Enter the angle of projection (degrees): "))
    except ValueError:
        print("You entered invalid input")
    else:
        draw_trajectory(u,theta)
        plt.show()
