# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        self.ptr = self
        
    def add(self,value):
        self.ptr.next = ListNode(val = value)
        self.ptr = self.ptr.next
        
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ptr = l1
        l1_nums = []
        while ptr:
            l1_nums.append(ptr.val)
            ptr = ptr.next
        a = "".join([str(x) for x in l1_nums])
        
        ptr = l2
        l2_nums = []
        while ptr:
            l2_nums.append(ptr.val)
            ptr = ptr.next
        b = "".join([str(x) for x in l2_nums])
        
        result = self.custom_add(a,b)
        
        temp = ListNode(val = result[0])
        for x in result[1:]:
            temp.add(x)
        
        return temp
    
    @staticmethod
    def custom_add(a,b):
        
        i = 0 
        carry = set()
        result = []
        while i < max(len(a),len(b)):
            try:
                x = eval(a[i])
            except:
                if carry:
                    x = carry.pop()
                else:
                    x = 0
            
            try:
                y = eval(b[i])
            except:
                if carry:
                    y = carry.pop()
                else:
                    y = 0
            
            q = None
            r = None
            if not carry:
                temp = x + y
            else:
                temp = (x + y) + carry.pop()
            if temp > 9:
                q = temp // 10 
                r = temp % 10                                                                                                                                                                                              
                carry.add(q)                                                                                                                                                                                               
                result.append(r)                                                                                                                                                                                           
            else:                                                                                                                                                                                                          
                result.append(temp)                                                                                                                                                                                        
            i += 1
        if carry:
            result.append(carry.pop())
        return result
