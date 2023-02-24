from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

def visualization(Point, n, d, Hasil1, Hasil2, min_distance):
    fig = plt.figure()
        
    if (d==2):
        ax = plt.axes()
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        
        for i in range (0,n):
            ax.scatter(Point[i][0], Point[i][1])
            ax.text(Point[i][0], Point[i][1], '%s' % (str(i)), size=8)
        
        # plot line between two closest points and print the distance between them
        Hasil_x = []
        Hasil_x.append(Hasil1[0])
        Hasil_x.append(Hasil2[0])
        Hasil_y = []
        Hasil_y.append(Hasil1[1])
        Hasil_y.append(Hasil2[1])
        ax.plot(Hasil_x,Hasil_y)
        ax.text((Hasil1[0]+Hasil2[0])/2,(Hasil1[1]+Hasil2[1])/2, 'distance = %s' % (str(round(min_distance,4))), size=6)
        
        plt.show()
        
    elif (d==3):
        ax = plt.axes(projection='3d')
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.set_zlabel('Z-axis')
        
        for i in range (0,n):
            ax.scatter(Point[i][0], Point[i][1], Point[i][2])
            ax.text(Point[i][0], Point[i][1], Point[i][2], '%s' % (str(i)), size=8)
        
        # plot line between two closest points and print the distance between them
        Hasil_x = []
        Hasil_x.append(Hasil1[0])
        Hasil_x.append(Hasil2[0])
        Hasil_y = []
        Hasil_y.append(Hasil1[1])
        Hasil_y.append(Hasil2[1])
        Hasil_z = []
        Hasil_z.append(Hasil1[2])
        Hasil_z.append(Hasil2[2])
        ax.plot(Hasil_x,Hasil_y,Hasil_z)
        ax.text((Hasil1[0]+Hasil2[0])/2,(Hasil1[1]+Hasil2[1])/2,(Hasil1[2]+Hasil2[2])/2, 'distance = %s' % (str(round(min_distance,4))), size=6)
        
        plt.show()