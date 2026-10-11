from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dick1 = Counter(s1) 
        l_s1 = len(s1) # 2
        r = l_s1 - 1 # 1
    
        while r < len(s2): # 
            # s2[1-2+1:1]
            if dick1 == Counter(s2[r-l_s1 + 1:r+1]):
                return True
            r+=1
        return False
