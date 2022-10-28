a = float(input("Enter coordinates of 1 vertex: "))
b = float(input("Enter coordinates of 2 vertex: "))
c = float(input("Enter coordinates of 3 vertex: "))
P = a + b + c
pp = P/2
S = (pp*(pp-a)*(pp-b)*(pp-c))**0.5
print('Square',S,'Perimeter',P)