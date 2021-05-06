# continue: 结束本次循环，继续下一次循环
# 练习：从键盘输入10个整数，如果输入的是负数，就不要了，如果正数就累加起来
sum=0
for i in range(1,11,1):
    num=int(input('请输入第%d个整数：'%i))
    if num < 0:
        continue
    else:
        sum=sum+num
print('输入的正数的和为：%d'%sum)