import math
import time
# import numpy as np
import IO_processing
import visualizer

def distance(Point,p1,p2,d):
    sum = 0
    for i in range (0,d) :
        sum += (Point[p1][i]-Point[p2][i])**2
    return math.sqrt(sum)

def bruteforce(Point,n,d):
    hasil = []
    count = 0
    min = distance(Point,0,1,d)
    count +=1
    idx1 = 0
    idx2 = 1
    if (n>=3) :
        for i in range (0,n) :
            for j in range (i+1,n):
                if(i!= 0 or j!=1):
                    temp = distance(Point,i,j,d)
                    count +=1
                    if temp<min :
                        min = temp
                        idx1 = i
                        idx2 = j
    hasil.append(min)
    hasil.append(idx1)
    hasil.append(idx2)
    hasil.append(count)
    return hasil

def quicksort(Point,low,high,d_now) :
    if low<high :
        pivot = Point[high][d_now]
        i = low -1
        for j in range (low,high):
            if Point[j][d_now]<=pivot:
                i +=1
                (Point[i],Point[j]) = (Point[j],Point[i])
        (Point[i+1],Point[high]) = (Point[high],Point[i+1])
        pi = i+1

        quicksort(Point,low,pi-1,d_now)
        quicksort(Point,pi+1,high,d_now)
    return Point

def closest(Point,min,d):
    hasil = []
    count = 0
    idx1 = 0
    idx2 = 1
    for j in range (0,len(Point)):
        for k in range (j+1,len(Point)):
            flag = True
            for i in range (0,d):
                if abs(Point[j][i] - Point[k][i])>min :
                    flag = False
            if (flag) :
                count +=1
                temp = distance(Point,j,k,d)
                if (temp<min) :
                    min = temp
                    idx1 = j
                    idx2 = k
                    

    hasil.append(min)
    hasil.append(idx1)
    hasil.append(idx2)
    hasil.append(count)
    return hasil

def divide_conquer(Point,d,count):
    # prekondisi: Point terurut membesar
    hasil = []
    countbrute = 0
    if (len(Point)>=2 and len(Point)<=3):
        if (len(Point)==2):
            countbrute=1
        else :
            countbrute=3
        return bruteforce(Point,len(Point),d)
    
    mid = len(Point)//2
    # menghitung jarak titik-titik dekat perbatasan
    midpoint = (Point[mid-1][0]+Point[mid][0])/2 # titik tengah antara left & right
    
    PointLeft = Point[:mid]
    PointRight = Point[mid:]
    
    # find minimum distance in left & right area (rekurens) 
    left = divide_conquer(PointLeft,d,count)
    right = divide_conquer(PointRight,d,count)
    if (left[0]<=right[0]):
        min = left[0]
        idx1 = left[1]
        idx2= left[2]
    else :
        min = right[0]
        idx1 = right[1]
        idx2= right[2]
     
    countleft = left[3]
    countright = right[3]
    #min = distance(Point,left[0],right[0],d) # cari jarak minimum
    
    # find minimum distance near midpoint
    Pointcenter = []
    for i in range (0,len(PointLeft)):
        if abs(PointLeft[i][0] - midpoint)<=min :
            Pointcenter.append(PointLeft[i])
    for i in range (0,len(PointRight)):
        if abs(PointRight[i][0] - midpoint)<=min :
            Pointcenter.append(PointRight[i])
    minbaru = closest(Pointcenter,min,d)
    if (minbaru[0]<min):
        min = minbaru[0]
        idx1= minbaru[1]
        idx2= minbaru[2]
    
    countminbaru= minbaru[3]
    count = count + countleft + countright + countbrute + countminbaru
    
    hasil.append(min)
    hasil.append(idx1)
    hasil.append(idx2)
    hasil.append(count)
    return hasil

def main() :
    IOresult = IO_processing.inputPoint()
    Point = IOresult[0]
    n = IOresult[1]
    d = IOresult[2]
    Point2 = quicksort(Point,0,len(Point)-1,0)
    
    # solve by brute force
    start = time.time()
    Hasil = bruteforce(Point,n,d)
    end = time.time()
    print("Jarak terdekat adalah titik " + str(Hasil[1]), end=' ')
    IO_processing.printPoint(Point[Hasil[1]],d)
    print(" dan " + str(Hasil[2]), end=' ')
    IO_processing.printPoint(Point[Hasil[2]],d)
    print(" dengan jarak " + str(Hasil[0]))
    print("Waktu ekskusi:", (end-start) * 10**3, "ms")
    print ("Banyak operasi " + str(Hasil[3]))
    
    # solve by divide and conquer
    start = time.time()
    Hasil2 = divide_conquer(Point2,d,0)
    end = time.time()
    print("Jarak terdekat adalah titik " + str(Hasil[1]), end=' ')
    IO_processing.printPoint(Point[Hasil[1]],d)
    print(" dan " + str(Hasil[2]), end=' ')
    IO_processing.printPoint(Point[Hasil[2]],d)
    print(" dengan jarak " + str(Hasil[0]))
    print("Waktu ekskusi:", (end-start) * 10**3, "ms")
    print ("Banyak operasi " + str(Hasil[3]))
    
    # visualizer
    visualizer.visualization(Point,n,d,Point[Hasil[1]],Point[Hasil[2]],Hasil[0])
    
main()
