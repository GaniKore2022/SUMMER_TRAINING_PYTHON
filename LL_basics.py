class Node:
    def __init__(self,data,next=None):
        self.data=data
        self.next=None
    
class LL:
    def __init__(self,nodes=None):
        self.head=None
        if nodes is not None:
            node=Node(data=nodes.pop(0))
            self.head=node

            for i in nodes:
                node.next=Node(data=i)
                node=node.next
    def __repr__(self):
        node=self.head
        arr=[]
        while node:
            arr.append(str(node.data))
            node=node.next
        return "->".join(arr)
    def length(self):
        temp=self.head
        c=0
        while temp:
            c=c+1
            temp=temp.next
        return c
    def even(self):
        e=Node(0)
        etemp=e
        temp=self.head
        while temp:
            x=temp.data
            if x%2==0:
                etemp.next=Node(x)
                etemp=etemp.next
            temp=temp.next
        return e.next
    def odd(self):
        o=Node(0)
        otemp=o
        temp=self.head
        while temp:
            if temp.data%2!=0:
                otemp.next=Node(temp.data)
                otemp=otemp.next
            temp=temp.next
        return o.next
    @staticmethod
    def add_last(head,x):
        temp=head
        while temp and temp.next:
            temp=temp.next
        new_node=Node(x)
        temp.next=new_node
        return head
    @staticmethod
    def reverse1(head):
    #     if head is None or head.next is None:
    #         return head
    #     re=reverse1(head.next)
    #     head.next.next=head
    #     head.next=None
    #     return re
        prev, curr = None , head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        head=prev
        return head
    def removedup(self):
        temp=self.head
        while temp and stemp.next:
            if temp.data==temp.next.data:
                temp.next=temp.next.next
            else:
                temp=temp.next
        return self.head
    def middle(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        return slow
    def mergesorted(self,head2):
        temp1=self.head
        temp2=head2
        res=Node(0)
        ans=res
        while temp1 and temp2:
            if temp1.data<temp2.data:
                ans.next=temp1
                temp1=temp1.next
            else:
                ans.next=temp2
                temp2=temp2.next
            ans=ans.next
        ans.next=temp1 or temp2
        return res.next
    def removedupunsorted(self):
        s=set()
        temp=self.head
        prev=None
        while temp:
            if temp.data in s:
                prev.next=temp.next
            else:
                s.add(temp.data)
                prev=temp
            temp=temp.next
        return self.head
    def Nthnode_from_end(self,n):
        temp=self.head
        c=0
        while temp:
            c+=1
            temp=temp.next
        c=c+1-n
        k=0
        temp=self.head
        while temp:
            k+=1
            if k==c:
                break
            else:
                temp=temp.next
        return temp

#         slow = self.head
#         fast = self.head
# 
#         # Move fast pointer n steps ahead
#         for _ in range(n):
#             if fast is None:
#                 return None  # n is greater than the length of the list
#             fast = fast.next
# 
#         # Move both pointers until fast reaches the end
#         while fast:
#             slow = slow.next
#             fast = fast.next
# 
#         return slow
    def palindrome(self):
#         curr=self.head
#         prev=None
#         while curr:
#             temp=curr.next
#             curr.next=prev
#             prev=curr
#             curr=temp
#         temp2=prev
#         temp=self.head
#         while temp:
#             if temp.data!=temp2.data:
#                 return False
#             temp=temp.next
#             temp2=temp2.next
#         return True
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        temp=slow
        prev=None
        while temp:
            temp1=temp.next
            temp.next=prev
            prev=temp
            temp=temp1
        half2=prev
        half1=self.head
        while half2:
            if half1.data!=half2.data:
                return False
            half1=half1.next
            half2=half2.next
        return True
#     def addingLLs(self,head2):
#         head1=self.reverse1(self.head)
#         head2=self.reverse1(head2)
#         temp1=head1
#         temp2=head2
#         res=Node(0)
#         res1=res
#         while temp1:
#             x=temp1.data+temp2.data
#             new_node=Node(x)
#             res1.next=new_node
#             res1=res1.next
#             temp1=temp1.next
#             temp2=temp2.next
#         ans=res.next
#         c=0
#         temp=ans
#         while temp:
#             a=temp.data
#             if c==1:
#                 a=a+c
#                 c=0
#             if a<10:
#                 temp.data=a
#             else:
#                 r=a%10
#                 temp.data=r
#                 c=1
#             temp=temp.next
#         if c==1:
#             ans=self.add_last(ans,c)
#         return self.reverse1(ans)
    def binarytodecimal(self):
        temp=self.head
        n=0
        while temp:
            n+=1
            temp=temp.next
        temp=self.head
        s=0
        while temp:
            if temp.data==1:
                s=s+(2**(n-1))
            n=n-1
            temp=temp.next
        return s
    def pairSum(self):
        slow=self.head
        fast=self.head
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next
        prev=None
        curr=slow
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        m=0
        while prev:
            if prev is None or self.head is None:
                break
            m=max(m,prev.data+self.head.data)
            self.head=self.head.next
            prev=prev.next
        return m
'''    @staticmethod
    def addTwoNumbers(l1, l2):
        temp1=l1
        temp2=l2
        ans=Node(0)
        res=ans
        while temp1 or temp2:
            if temp1 and temp2:
                x=temp1.data + temp2.data
                res.next=Node(x)
                res=res.next
                temp1=temp1.next
                temp2=temp2.next
            elif temp1:
                x=temp1.data
                res.next=Node(x)
                res=res.next
                temp1=temp1.next
            else:
                x=temp2.data
                res.next=Node(x)
                res=res.next
                temp2=temp2.next
        temp3=ans.next
        temp=temp3
        print_list(temp3)
        c=0
        while temp:
            a=temp.data
            if c==1:
                a=a+c
                c=0
            if a<10:
                temp.data=a
            else:
                r=a%10
                temp.data=r
                c=1
            temp=temp.next
        if c==1:
            temp=temp3
            while temp.next:
                temp=temp.next
            temp.next=Node(c)
        return temp3'''
'''def detectandremoveloop(head):
    if head is None or head.next is None:
        return False
    slow=head
    fast=head
    while fast and fast.next:
        slow=slow.next
        fast=fast.next.next
        if slow==fast:
            break
    if slow!=fast:
        return False
    slow=head
    while slow!=fast:
        slow=slow.next
        fast=fast.next
    temp=slow
    while temp.next!=slow:
        temp=temp.next
    temp.next=None
    return True'''
def print_list(head):
    current = head
    while current:
        print(current.data, end=" -> ")
        current = current.next
    print("None")

#lst=LL([9,9,9,9,9,9,9])
#print(lst.length())
# k=LL()
# k.head=lst.even()
# print(k)
# k1=LL()
# k1.head=lst.odd()
# print(k1)
# lst.reverse1()
# print(lst)
# lst.removedupunsorted()
# print(lst)
# k2=LL()
# k2.head=lst.middle()
# print(k2)
# k3=LL()
# lst2=LL([2,4,5,7])
# k3.head=lst.mergesorted(lst2.head)
# k4=LL()
# k4.head=lst.Nthnode_from_end(3)
# print(k4)
# print(lst.palindrome())
'''node=Node(1)
node1=Node(2)
node2=Node(3)
node3=Node(4)
node4=Node(5)
node.next=node1
node1.next=node2
node2.next=node3
node3.next=node4
node4.next=node2
print(detectandremoveloop(node))
print_list(node)'''
# lst1=LL([9,9,9,9])
# k5=LL()
# k5.head=lst.addTwoNumbers(lst.head,lst1.head)
# print(k5)
lst2=LL([47,22,81,46,94,95,90,22,55,91,6,83,49,65,10,32,41,26,83,99,14,85,42,99,89,69,30,92,32,74,9,81,5,9]
)
print(lst2.pairSum())