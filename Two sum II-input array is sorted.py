class Solution(object):
    def twoSum(self, num, target):
        n=len(num)
        num.sort()
        i1=0
        i2=n-1
        while i1<i2:
            if num[i1]+num[i2]<target:
                i1+=1
            elif num[i1]+num[i2]>target:
                i2-=1
            else:
                return [i1+1,i2+1]
        
