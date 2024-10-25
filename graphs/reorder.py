class Solution(object):
    def minReorder(self, n, connections):
        """
        - my approach is to first find out all the paths and create a fake reversed 
        version of them while specifying there are not real.
        - im going to do this by first traversing throu the connnctions and then 
        adding edges in a new graph were i have both real and fake paths.
        - then i start my dfs from 0,-1 meaing child is 0 parent is -1.
        - then traverse thru its neighbors in dfs if par==neighbor go to next       neighbor, else check if you can go from here to that neighbor, if yes it means that dude you gotta reverse, so changes++ and then do dfs recursively on other neighbor given its not parent. 

side note: this problemm didnt let me sleep all night so i woke up early to complete it!!!!
        """


        self.changes=0
        graph=defaultdict(list)

        for a,b in connections:
            graph[a].append((b,True))
            graph[b].append((a,False))

        
        def dfs(city,parent):



            for neighbor,original in graph[city]:
                if neighbor==parent:
                    continue

                if original:
                    self.changes+=1

                dfs(neighbor,city)

        dfs(0,-1)
        return self.changes