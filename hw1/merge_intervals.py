class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        result = [intervals[0]]
        for pair in intervals:
            if result[-1][1] >= pair[0]:
                result[-1] = [min(result[-1][0], pair[0]), max(result[-1][1], pair[1])]
            else:
                result.append(pair)
        return result
