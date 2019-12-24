
class Solution:
    '''
    比起3Sum更接近渐进法
    '''
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums=sorted(nums)
        closet=nums[0]+nums[1]+nums[2]
        dif=abs(closet-target)
        for a in range(len(nums)):
            b=a+1
            c=len(nums)-1
            while b<c:
                temp=nums[a]+nums[b]+nums[c]
                tempdif=abs(temp-target)
                if target==temp:
                    return target
                if tempdif<dif:
                    dif,closet=tempdif,temp
                if target>temp:
                    b+=1
                else:
                    c-=1
        return closet
