tn=0
un=1
h=0.1
for i in range(10):
    un = un + 4 * h * tn * un **1/2
    tn = tn + h
    print(un)
     









tn = 0
un = 1
h =0.1
for i in range(10):
    un = un + 4 * tn * h * un ** 1/2
    vn = (1 + tn ** 2) **2
    tn = tn + h
    wn = abs (un - vn)
    print(un, wn)


    

