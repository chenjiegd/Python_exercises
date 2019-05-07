print("Hello world！")

r = 5
s = 3.141*r * r
print(s)

print("{2} {1} {0} {1}".format("hello", "world","miky"))

list1 = ['馒头研究院','www.mindtour.cn']
list2 = ['Thimbo','www.thimbbo.com']
list3 = [list1, list2]
print("公司名：{0[0]}，网址：{0[1]}".format(list1))
print("公司名：{0[0]}，网址：{0[1]}".format(list2))
print("公司名：{0[0][0]}".format(list3))

