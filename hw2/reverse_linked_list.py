class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        curr_node = head
        prev_node = None
        while curr_node is not None:
            next_node = curr_node.next
            curr_node.next = prev_node
            prev_node, curr_node = curr_node, next_node
        return prev_node
