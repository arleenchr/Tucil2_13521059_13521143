import random

def pembentukan_titik(n,d):
    # randomizer titik
    Point = [[round(random.uniform(-100*(n//10+1),100*(n//10+1)), 2) for c in range (d)]for r in range (n)]
    #Point = [[random.randint(-100*(n//10),100*(n//10))for c in range (d)]for r in range (n)]
    return Point

def printPoint(P,d):
    # print point (x, y, z, ...)
    print("(", end='')
    for j in range (0,d):
        print(P[j], end = '')
        if (j != d-1):
            print(", ",end='')
    print(")", end='')

def inputPoint():
    # input banyak titik, dimensi, dan generate points
    n = int(input("Masukkan banyak titik: "))
    d = int(input("Masukkan dimensi: "))
    print('')
    
    # validasi input
    if (n<=1):
        print("Jarak terdekat tidak bisa dikalkulasi! Silakan masukkan kembali input paling sedikit 2 titik!\n")
        return inputPoint()
    elif (d<=0):
        print("Dimensi tidak valid! Silakan masukkan kembali input!\n")
        return inputPoint()
    else:
        Point = pembentukan_titik(n,d)
        # print points
        print("Generating points...")
        for i in range (0,n):
            print("Point ", (i+1), end='')
            printPoint(Point[i],d)
            print('')
        print('')
        
        hasil = []
        hasil.append(Point)
        hasil.append(n)
        hasil.append(d)
        return hasil