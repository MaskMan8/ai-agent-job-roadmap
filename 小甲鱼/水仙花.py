for i in range(100,1001):
    sum = 0
    while True:
        sum = (i / 100)**3 + (i / 10)**3 + (i % 10)**3
        if sum == i:
            print(i, "是水仙花数")
