class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        graph = [[] for _ in range(n)]
        for i, e in enumerate(edges):
            graph[e[0]].append((e[1], succProb[i]))
            graph[e[1]].append((e[0], succProb[i]))
        probs = [float(0) for _ in range(n)]
        probs[start] = float(1)
        heap = []
        heapq.heappush(heap, (float(-1), start))
        while heap:
            currProb, cur = heapq.heappop(heap)
            for neighb, succProb in graph[cur]:
                newProb = succProb * (-currProb)
                if probs[neighb] < newProb:
                    probs[neighb] = newProb
                    heapq.heappush(heap, (-newProb, neighb))
        return probs[end]
