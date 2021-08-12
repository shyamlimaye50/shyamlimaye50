class ListNode:  
    def __init__(self, val=0, next=None):  
	        self.val = val  
	        self.next = next  
	  
def display(root):   
    while (root != None) :   
        print(root.val, end = " ")   
        root = root.next  
	  
n1=ListNode(1)  
n2=ListNode(3)  
n3=ListNode(5)  
n1.next=n2  
n2.next=n3  
n3.next=None  
display(n1)  
