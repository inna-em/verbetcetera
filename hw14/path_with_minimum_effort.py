class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        res = [[1e6 + 1 for _ in range(len(heights[0]))] for _ in range(len(heights))]
        res[0][0] = 0
        heap = []
        heapq.heappush(heap, (0, (0, 0)))
        shifts = ((0, 1), (1, 0), (-1, 0), (0, -1))
        while heap:
            effort, coords = heapq.heappop(heap)
            for l_shift, r_shift in shifts:
                new_l, new_r = coords[0] + l_shift, coords[1] + r_shift
                if 0 <= new_l < len(heights) and 0 <= new_r < len(heights[0]):
                    curr_effort = max(effort, abs(heights[coords[0]][coords[1]] - heights[new_l][new_r]))
                    if curr_effort < res[new_l][new_r]:
                        res[new_l][new_r] = curr_effort
                        heapq.heappush(heap, (curr_effort, (new_l, new_r)))
        return res[-1][-1]
                    
