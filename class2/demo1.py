#不借助临时，交换2个变量，使用2中方法
# 方法1：
# a=10
# b=20
# print('交换前：',a,b)
# a,b=b,a
# print('交换后：',a,b)

# 方法2:
a=20
b=10
print('交换前：',a,b)
a=a+b
b=a-b
a=a-b
print('交换后：',a,b)
