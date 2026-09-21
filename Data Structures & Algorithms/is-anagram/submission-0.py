class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ds = {}
        dt = {}

        for i in s:
            if i in ds:
                ds[i] += 1
            else :
                ds[i] = 1
        
        for j in t:
            if j in dt:
                dt[j] += 1
            else :
                dt[j] = 1
        
        return (ds == dt)