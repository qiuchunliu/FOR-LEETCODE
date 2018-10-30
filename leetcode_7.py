
x = -12300
while (x >= pow((-2),31)) and (x <= (pow(2,31)-1)):
    num1 = str(x)
    list1 = list(num1)
    list1.reverse()
    lenth = len(list1)
    temp = 0
    num = 0
    for n in range(0,lenth):
        if list1[n] != '0':
            temp = n
            break
    if list1[-1] == '-':
        p = lenth - temp - 2
        for m in range(temp,lenth-1):
            num += int(list1[m])*pow(10,p)
            p -= 1
        if (num >= pow((-2),31)) and (num <= (pow(2,31)-1)):
            print (-num)
            break
        else :print(0);break
    elif list1[-1] != '-' :
        for m in range(temp,lenth):
            num += int(list1[m])*pow(10,lenth-m-1)
        if (num >= pow((-2),31)) and (num <= (pow(2,31)-1)):print (num);break
        else:print (0);break
    print (0)
