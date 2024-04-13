class Solution(object):
    def moveZeroes(self, nums):
        n=len(nums)
        r=0
        w=0
        while r<n:
            if nums[r]!=0:
                nums[r],nums[w]=nums[w],nums[r]
                w+=1
            r+=1

        
