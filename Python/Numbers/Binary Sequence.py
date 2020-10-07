# Date - 0ct 7, 2020 By Jatin Sharma

for i in range(int(input())):
    
    x,y,a,b = map(int,input().split())

    if(x*y == a+b):
        print("Yes")
    else:
        print("No")