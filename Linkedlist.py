class Node:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=next
    def __prt__(self,head):
        temp=head
        while temp and temp.next:
            print(temp.val,end="-->")
            temp=temp.next
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node4 = Node(4)

node1.next = node2
node2.next = node3
node3.next = node4