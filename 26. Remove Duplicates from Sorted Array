#two-pointer
def removeDuplicates(self, nums):
     
        n=len(nums)
        
        i=j=0
        while j<n:
            if nums[j]==nums[i]:
                j+=1
            else:
                i+=1
                nums[i]=nums[j]
                
        return i+1
# fast:
  n=len(nums)
        if n<2:
            return n
        i=1
        num=nums[0]
        while i<n:
            if num==nums[i]:
                del nums[i]
                n-=1
            else:
                num=nums[i]
                i+=1
        return n
#slowone:
if len(nums)<2:
            return 
        i=1
        num=nums[0]
        while i<len(nums):
            if num==nums[i]:
                nums.remove(num)
            else:
                num=nums[i]
                i+=1
