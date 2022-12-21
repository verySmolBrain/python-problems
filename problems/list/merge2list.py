from typing import Optional
from problems.ds import ListNode

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1 or not list2:
            return list1 if list1 else list2

        if list1.val < list2.val:
            resultHead, resultTail = list1, list1
            list1 = list1.next
        else:
            resultHead, resultTail = list2, list2
            list2 = list2.next
    
        while list1 and list2:
            if list1.val < list2.val:
                resultTail.next = list1
                resultTail, list1 = resultTail.next, list1.next
            else:
                resultTail.next = list2
                resultTail, list2 = resultTail.next, list2.next
        
        if list1 or list2:
            resultTail.next = list1 if list1 else list2
        
        return resultHead