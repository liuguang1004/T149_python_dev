#需求1：从键盘输入自己的name , age  int ,money  float
#需求2：打印在控制台
name=input('姓名：')
age=int(input('年龄：'))
money=float(input('存款：'))
print('----------------------------')
print('姓名：%s'%name)
print('年龄：%d'%age)
print('存款：%.02f'%money)

#输出
print(' 我叫%s，今年%d岁，存款为%.02f'%(name,age,money))

print(' 我叫{}，今年{}岁，存款为{}'.format(name,age,money))