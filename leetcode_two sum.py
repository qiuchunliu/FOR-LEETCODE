class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenth = len (nums)
        for n in range (0,lenth) :
            if (target - nums[n] in nums) and nums.index(target - nums[n]) != n:
                return ([n,nums.index(target - nums[n])])