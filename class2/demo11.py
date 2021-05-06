#is 练习：判断二个变量是否为同一个对象， 是否指向同一个内存地址
stu_list=['王利利',24,88888.88]
print(id(stu_list))

#地址传递
stu2_list=stu_list
print(id(stu2_list))
#is 运算
if stu_list is stu2_list:
    print('A is B')
else :
    print('A is not  B')

#值传递，再开辟一个空间存放数据
c=stu_list[:]  #切片  没头没尾就是全部复制
print(id(c))  #查看内存地址
if c is stu_list:
    print( 'C is A')
else:
    print('C is not A')

# 看代码猜结果
stu_list[0]='王小利'
print(stu_list[0])
print(stu2_list[0])
print(c[0])


