from typing import List
def display(root): 
    while (root != None) : 
        print(root.val, end = " ") 
        root = root.next

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        fast = head
        slow = head

        while slow and fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if(slow == fast):
                return True
        return False
n1 = ListNode(3);n2=ListNode(2);n3=ListNode(0);n4=ListNode(-4)
n1.next = n2;n2.next = n3;n3.next = n4;n4.next = n2
sol=Solution()
print(sol.hasCycle(n1))
