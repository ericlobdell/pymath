from pylab import plot, savefig

def plot_and_save():
    xs = [1,2,3]
    ys = [2,4,6]
    plot(xs,ys)
    savefig("c:\\temp\mygraph.png")

if __name__ == '__main__':
    plot_and_save();