class Solution:
    def largeGroupPositions(self, s: str) -> list[list[int]]:
        n=len(s)
        i=0
        j=1
        c=1
        h=[]
        while j<n:
            if s[i]==s[j]:
                c+=1
                j+=1

            else:
                if c>=3:
                    h.append([i,j-1])
                c=1
                i=j
                j+=1
                
        if c >= 3:
            h.append([i, n - 1])        
        return h
        
