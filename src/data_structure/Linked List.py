
# Linked List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

    # Insert Operations

    # Append Left 
    def appendLeft(self, value) -> "ListNode":
        temp = self
        self = ListNode(value)
        self.next = temp
        return self

    # Append Right
    def appendRight(self, value) -> None:
        if self.next == None:
            self.next = ListNode(value)
        else:
            temp = self
            while temp.next:
                temp = temp.next
            temp.next = ListNode(value)
    

    # Remove Operations
    def pop(self) -> None:
        pass


    def __str__(self) -> str:
        result = []
        curr = self
        while curr:
            result.append(str(curr.val))
            curr = curr.next
        
        return "[" + " ".join(result) + "]"
    
# Test
dummy = ListNode(0)
dummy.appendRight(1)
dummy.appendRight(2)
dummy.appendRight(3)

dummy = dummy.appendLeft(-1)
dummy = dummy.appendLeft(-2)
dummy = dummy.appendLeft(-3)

print(dummy)

