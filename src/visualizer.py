from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def visualization(Point, n, d):
    fig = plt.figure()
        
    if (d==2):
        ax = plt.axes()
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        
        for i in range (0,n):
            ax.scatter(Point[i][0], Point[i][1])
            ax.text(Point[i][0], Point[i][1], '%s' % (str(i)), size=8)
        plt.show()
        
    elif (d==3):
        ax = plt.axes(projection='3d')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        
        for i in range (0,n):
            ax.scatter(Point[i][0], Point[i][1], Point[i][2])
            ax.text(Point[i][0], Point[i][1], Point[i][2], '%s' % (str(i)), size=8)
        plt.show()