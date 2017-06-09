# Python3 编程第一步

#Fibonacci series:斐波那契数列
#两个元素的总和确定下一个元素

a,b=0,1
while b<100:
    print(b,end=",")
    a,b=b,a+b
#return    1,1,2,3,5,8,13,21,34,55,89,

#无限循环
#我们可以通过设置条件表达式永远不为false来实现无限循环，实例：

# var = 1
# while var == 1:
#     num = int(input('输入一个数字：'))
#     print('您输入的数字是：',num)
# print('Good Bye!')

#可以使用CTRL+C来退出当前的无限循环。
#无限循环在服务器上客户端的实时请求非常有用。



#while循环使用else语句
#在while...else在条件语句为false时执行else语句块：

count = 0
while count<5:
    print(count,'小于5')
    count+=1
else:
    print(count,'大于或等于5')



#range()函数
#如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列，例如：

for i in range(5):
    print(i,end='')
#return 01234

for i in range(5,9):
    print(i, end='')
#return 5678

for i in range(0,10,3):
    print(i,end='')
#return 0369

#可以结合range()和len()函数以遍历一个序列的索引，例如：
a = ['one','two','three']
for i in range(len(a)):
    print(i,a[i],end=',')
#return 0 one,1 two,2 three,



#使用内置enumerate函数进行遍历

#for index,item in enumerate(sequence):
#   process(index,item)

sequence = [12,34,12,23,67]
for i,j in enumerate(sequence):
    print(i,j)
#return
# 1 34
# 2 12
# 3 23
# 4 67

#pass语句
#Python pass是空语句，是为了保持程序结构的完整性。
#pass不做任何事情，一般用作占位语句：
# while True:
#     pass
