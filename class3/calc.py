#封装计算机相关的函数

#不使用封装
# a=100
# b=200
# c=a+b
# print(c)

#加法
def add(num1,num2):
    num3=num1+num2
    return  num3

#减法
def sub(num1,num2):
     num3=num1-num2
     return num3

print(add(1,2))
print(add(100,200))
print(add(200,300))
print(add(3,4))
print(add(5,6))
print(sub(200,100))
print(sub(5,4))