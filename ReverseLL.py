class ListNode:
    def __init__(self,val=0,next=None):
        self.val=val
        self.next=None
    def __repr__(self):
        node=self
        x=[]
        while node:
            x.append(str(node.val))
            node=node.next
        return "-->".join(x)
#     def reverseList(self, head):
#         curr=head
#         if curr is None:
#             return None
#         prev=None
#         while curr.next:
#             curr=curr.next
#         newhead=curr
#         curr=head
#         prev=None
#         while curr!=newhead:
#             temp=curr.next
#             curr.next=prev
#             prev=curr
#             curr=temp
#         curr.next=prev
#         return newhead
    def getIntersectionNode(self, headA, headB):
        s=set()
        while headA:
            s.add(headA)
            headA=headA.next
        while headB:
            if headB in s:
                return headB
            headB=headB.next
        return None

lst=ListNode()
node1=ListNode(4)
node2=ListNode(1)
node3=ListNode(8)
node4=ListNode(4)
node5=ListNode(5)
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node5
nodeA=ListNode(5)
nodeB=ListNode(6)
nodeC=ListNode(1)
nodeD=ListNode(8)
nodeE=ListNode(4)
nodeF=ListNode(5)
nodeA.next=nodeB
nodeB.next=nodeC
nodeC.next=node3
lst1=lst.getIntersectionNode(node1,nodeA)
print(lst1)