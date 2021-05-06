
age =18
money=12.88

# 格式化输出
print('我今年%d岁,我口袋里面有%f块钱。'%(age,money))

#自动类型转换   int -->float
print(age+money)
print('%.02f'%(age+money))

#强制类型转换 float-->int
print(age+int(money))

#把 list转set
list1=['a','a','b']
print(set(list1))