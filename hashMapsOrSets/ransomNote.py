class Solution:
    def canConstruct(self, r: str, m: str) -> bool:
        counter = {key:0 for key in r}

        for c in r:
            counter[c]+=1
        

        for c in m:
            if c in counter and counter[c] > 0:
                counter[c]-=1

        
        return all(val == 0 for val in counter.values())
