class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        graph = [[] for _ in range(n)]
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))
        heap = []
        heapq.heappush(heap, (0, src, 0))
        while heap:
            dist, node, steps = heapq.heappop(heap)
            if node == dst:
                return dist
            if steps >= k + 1:
                continue
            for neighbour, cost in graph[node]:
                heapq.heappush(heap, (dist + cost, neighbour, steps + 1))
        return -1
        
