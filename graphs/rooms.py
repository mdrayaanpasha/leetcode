class Solution(object):

    

    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        def DFS(src,G,visited):
            visited[src]=True

            for elem in G[src]:
                if not visited[elem]:
                    DFS(elem,G,visited)


        visited=[False] * len(rooms)
        DFS(0,rooms,visited)

        return all(visited)
        