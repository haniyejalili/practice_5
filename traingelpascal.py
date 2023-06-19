n=int(input("please enter number of rows: "))

def tringelpascal(n):

    tringelpascal=[]

    for i in range(n):
        row=[]
        for j in range(0,i+1):
            row.append(1)
        tringelpascal.append(row)

    for i in range(2,n):
        for j in range(1,i):
            tringelpascal[i][j]=tringelpascal[i-1][j]+tringelpascal[i-1][j-1]

    for r in tringelpascal:
        for c in r:
            print(c,end='  ')
        print("")

tringelpascal(n)