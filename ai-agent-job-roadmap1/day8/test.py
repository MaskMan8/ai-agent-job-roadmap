while True:
    print("请输入一个数字")
    num = int(input())
    if num == 0:
        print("结束循环")
        break
    elif num < 0:
        print("跳过")
        continue
    else:
        print("")