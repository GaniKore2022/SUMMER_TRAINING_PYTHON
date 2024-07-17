class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
def insertion_sort_list(head):
    if not head or not head.next:
        return head

    sorted_head = ListNode(0)  # Dummy node to act as the sorted part's head
    current = head

    while current:
        prev = sorted_head
        next_node = current.next

        # Find the correct position to insert the current node in the sorted part
        while prev.next and prev.next.value < current.value:
            prev = prev.next

        # Insert the current node into the sorted part
        current.next = prev.next
        prev.next = current

        # Move to the next node in the original list
        current = next_node

    return sorted_head.next
def create_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for value in values[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
# Create a linked list
values = [4, 2, 1, 3]
head = create_linked_list(values)

print("Original linked list:")
print_linked_list(head)

# Sort the linked list
sorted_head = insertion_sort_list(head)

print("Sorted linked list:")
print_linked_list(sorted_head)
