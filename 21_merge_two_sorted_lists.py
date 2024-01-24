# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        dummy = cur = ListNode(0)

        while l1 and l2:
            if l1.val < l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next
        if not l1:
            cur.next=l2
        else:
            cur.next=l1

        return dummy.next
o=Solution()
l1=ListNode([1,1,3,4,6])
l2=ListNode([0,2,4,6,7])
print(o.mergeTwoLists(l1,l2))

                
        
            
                
        