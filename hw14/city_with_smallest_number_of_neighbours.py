class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        graph = [[] for _ in range(n)]
        for e in edges:
            graph[e[0]].append((e[1], e[2]))
            graph[e[1]].append((e[0], e[2]))
        res = (0, n - 1)
        for node in range(n):
            min_dist = [1e7] * n
            min_dist[node] = 0
            heap =[]
            heapq.heappush(heap, (0, node))
            while heap:
                dist, curr = heapq.heappop(heap)
                if dist > distanceThreshold:
                    break
                for neighb in graph[curr]:
                    if dist + neighb[1] < min_dist[neighb[0]]:
                        min_dist[neighb[0]] = dist + neighb[1]
                        heapq.heappush(heap, (dist + neighb[1], neighb[0]))
            reachable = -1
            for d in min_dist:
                if d <= distanceThreshold:
                    reachable += 1
            if reachable <= res[1]:
                res = (node, reachable)
        return res[0]
