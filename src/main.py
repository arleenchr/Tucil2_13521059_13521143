import time
import IO_processing
import visualizer
import distance

def main() :
    # Program Utama
    # Proses input
    IOresult = IO_processing.inputPoint()
    Point = IOresult[0]
    Pointdiv = Point.copy()
    n = IOresult[1]
    d = IOresult[2]
    
    # solve by brute force
    start = time.time()
    Hasil = distance.bruteforce(Point,n,d)
    end = time.time()
    print("Dengan strategi algoritma Brute Force,\npasangan titik terdekat adalah titik ", end='')
    IO_processing.printPoint(Hasil[1],d)
    print(" dan titik ", end='')
    IO_processing.printPoint(Hasil[2],d)
    print(" dengan jarak %.4f" % (Hasil[0]))
    print("Waktu eksekusi:", (end-start)*1000, " ms")
    print("Banyak operasi: " + str(Hasil[3]))
    
    print("")
    
    # solve by divide and conquer
    start = time.time()
    Point2 = distance.quicksort(Pointdiv,0,len(Point)-1,0)
    Hasil = distance.divide_conquer(Point2,d,0)
    end = time.time()
    print("Dengan strategi algoritma Divide and Conquer,\npasangan titik terdekat adalah titik ", end='')
    IO_processing.printPoint(Hasil[1],d)
    print(" dan titik ", end='')
    IO_processing.printPoint(Hasil[2],d)
    print(" dengan jarak %.4f" % (Hasil[0]))
    print("Waktu eksekusi:", (end-start)*1000, " ms")
    print("Banyak operasi: " + str(Hasil[3]))
    
    # visualizer
    visualizer.visualization(Point,n,d,Hasil[1],Hasil[2],Hasil[0])
    
main()