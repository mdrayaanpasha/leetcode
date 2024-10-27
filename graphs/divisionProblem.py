class Solution(object):
    def calcEquation(self, equations, values, queries):
        """
        :type equations: List[List[str]]
        :type values: List[float]
        :type queries: List[List[str]]
        :rtype: List[float]
        """
        G = defaultdict(list)
        for i, eq in enumerate(equations):
            G[eq[0]].append((eq[1], values[i]))
            G[eq[1]].append((eq[0], 1 / values[i]))

        def dfs(src, target, visited, g, result):
            if src not in g or target not in g:
                return -1.0
            if src == target:
                return result

            visited[src] = True
            for neighbor, weight in g[src]:
                if neighbor not in visited:
                    res = dfs(neighbor, target, visited, g, result * weight)
                    if res != -1.0:
                        return res
            return -1.0

        return [dfs(q[0], q[1], defaultdict(bool), G, 1) for q in queries]