 
def chess(n, m):
    for i in range(n):
        for j in range(m):
            if (i + j) % 2 == 0:
                print("⬛️", end="")
            else:
                print("⬜️", end="")
        print()

n = int(input(" width : "))
m = int(input(" length : "))

chess(n, m)
