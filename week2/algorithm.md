## Add Two Numbers
### 给出两个链表，存储非负数，两个链表都是按倒序方式存储数字（个位，十位，百位……）要求将两个链表相加并以链表形式返回。
- [ ] 关于链表：data部分（数据域）存储数据，next部分（指针域）存储指针，指向下一个节点。任一个链表开始于头指针head，头结点的数据域可以不存储数据。
- [ ] code
```
def AddTwoNumbers(self, l1, l2):
        #指定到链表头节点
        p = dummy = ListNode(-1)
        #进位标志，低位有进位时为1，默认为0
        carry = 0
        #当两个链表的同一位置同时不为空时（即小詹举例的低三位数）
        while l1 and l2:
            #p.next为指针所指 l1.val为对应的数据
            p.next = ListNode(l1.val + l2.val + carry)
            #除法和求模运算获取p.next的十位个位
            carry =carry=int（p.next.val / 10）
            p.next.val %= 10
            p = p.next
            l1 = l1.next
            l2 = l2.next
        res = l1 or l2 #或运算即对应小詹举得高位例子（第四位第五位）
        while res:
            p.next = ListNode(res.val + carry)
            carry = carry=int（p.next.val / 10）
            p.next.val %= 10
            p = p.next
            res = res.next
        if carry:
            p.next = ListNode(1)
        return dummy.next#返回该链表
```
