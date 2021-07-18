class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: (x[0], x[1]))
        curr = points[0]
        i = 1
        shots = 1
        while i < len(points):
            if points[i][0] > curr[1]:
                curr = points[i]
                shots += 1
            if points[i][1] < curr[1]:
                curr = points[i]
            i += 1
        return shots
