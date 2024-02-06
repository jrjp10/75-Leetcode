class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []
    
new = Solution()
nums = [2, 7, 11, 15]
target = 9
result = new.twoSum(nums, target)
print("Indices of two numbers that add up to the target:",result)