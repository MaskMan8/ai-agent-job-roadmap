n = 2
while n < 10:
    x = 2
    while x < n:
        if n % x == 0:
            print(n, "=", x, "*", n // x)
            break
        x += 1
    else:
        print(n, "是素数")
    n += 1
