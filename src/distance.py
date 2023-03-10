import math

def distance(Point,p1,p2,d):
    # Point = list of Points, p1 = titik 1, p2 = titik2, d = dimensi
    # Mengembalikan jarak, koordinat titik1, koordinat titik2
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

def bruteforce(Point,n,d):
    # Point = list of points, n = total titik, d = dimensi
    # Mengembalikan jarak terdekat, pasangan titik1 dan titik2 terdekat, banyak operasi distance
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

def quicksort(Point,low,high,d_now) :
    # Point = list of points, low = index awal, high = index akhir, d_now = dimensi sekarang
    # Mengembalikan list of points yang terurut membesar berdasarkan d_now
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

def checker (Point,min,d,p1,p2) :
    #Point = list of Points, min = jarak minimal, d = dimensi, p1 = titik1, p2 = titik2
    #Mengembalikan boolean apakah harus dicek jaraknya/tidak
    summ = 0
    flag = True
    for i in range (0,d) :
        if (summ<min**2):
            summ += (Point[p1][i]-Point[p2][i])**2
        else :
            flag = False
            break
    return flag

def closest(Point,min,d,idx1,idx2):
    # Point = list of Points, min = jarak minimal, d = dimensi, idx1 = titik1 min, idx2 = titik2 min
    # Mengembalikan jarak terdekat, pasangan titik1 dan titik2 jarak terdekat, jumlah pemanggilan distance
    hasil = []
    count = 0
    for j in range (0,len(Point)):
        for k in range (j+1,len(Point)):
            flag = True
            for i in range (0,d):
                if abs(Point[j][i] - Point[k][i])>min :
                    flag = False        
            if (flag) :
                flag2 = True
                if (d>3):
                    flag2 = checker(Point, min, d, j, k)
                if (flag2): 
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

def divide_conquer(Point,d,count):
    # Point = list of points, d = dimensi, count = banyak dipanggilnya distance
    # Mengembalikan jarak terdekat, pasangan titik1 dan titik2 jarak terdekat, jumlah pemanggilan distance
    # prekondisi: Point terurut membesar
    hasil = []
    countbrute = 0
    if (len(Point)>=2 and len(Point)<=3): # basis
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
    
    # cari jarak minimum di area left dan right (rekurens) 
    left = divide_conquer(PointLeft,d,count)
    right = divide_conquer(PointRight,d,count)
    if (left[0]<=right[0]):
        min = left[0]
        idx1 = left[1]
        idx2= left[2]
    else:
        min = right[0]
        idx1 = right[1]
        idx2= right[2]
     
    countleft = left[3]
    countright = right[3]
    
    # cari jarak terdekat di sekitar midpoint
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
