class Solution(object):
    def firstMissingPositive(self, nums):
        
        if nums==[]:
            return 1
        nums=set(nums)
        for i in range(1,len(nums)+1):
            if i not in nums:
                return i
        return i+1
