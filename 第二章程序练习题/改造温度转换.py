# e1.4TempConvert.py
# TempStr = input("请输入带有符号的温度值：")
if input("请输入带有符号的温度值：")[-1] in ['F','f']:
    C = (eval(input("请输入带有符号的温度值：")[0:-1])-32)/1.8
    print("转换后的温度是{:.2f}C".format(C))
elif TempStr[-1] in ['C','c']:
    F = eval(TempStr[0:-1])*1.8+32
    print("转换后的温度是{:.2f}F".format(F))
else:
    print("输入的温度不正确。")
