import matplotlib.pyplot as plt

def square(x=1, y=1):
    plt.plot([x, x+4, x+4, x, x],[y, y, y+4, y+4, y], marker='o')
    plt.axis('equal')
    plt.savefig('task_1.png')

if(__name__ == '__main__'):
    square()