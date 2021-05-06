#for的第二种用法
# score_list=[100,99,77,66,54,1000]
#
# for score in score_list:
#     print(score)

# 1. 1到100求和
# sum=0
# for i in range(1,101,1):
#     sum=sum+i
#
# print('1+2+3+...+100=%d'%sum)

# 2. 100到1求和
# sum=0
# for i in range(100,0,-1):
#     sum=sum+i
#
# print('100+99+98+...+1=%d'%sum)

# 3. 1到100求和，如果结果累计到了666就算了，跳出循环，并返回当前的num是多少
sum=0
for i in range(1,101):
    sum=sum+i
    if sum>=666:
        print('i =',i)
        break

