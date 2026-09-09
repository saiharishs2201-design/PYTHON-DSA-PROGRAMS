class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return True   
    return False
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = head.next
if has_cycle(head):
    print("Loop detected")
else:
    print("No loop detected")