#三目运行符
#练习1
# a=10
# b=20
#
# max= a if a>b else b
# print(max)

# 练习2： 有3个数，使用一行代码求最大值，提示：使用三目运行符
a=30
b=10
c=20

# max= a if a>b else b
# max2=max if max >c else c

max2=(a if a>b else b) if (a if a>b else b) >c else c
print(max2)
