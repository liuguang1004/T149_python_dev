#set集合   使用{}创建   无序，不重复, 重复的算一次
# 练习1:
stu_set={'王金财','邓轩','邓轩','胡晶晶','胡晶晶','陈盼'}
print(stu_set)

# 练习2：遍历集合
for name in stu_set:
    print(name)

#练习3：使用in 判断是否为成员
if '胡晶晶' in stu_set:
    print('胡晶晶是我们班的同学')
else:
    print('胡晶晶不是我们班的同学')