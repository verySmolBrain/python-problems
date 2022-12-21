from typing import Optional
from ds.ListNode import ListNode

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        h1, h2 = head, head
        
        while h2 and h2.next:
            h1 = h1.next
            h2 = h2.next.next
            
            if h1 == h2:
                return True
        
        return False

def run():
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    
    a = Solution().hasCycle(node1)
    print(a)
    
    node1 = ListNode(1)
    
    a = Solution().hasCycle(node1)
    print(a)