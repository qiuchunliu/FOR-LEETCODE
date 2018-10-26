s = '34f erer erf'
b = len (s)
mwo,p = 0,0
if b == 1 :
    if s[0] ==' ':
        print (0)
    else :
        print (1)
elif b == 0:
    print (0)
else :
    for i in range(1,b+1):
        if s[-i] != ' ' :
            p = i
            break
    for j in range(p,b+1):
        if s[-j] != ' ':
            mwo += 1
        else :
            break
    print (mwo)
