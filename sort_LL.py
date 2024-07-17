class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def sortList(self, head):
        if head==None or head.next==None:
            return head
        x=[]
        temp=head
        while temp:
            x.append(temp.val)
            temp=temp.next
        x.sort()
        lst=self.sorting(x)
        return lst
    def sorting(self,x):
        if not x:
            return None
        a=ListNode(x[0])
        temp1=a
        for i in x[1:]:
            temp1.next=ListNode(i)
            temp1=temp1.next
        return a
def print_list(LL):
    temp=LL
    while temp:
        print(temp.val,end="->")
        temp=temp.next
node=ListNode(4)
node1=ListNode(2)
node2=ListNode(1)
node3=ListNode(3)
node.next=node1
node1.next=node2
node2.next=node3
k=Solution().sortList(node)
print_list(k)