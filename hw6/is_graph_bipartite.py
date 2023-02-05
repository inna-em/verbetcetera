class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color = [-1 for _ in range(len(graph))]
        for node in range(len(graph)):
            if color[node] == -1:
                color[node] = 0
                stack = [node]
                while stack:
                    curr = stack.pop()
                    for nei in graph[curr]:
                        if color[nei] == -1:
                            color[nei] = color[curr] ^ 1
                            stack.append(nei)
                        elif color[nei] == color[curr]:
                            return False
        return True
