class Solution:
    def reorganizeString(self, s: str) -> str:
        cnt = collections.Counter(s)
        heap = []
        for l in cnt:
            if (len(s) % 2 != 0 and cnt[l] > len(s)//2 + 1) or (len(s) % 2 == 0 and cnt[l] > len(s)//2):
                return ""
            else:
                heapq.heappush(heap, (-cnt[l], l))
        result = []
        while heap:
            cnt, cur = heapq.heappop(heap)
            if not result or result[-1] != cur:
                result.append(cur)
                if -(cnt + 1) > 0:
                    heapq.heappush(heap, (cnt + 1, cur))
            else:
                cnt_next, cur_next = heapq.heappop(heap)
                result.append(cur_next)
                if -(cnt_next + 1) > 0:
                    heapq.heappush(heap, (cnt_next + 1, cur_next))
                heapq.heappush(heap, (cnt, cur))
        return ''.join(result)
