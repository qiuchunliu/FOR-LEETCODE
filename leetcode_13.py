# 输出罗马数字对应的数字
# 反向相加，注意负号的使用
num = {'I': 1,
	   'V': 5,
	   'X': 10,
	   'L': 50,
	   'C': 100,
	   'D': 500,
	   'M': 1000
	   }

string = input('enter a roma num : ')
summ = 0
count = -1
summ += num[string[count]]
for i in range(len(string) - 1):
	count -= 1
	if num[string[count]] < num[string[count + 1]]:
		temp = -num[string[count]]
		summ += temp
	else:
		summ += num[string[count]]

print(summ)
