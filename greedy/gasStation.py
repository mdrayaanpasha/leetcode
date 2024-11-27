class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int

        #stratergy:

        - dude lets traverse from 0:n.
        - keep track of cost at that point with tht gas station. cause u see if the cost of going to that thing is more
         then what we get at before station we dont wanna go there from prev station, we wanna start from here.
        - then we keep track of total cost and total gas, if cost > gas : ofc i cant go mate!
        - else return the index.
        """
        tot_cost,tot_gas,curr_gas,start_index,n = 0,0,0,0,len(gas)
      
        for i in range(n):
            tot_gas+=gas[i]
            tot_cost+=cost[i]
            curr_gas+=gas[i]-cost[i]

            if curr_gas < 0:
                start_index=i+1
                curr_gas=0

        
        if tot_cost > tot_gas:
            return -1
        

        return start_index
       