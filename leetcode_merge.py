nu1 = [1,2,3,0,0,0]
nu2 = [2,5,6]
m,n = 4,3
nu1.reverse()
for i in range(0,len(nu1)):
	if nu1[0] == 0:
		nu1.remove(nu1[0])
	else :break
nu1.extend(nu2)
nu1.sort()
while nu1[0] == 0 :
	nu1.remove(nu1[0])
if len(nu1) < (m+n):
        nu1.extend([0]*((m+n)-len(nu1)))
print (nu1)
