#字典  {}创建  {key:value}
#创建一个人的字段
people_dic={'name':'王利','age':23,'sex':'男'}
print(people_dic)
#提取数据 dic[key]
print(people_dic['name'])
print(people_dic['age'])
print(people_dic['sex'])

#创建一个学生的字典
stu_dic={'class_name':'T149班',
         'sid':1,
         'school':'新梦想IT教育学院'}
print(stu_dic)
print(stu_dic['class_name'])
print(stu_dic['sid'])
print(stu_dic['school'])

# dic[key]=值   如果key存在即是修改，如果key不存在就是添加
# 练习1：给王利加一个key，money 值为1000000
# 练习2：过了一个年，把王利的age+1
people_dic['age']=people_dic['age']+1
print(people_dic['age'])
# 练习3：把王利的age删除掉，变成一个密密
# 练习4：通过key遍历字典
#提取所有的key
print(people_dic.keys())

for k in people_dic.keys():
    print(k)
    print(people_dic[k])


# 练习5：通过in从字典中取值，遍历字典