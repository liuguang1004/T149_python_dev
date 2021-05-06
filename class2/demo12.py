a=10
b=20
#单条件分支
# if a>b:
#     max=a;
# else :
#     max=b;
# print(max)
#多条件分支  根据考试的分数，来设置等级
score=55
level=''

if score>=90:
    level='优秀'
elif score>=80 and score<90:
    level = '良好'
elif score >=60 and score <80:
    level = '合格'
else:
    level = '不合格'
print('分数：%d，等级：%s'%(score,level))



