class Solution(object):
    def searchInsert(self, nums, target):
        if target in nums:
            return nums.index(target)
        else:
            for i in range(len(nums)):
                if(nums[i]>target):
                    return i
            return len(nums)
n=[2,3,5,6,8,9]           
o=Solution()
print(o.searchInsert(n,7))