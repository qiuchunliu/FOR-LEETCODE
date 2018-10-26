strs = ["flower","flow","flight"]
len1 = len(strs)
if len1 != 0:
	listt = []
	m = 0
	for i in range(0,len1):
		listt.append(len(strs[i]))
	temp = min(listt)
	for j in range(0,temp):
		n = 0
		for k in range(0,len1):
			if strs[k][j] == strs[0][j]:
				n += 1
		if n == len1:
			m += 1
		else:break
	print ('"%s"' % strs[0][0:m])
else :
	print ('""')
