# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        out=ListNode(l1.val+l2.val)
        l1=l1.next
        l2=l2.next
        out1=out
        
        while l1 or l2:
            if l2==None:
                l2=ListNode(0)
            elif l1==None:
                l1=ListNode(0)
                
            out1.next=ListNode(l1.val+l2.val)
            out1=out1.next
            
            l1=l1.next
            l2=l2.next
        
        out1=out
        c=0
        while out1:
            c1=(out1.val+c)//10
            out1.val=(out1.val+c)%10
            c=c1
            if out1.next==None and c>0:
                out1.next=ListNode(c)
                break
            out1=out1.next
            
        return out
