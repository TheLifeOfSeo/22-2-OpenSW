
t = 10
a = [9, 15, 54, 369, 634, 1053, 2954, 4234, 5424, 9531]
b = [2, 6, 6, 15, 20, 34, 50, 89, 123, 9999]

for i in range(0, int(t)) :
    print("%d] %d %d" % (i+1, a[i]//b[i], a[i]%b[i]))

#정답