class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        curr_node = head
        sz = 0
        while curr_node is not None:
            curr_node = curr_node.next
            sz += 1
        prefix = sz - n
        if prefix == 0:
            new_head = head.next
            return new_head
        curr_node = head
        for _ in range(prefix - 1):
            curr_node = curr_node.next
        next_node = curr_node.next.next
        curr_node.next = next_node
        return head
