#Assignment-01 By Md.Shafiul Haque Johny Id:011171319

n = int(input())
#n = 9
for i in range(1, n+1):
    number = 1
    for j in range(n, 0, -1):
        if j > i:
            print(" ", end=' ')
        else:
            print(number, end=' ')
            number +=1
    print("")