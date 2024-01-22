#-----Solution-1----------

# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 if(nums[i]+nums[j]==target):
#                     return [i,j]

            
# n=[2,3,5,4,6]
# obj=Solution()
# print(obj.twoSum(n,10))

#--------solution-2---------
# class Solution(object):
#     def twoSum(self, nums, target):
#         visited = {}
#         for i, element in enumerate(nums):
#             n = target - element
#             if n not in visited:
#                 visited[element] = i
#             else:
#                 return [visited[n], i]
# n=[2,3,5,4,6]
# obj=Solution()
# print(obj.twoSum(n,10))


#--------solution-3---------
class Solution(object):
    def twoSum(self, nums, target):
        visited = {}
        for i in range(len(nums)):
            element=nums[i]
            n = target - element
            if n not in visited:
                visited[element] = i
            else:
                return [visited[n], i]
n=[2,3,5,4,6]
obj=Solution()
print(obj.twoSum(n,10))


# class Solution(object):
#     def twoSum(self, nums, target):
#         for i in range(len(nums)):
#             seen=nums.copy()
#             n=target-nums[i]
#             if n in seen:
#                 index=nums.index(n)
#                 return [i,index]
#             else:
#                 return "Not Found"
                
# obj=Solution()
# l=[2,5,4,3,6,7]
# t=10
# print(obj.twoSum(l,t))






