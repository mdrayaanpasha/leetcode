class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
         
    #here i am creating this result thing to store all possible combinations.
        results = []
        
        #this is a helper fucntion where am like dude i'll keep adding the same element unless the acc sum < target. then be like once i reach the thing i pop it, then i append the other element adjacent to it, unless again lesser then target, keep doin this. it will fo on and iterate over everythin.
        def helper(start,curr_comb,curr_sum):
            if curr_sum == target:
                results.append(list(curr_comb))
                
            if curr_sum > target:
                return
            
            for i in range(start,len(candidates)):
                # print(candidates[i])
                curr_comb.append(candidates[i])
                helper(i,curr_comb,curr_sum+candidates[i])
                curr_comb.pop()
                
        
        helper(0,[],0)
        
        return results
        
