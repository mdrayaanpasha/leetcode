class Solution:
    def removeDuplicates(self, arr: List[int]) -> int:
        """
        whats the plan phiieel?

        - so have 2 pointers and counter -> i,j
        - count the number of duplicates as you traverse of the latest elem
        - use i -> read pointer | j -> write pointer.
        - so go thru the list and then untill you have less then 2 duplicate count j++ and insert
        """
        j=1
        n=len(arr)
        count=1
        for i in range(1,n):
            if arr[i] == arr[i-1]:
                count+=1
            else:
                count=1
            if count <= 2:
                arr[j]=arr[i]
                j+=1

        return j
