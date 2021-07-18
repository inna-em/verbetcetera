class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        result = ListNode()
        res_cur = result
        heap = []
        for i, l in enumerate(lists):
            if l:
                heapq.heappush(heap, (l.val, i))
        while heap:
            curr = heappop(heap)
            res_cur.next = ListNode(curr[0])
            res_cur = res_cur.next
            if lists[curr[1]].next:
                lists[curr[1]] = lists[curr[1]].next
                heapq.heappush(heap, (lists[curr[1]].val, curr[1]))
        return result.next
