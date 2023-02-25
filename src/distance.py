import math
import time
# import numpy as np
import IO_processing
import visualizer

def distance(Point,p1,p2,d): #Point = list of Point, p1 = titik 1, p2 = titik2, d = dimensi
    #Kembaliin jarak, koordinat titik1, koordinat titik2
    sum = 0
    idx1 = []
    idx2 = []
    hasil = []
    for i in range (0,d) :
        sum += (Point[p1][i]-Point[p2][i])**2
        idx1.append(Point[p1][i])
        idx2.append(Point[p2][i])
    hasil.append(math.sqrt(sum))
    hasil.append(idx1)
    hasil.append(idx2)
    return hasil

def bruteforce(Point,n,d):#Point = list of point, n = total titik, d = dimensi
    #kembaliin jarak terdekat, titik1 terdekat, titik2 terdekat, banyak operasi distance
    hasil = []
    count = 0
    minlist = distance(Point,0,1,d)
    min = minlist[0]
    count +=1
    idx1 = minlist[1]
    idx2 = minlist[2]
    if (n>=3) :
        for i in range (0,n) :
            for j in range (i+1,n):
                if(i!= 0 or j!=1):
                    temp = distance(Point,i,j,d)
                    count +=1
                    if temp[0]<min :
                        min = temp[0]
                        idx1 = temp[1]
                        idx2 = temp[2]
    hasil.append(min)
    hasil.append(idx1)
    hasil.append(idx2)
    hasil.append(count)
    return hasil

def quicksort(Point,low,high,d_now) : #Point = list of point, low = index awal, high = index akhir, d_now = dimensi sekarang
    #Kembaliin list of point terurut dari kecil berdasarkan d_now
    # pi = pivot
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

def closest(Point,min,d,idx1,idx2):#Point = list of Point, min = jarak minimal,d = dimensi, idx1 = titik1 min, idx2 = titik2 min
    #Kembaliin jarak terdekat, titik1 jarak terdekat, titik2 jarak terdekat, jumlah pemanggilan distance
    hasil = []
    count = 0
    for j in range (0,len(Point)):
        for k in range (j+1,len(Point)):
            flag = True
            for i in range (0,d):
                if abs(Point[j][i] - Point[k][i])>min :
                    flag = False
            if (flag) :
                count +=1
                temp = distance(Point,j,k,d)
                if (temp[0]<min) :
                    min = temp[0]
                    idx1 = temp[1]
                    idx2 = temp[2]
                    

    hasil.append(min)
    hasil.append(idx1)
    hasil.append(idx2)
    hasil.append(count)
    return hasil

def divide_conquer(Point,d,count):#Point = list of point, d = dimensi, count = banyak dipanggilnya distance
    #Kembaliin jarak terdekat, titik1 jarak terdekat, titik2 jarak terdekat, jumlah pemanggilan distance
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
    minbaru = closest(Pointcenter,min,d,idx1,idx2)
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
    Pointdiv = Point.copy()
    n = IOresult[1]
    d = IOresult[2]
    
    # solve by brute force
    start = time.time()
    Hasil = bruteforce(Point,n,d)
    end = time.time()
    print("Jarak terdekat adalah titik ", end=' ')
    IO_processing.printPoint(Hasil[1],d)
    print(" dan ", end=' ')
    IO_processing.printPoint(Hasil[2],d)
    print(" dengan jarak " + str(Hasil[0]))
    print("Waktu ekskusi:", (end-start) * 10**3, "ms")
    print ("Banyak operasi " + str(Hasil[3]))
    
    # solve by divide and conquer
    start = time.time()
    Point2 = quicksort(Pointdiv,0,len(Point)-1,0)
    Hasil = divide_conquer(Point2,d,0)
    end = time.time()
    print("Jarak terdekat adalah titik ", end=' ')
    IO_processing.printPoint(Hasil[1],d)
    print(" dan ", end=' ')
    IO_processing.printPoint(Hasil[2],d)
    print(" dengan jarak " + str(Hasil[0]))
    print("Waktu ekskusi:", (end-start) * 10**3, "ms")
    print ("Banyak operasi " + str(Hasil[3]))
    
    # visualizer
    visualizer.visualization(Point,n,d,Hasil[1],Hasil[2],Hasil[0])
    
main()
