class Solution(object):
    def dividePlayers(self, skill):
        total = sum(skill)
        skill.sort()
        n = len(skill)
        if total % (n // 2) != 0:
            return -1
        
        i1=0
        i2=n-1
        chemistry=0
        summ=skill[i1]+skill[i2]
        for i in range(n//2):
            chemistry+=skill[i1]*skill[i2]
            if (summ!=skill[i1]+skill[i2]):
                return -1
            i1+=1
            i2-=1
        return chemistry  
