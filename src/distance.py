import math
import random
import time
# import numpy as np
import visualizer

def distance(Point,p1,p2,d):
    sum = 0
    for i in range (0,d) :
        sum += (Point[p1][i]-Point[p2][i])**2
    return math.sqrt(sum)

def pembentukan_titik(n,d):
    Point = [[random.randint(0,100)for c in range (d)]for r in range (n)]
    return Point

def bruteforce(Point,n,d):
    hasil = []
    min = distance(Point,0,1,d)
    idx1 = 0
    idx2 = 1
    for i in range (0,n) :
        for j in range (i+1,n):
            temp = distance(Point,i,j,d)
            if temp<min :
                min = temp
                idx1 = i
                idx2 = j
    hasil.append(min)
    hasil.append(idx1)
    hasil.append(idx2)
    return hasil

def divide_conquer(Point,n,d):
    # prekondisi: Point terurut membesar
    hasil = []
    if (len(Point)>=2 & len(Point)<=3):
        return bruteforce(Point,n,d)
    
    mid = n//2
    # menghitung jarak titik-titik dekat perbatasan
    midpoint = (Point[mid-1][0]+Point[mid][0])/2 # titik tengah antara left & right
    PointLeft = [] # titik di area kiri
    PointRight = [] # titik di area kanan
    for i in range (0,len(Point)):
        if Point[i][0] <= midpoint:
            PointLeft.append(Point[i])
        else:
            PointRight.append(Point[i])
    
    # find minimum distance in left & right area (rekurens) 
    left = divide_conquer(PointLeft,mid,d)
    right = divide_conquer(PointRight,mid,d)
    
    if (left[0] < right[0]):
        min = left[0]
        idx1 = left[1]
        idx2 = left[2]
    else:
        min = right[0]
        idx1 = right[1]
        idx2 = right[2]
    #min = distance(Point,left[0],right[0],d) # cari jarak minimum
    
    # find minimum distance near midpoint
    PointCenter = []
    for i in range (0,len(PointLeft)):
        if abs(PointLeft[i][0] - midpoint) <= min:
            PointCenter.append(PointLeft[i])
    for i in range (0,len(PointRight)):
        if abs(PointRight[i][0] - midpoint) <= min:
            PointCenter.append(PointRight[i])
    
    center = divide_conquer(PointCenter,len(PointCenter),d)
    
    if center[0] < min:
        min = center[0]
        idx1 = center[1]
        idx2 = center[2]
    
    '''
    idx1 = left
    idx2 = right
    dummy = []
    for a in Point: # list Point yang dekat midpoint
        if abs(a[0] - midpoint)<min:
            dummy.append(a)
    panjang = len(dummy)
    for i in range (0,panjang) :
        for j in range (i+1,panjang):
            temp = distance(dummy,i,j,d)
            if temp<min :
                min = temp
                idx1 = i
                idx2 = j
    '''
    hasil.append(min)
    hasil.append(idx1)
    hasil.append(idx2)
    return hasil

def printPoint(P,d):
    print("(", end='')
    for j in range (0,d):
        print(P[j], end = '')
        if (j != d-1):
            print(",",end='')
    print(")", end='')

def main() :
    n = int(input("Masukkan banyak titik : "))
    d = int(input("Masukkan dimensi : "))
    print('\n')
    Point = pembentukan_titik(n,d)
    
    print("Generating points...\n")
    
    for i in range (0,n):
        print("Point", (i+1), end='')
        printPoint(Point[i],d)
        print('')
    
    start = time.time()
    Hasil = bruteforce(Point,n,d)
    end = time.time()
    print("Jarak terdekat adalah titik " + str(Hasil[1]), end=' ')
    printPoint(Point[Hasil[1]],d)
    print(" dan " + str(Hasil[2]), end=' ')
    printPoint(Point[Hasil[2]],d)
    print(" dengan jarak " + str(Hasil[0]))
    print("Waktu ekskusi:", (end-start) * 10**3, "ms")
    
    start = time.time()
    Hasil2 = divide_conquer(Point,n,d)
    end = time.time()
    print("Jarak terdekat adalah titik " + str(Hasil[1]), end=' ')
    printPoint(Point[Hasil[1]],d)
    print(" dan " + str(Hasil[2]), end=' ')
    printPoint(Point[Hasil[2]],d)
    print(" dengan jarak " + str(Hasil[0]))
    print("Waktu ekskusi:", (end-start) * 10**3, "ms")
    
    visualizer.visualization(Point,n,d)
    
main()
