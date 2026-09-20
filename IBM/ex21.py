#1. Remove nth node from the back of the linked list
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeNthFromEnd(head, n):
    dummy = ListNode(0, head)
    fast = slow = dummy
    
    for _ in range(n):
        fast = fast.next
        
    while fast and fast.next:
        fast = fast.next
        slow = slow.next
        
    slow.next = slow.next.next
    return dummy.next

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def removeNthFromEnd(self, nth):
    #print(f"{self.val}")
    dummy = ListNode(0)
    dummy.next = self

    fast=self
    slow=dummy #slow starts one step behind fast to detect the node before what i want delate

    while nth>0 and fast is not None:
        fast=fast.next
        nth -=1

    print(f"fast {fast.val}")
    print(f"slow {slow.val}")

    while fast is not None:
        fast=fast.next
        slow=slow.next
    if slow.next is not None:
        slow.next=slow.next.next

    print(slow.val)
    return dummy.next

def print_linked_list(head):
    
    elements = []
    current = head
    while current:
        elements.append(str(current.val))
        current = current.next
    print(" -> ".join(elements))

# --- Example Usage ---
if __name__ == "__main__":
    # Create list: 1 -> 2 -> 3 -> 4 -> 5
    head = create_linked_list([1, 2, 3, 4, 5])
    print("Original list:")
    print_linked_list(head)
    
    # Remove the 2nd node from the end (which is 4)
    new_head = removeNthFromEnd(head, 2)
    
    print("\nList after removing 2nd node from the end:")
    print_linked_list(new_head)