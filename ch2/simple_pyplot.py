'''
Simple plot using pyplot
'''

import matplotlib.pyplot as plt

def create_graph():
    xs = [1,2,3]
    ys = [2,4,6]
    plt.plot(xs,ys)
    plt.show()

if __name__ == '__main__':
    create_graph()
