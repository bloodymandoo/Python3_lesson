# Python3迭代器与生成器

#迭代器
#迭代是Python最强大的功能之一，是访问集合元素的一种方式。
#迭代器是一个可以记住遍历的位置的对象。
#迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。
#迭代器只能往前不会后退。
#迭代器有两个基本的方法：iter()和next()。
#字符串，列表或元组对象都可用于创建迭代器：

list = [1,2,3,4]
it = iter(list)
print(it)               #return  <list_iterator object at 0x00000205F3BBB208>
print(next(it))         #return  1
print(next(it))         #return  2

#迭代器对象可以使用常规for语句进行遍历：

list = [1,2,3,4]
it = iter(list)
for x in it:
    print(x,end=",")    #return  1,2,3,4,

#也可以使用next()函数：
# import sys          #引入sys模块
#
# list = [1,2,3,4]
# it = iter(list)
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()
#return
# 1
# 2
# 3
# 4




#生成器

#在Python中，使用了yield的函数被称为生成器（generaotr）。
#跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
#在调用生成器运行的过程中，每次遇到yield函数会暂停并保存当前所有的运行信息，返回yield的值。并在下一次执行next()
#方法时从当前位置继续运行。

#以下实例使用yield实现斐波那契数列：

import sys

def fibonacci(n):               #生成器函数 - 斐波那契
    a,b,counter=0,1,0
    while True:
        if(counter>n):
            return
        yield a
        a,b = b,a+b
        counter += 1
f = fibonacci(10)               #f是一个迭代器，由生成器返回生成

while True:
    try:
        print(next(f),end=" ")
    except StopIteration:
        sys.exit()
#return  0 1 1 2 3 5 8 13 21 34 55
