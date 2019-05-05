# e6.1CalPi.py
from random import *
from math import *
from time import *

Darts = 10000000000
hits = 0.0
clock()
for i in range(1, Darts+1):
    x, y = random(), random()
    dist = sqrt(x ** 2 + y ** 2)
    if dist <= 1.0:
        hits = hits + 1
pi = 4 * (hits/Darts)
print("PI值是{}.".format(pi))
print("运行时间是：{:5.5}s".format(clock()))