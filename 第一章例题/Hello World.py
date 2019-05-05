print('hello world')
print('祖国，你好')

classmate = ['Michael','Bob',"Tina"]

print(classmate)
print(len(classmate))

print(classmate[0])
print(classmate[1])
print(classmate[2])
print(classmate[-1])
print(classmate[-2])
print(classmate[-3])

classmate.append('Ada') #在list中追加元素到末尾
print(classmate)
print(len(classmate))

classmate.insert(1,'jack') #把元素插入到指定的位置（索引号为1的位置）
print(classmate)
print(len(classmate))

classmate.pop()
print(classmate)
print(len(classmate))

classmate.pop(0)
print(classmate)
print(len(classmate))

classmate[0] = 'Nancy'
print(classmate)
print(len(classmate))