a = 0
b = 1
while a < 1000:     # 输出不大于1000的数列
    print(a,end=',')
    a, b = b, a + b