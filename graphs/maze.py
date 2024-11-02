
from collections import deque

class Solution(object):
    def nearestExit(self, maze, entrance):
        """
        :type maze: List[List[str]]
        :type entrance: List[int]
        :rtype: int
        """
        queue = deque([(entrance[0], entrance[1], 0)])
        maze[entrance[0]][entrance[1]] = '+'
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        
        while queue:
            x, y, steps = queue.popleft()
            
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(maze) and 0 <= ny < len(maze[0]) and maze[nx][ny] == '.':
                    if nx == 0 or nx == len(maze) - 1 or ny == 0 or ny == len(maze[0]) - 1:
                        return steps + 1
                    
                    maze[nx][ny] = '+'
                    queue.append((nx, ny, steps + 1))
                    
        return -1
        