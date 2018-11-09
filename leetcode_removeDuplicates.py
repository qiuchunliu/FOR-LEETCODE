nums = [0,1,1,1,2,2,3,3,4]
lenth = len(nums)
temp = ' '
i = 0
while i < lenth:
	if nums[i] != temp :
		temp = nums[i]
		i += 1
	else :
		nums.remove(nums[i])
	lenth = len(nums)
print (nums)
