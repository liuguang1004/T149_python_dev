
for i in range(1,10,1):
    for j in range(1,i+1):
        print('%d*%d=%02d '%(j,i,i*j),end='')
    print('')