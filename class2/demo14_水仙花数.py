# 求三位数的水仙花数
num=100
while num <1000:
     a=num%10
     b=num//10%10
     c=num//100
     if a**3+b**3+c**3==num:
         print(num)
     num=num+1
