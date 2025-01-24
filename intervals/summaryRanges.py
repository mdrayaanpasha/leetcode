class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        n=len(nums)
        out = []
        start=0
        for i in range(1,n):
            if nums[i] != nums[i-1]+1:
                if start == i-1:
                    r = f"{nums[start]}"
                    out.append(r)
                    start=i
                else:
                    r=f"{nums[start]}->{nums[i-1]}"
                    out.append(r)
                    start=i
        
        if start == n-1:
            out.append(f"{nums[start]}")
        else:
            out.append(f"{nums[start]}->{nums[n-1]}")

        return out

