# e3.1DayDayUp365.py
import math

dayup = math.pow((1+0.001),365)     # 提高
daydown = math.pow((1-0.001),365)   # 放任

print("向上：{:.2f},向下：{:.2f}".format(dayup,daydown))