class Node:
    def __init__(self, val=0, _next=None, prev=None):
        self.val = val
        self.next = _next
        self.prev = prev

class FrontMiddleBackQueue:

    def __init__(self):
        self.head = None
        self.mid = None
        self.tail = None
        self.len = 0
        

    def pushFront(self, val: int) -> None:
        
        if not self.head:
            self.head = Node(val)
            self.mid = self.head
            self.tail = self.head
            
        else:
            self.head.prev = Node(val=val, _next=self.head)
            self.head = self.head.prev
            if self.len % 2 == 1:
                self.mid = self.mid.prev
                
        self.len += 1
        return
        
        

    def pushMiddle(self, val: int) -> None:
        
        if not self.head:
            self.head = Node(val)
            self.mid = self.head
            self.tail = self.head
            
        elif self.len == 1:
            self.mid = Node(val=val, _next=self.tail)
            self.tail.prev = self.mid
            self.head = self.mid
            
        elif self.len % 2 == 0:
            old_mid = self.mid
            old_mid_next = old_mid.next
            new_mid = Node(val=val, _next=self.mid.next, prev=self.mid)
            old_mid.next = new_mid
            old_mid_next.prev = new_mid
            self.mid = new_mid

        elif self.len % 2 == 1:
            old_mid = self.mid
            old_mid_prev = old_mid.prev
            new_mid = Node(val=val, _next=self.mid, prev=self.mid.prev)
            old_mid.prev = new_mid
            old_mid_prev.next = new_mid
            self.mid=new_mid
            
        self.len += 1
        return
        

    def pushBack(self, val: int) -> None:
        
        if not self.head:
            self.head = Node(val)
            self.mid = self.head
            self.tail = self.head
            
        else:
            self.tail.next = Node(val=val, prev=self.tail)
            self.tail = self.tail.next
            if self.len % 2 == 0:
                self.mid = self.mid.next
                
        self.len += 1
        return
        
        

    def popFront(self) -> int:
        
        if self.len == 0:
            return -1
        
        old_head_val = self.head.val
        
        if self.len == 1:
            self.head = None
            self.mid = None
            self.tail = None
            
        else:
            self.head = self.head.next
            self.head.prev = None
            if self.len % 2 == 0:
                self.mid = self.mid.next
                
        self.len -= 1
        return old_head_val
        

    def popMiddle(self) -> int:
        
        if self.len == 0:
            return -1
        
        old_mid_val = self.mid.val
        
        if self.len == 1:
            self.head = None
            self.mid = None
            self.tail = None
            
        elif self.len == 2:
            self.mid = self.tail
            self.head = self.tail
            self.tail.prev = None
            
        else:
            self.mid.prev.next, self.mid.next.prev = self.mid.next, self.mid.prev
            if self.len % 2 == 0:
                self.mid = self.mid.next
            else:
                self.mid = self.mid.prev
                
        self.len -= 1
        return old_mid_val
        

    def popBack(self) -> int:
        
        if self.len == 0:
            return -1
        
        old_tail_val = self.tail.val
        
        if self.len == 1:
            self.head = None
            self.mid = None
            self.tail = None
            
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            if self.len % 2 == 1:
                self.mid = self.mid.prev
                
        self.len -= 1
        return old_tail_val
        
        


# Your FrontMiddleBackQueue object will be instantiated and called as such:
# obj = FrontMiddleBackQueue()
# obj.pushFront(val)
# obj.pushMiddle(val)
# obj.pushBack(val)
# param_4 = obj.popFront()
# param_5 = obj.popMiddle()
# param_6 = obj.popBack()
