import matplotlib.pyplot as plt
import numpy as np

def rect(x=0, y=0, dx=1, dy=1, **kwargs):
    CColor, CLabel, cMarker, CMs = kwargs.get('color'), kwargs.get('label'), kwargs.get('marker'), kwargs.get('ms')
    plt.plot([x, x+dx, x+dx, x, x], [y, y, y+dy, y+dy, y], colot=CColor, label=CLabel, marker=cMarker, ms=CMs)

def circle(x0=0, y0=0, R=1, pointNum=10000, **kwargs):
    CColor = kwargs.get('color')

    x = np.arange(-2*R + x0, 2*R + x0, 4*R/pointNum)
    y = np.arange(-2*R + y0, 2*R + y0, 4*R/pointNum)

    X, Y = np.meshgrid(x, y)
    fxy = (X - x0)**2 + (Y - y0)**2 - (R)**2

    plt.contour(X, Y, fxy, levels=[0], colors=CColor)

def ellipse(x0=0, y0=0, dx=1, dy=1, pointNum=10000, **kwargs):
    CColor = kwargs.get('color')

    x = np.arange(-2*dx + x0, 2*dx + x0, 4*dx/pointNum)
    y = np.arange(-2*dy + y0, 2*dy + y0, 4*dx/pointNum)

    X, Y = np.meshgrid(x, y)
    fxy = ((X-x0)**2)/(dx**2) + ((Y-y0)**2)/(dy**2)

    plt.contour(X, Y, fxy, levels=[1], colors=CColor)

if(__name__ == "__main__"):
    plt.axis('equal')
    plt.grid()
    #help(plt.contour)
    #rect(0, 0, 100, 20)
    #circle(10,5,10, 16)
    ellipse(10, 5, 10, 5, 16)
    plt.savefig("fig")