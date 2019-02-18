from numpy import *
import matplotlib.pyplot as plt
import random


# List of CMAPS to use in future versions
CMAPS = [
            'viridis', 'plasma', 'inferno', 'magma',
            'Greys', 'Purples', 'Blues', 'Greens', 'Oranges', 'Reds',
            'YlOrBr', 'YlOrRd', 'OrRd', 'PuRd', 'RdPu', 'BuPu',
            'GnBu', 'PuBu', 'YlGnBu', 'PuBuGn', 'BuGn', 'YlGn',
            'binary', 'gist_yarg', 'gist_gray', 'gray', 'bone', 'pink',
            'spring', 'summer', 'autumn', 'winter', 'cool', 'Wistia',
            'hot', 'afmhot', 'gist_heat', 'copper',
            'PiYG', 'PRGn', 'BrBG', 'PuOr', 'RdGy', 'RdBu',
            'RdYlBu', 'RdYlGn', 'Spectral', 'coolwarm', 'bwr', 'seismic',
            'Pastel1', 'Pastel2', 'Paired', 'Accent',
            'Dark2', 'Set1', 'Set2', 'Set3',
            'tab10', 'tab20', 'tab20b', 'tab20c',
            'flag', 'prism', 'ocean', 'gist_earth', 'terrain', 'gist_stern',
            'gnuplot', 'gnuplot2', 'CMRmap', 'cubehelix', 'brg', 'hsv',
            'gist_rainbow', 'rainbow', 'jet', 'nipy_spectral', 'gist_ncar'
            ]

def gaussian(x, mu=0,sigma=1):
    return (1/sqrt(2*pi*sigma**2))*exp(-((x-mu)**2)/(2*sigma**2))

def quad(x):
    return x**2

def inverse(x):
    return 1/x

def inverse_square(x):
    return 1/x**2

def cube(x):
    return x**3

def inverse_cube(x):
    return 1/x**3
while True:
    # List of functions that take one argument
    f_x = ['sin', 'cos', 'exp', 'sinh', 'cosh', 'quad', 'cube', 'inverse','inverse_square', 'inverse_cube'
            'tan','gaussian']
    expr = ''
    # Make an expression for the graph
    for i in range(random.randint(2, 12)):
        expr += random.choice(f_x)+random.choice(['(x) ','(y) '])+random.choice('+-*/')
    expr += '0'
    print(expr)

    def EVAL(x,y):
        return ( eval(expr)) 

    xx=linspace(-2,2,100)
    yy=linspace(-2,2,100)

    X,Y =meshgrid(xx,yy)

    Z = array([EVAL(i,j) for i in xx for j in yy]).reshape(100,100)

    plt.figure()
    plt.contourf(X,Y,Z,100, cmap='inferno')
    plt.xlabel(expr)
plt.show()
