class Solution(object):
    
    def canFinish(self, numCourses, pre):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        
        @stratergy:

        - its simple first we will run dfs on each and every course.
        - if we detect a cycle, wow, boy its bad - there's some course that has paradox
          i.e to take 1 take 0, to take 0 take 1.
        - if there is a cycle indeed, but it has been fully processed, then no problem 
          your visited and true.
    
        """

        Graph = defaultdict(list)
        visited=[0] * numCourses


        for dest,src in pre:
            Graph[src].append(dest)
        
        def dfs(src):
            if visited[src] == 1:
                return False

            if visited[src] == 2:
                return True

            visited[src]=1
            for n in Graph[src]:
                if not dfs(n):
                    return False
                
            visited[src]=2
            return True

        for c in range(numCourses):
            if visited[c]==0:
                if not dfs(c):
                    return False


        return True
        