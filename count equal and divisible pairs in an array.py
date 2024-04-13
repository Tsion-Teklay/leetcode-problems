class Solution(object):
    def countPairs(self, nums, k):
        n=len(nums)
        pairs=0
        for i in range(n):
            for j in range(i+1,n):
                    if nums[i]==nums[j] and ((i*j)%k==0):
                        pairs+=1
        return pairs

        
