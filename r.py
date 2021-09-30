i=1
for i in range(i,6):
    n=i
    print(i, end=" ")
    for j in range(1,i):
        c=1
        for k in range(4,0,-1):
            n=n+k
            print(n, end=" ")
            c=c+1
            if (c==i):
                break
        break
    print("\n")
            
        
