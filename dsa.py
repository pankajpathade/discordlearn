class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                for k in range(j + 1,len(nums)):
                    if nums[i] + nums[j] + nums[k] == target:
                        print(i,j,k)
                        return [i, j, k]


nums=[1,2,3,4,5,6,7,8,9]
target= 7                

a=Solution()

a.twoSum(nums,target)
print(a)

