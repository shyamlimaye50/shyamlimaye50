class node:
    def __init__(self, val=0, next=None):
        self.data = val
        self.next = next
def findMid(head):
    # Initialize two pointers, one will go one step a time (slow), another two at a time (fast)
   slow = head
   fast = head

   # Iterate till fast's next is null (fast reaches end)
   while fast and fast.next:
       slow = slow.next
       fast = fast.next.next
   # return the slow's data, which would be the middle element.
   #print("The middle element is ", slow.data)
   return slow.data
n1 = node(1);n2=node(2);n3=node(3);n4=node(4);n5=node(5)
n1.next = n2;n2.next = n3;n3.next = n4;n4.next=n5;n5.next = None
print('Middle element is ',findMid(n1))
