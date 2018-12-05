"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：
输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # me
        dummy_node = ListNode(-1)
        curr_node = dummy_node
        carry = 0
        while True:
            l1_val = 0 if l1 is None else l1.val
            l2_val = 0 if l2 is None else l2.val

            res_val = l1_val + l2_val + carry
            if res_val >= 10:
                res_val %= 10
                carry = 1
            else:
                carry = 0

            print(l1_val, l2_val, carry, res_val)

            curr_node.next = ListNode(res_val)
            curr_node = curr_node.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None
            if l1 is None and l2 is None:
                break

        return dummy_node.next


# class Solution:
#     def addTwoNumbers(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         # 最快
#         head = ListNode(0)
#         head.next = l1
#         carry = 0
#
#         while l1 and l2:
#             s = l1.val + l2.val + carry
#             val, carry = s % 10, s // 10
#             l1.val = val
#             prev, l1, l2 = l1, l1.next, l2.next
#
#         l = l1 or l2
#         prev.next = l
#         while l and carry:
#             s = l.val + carry
#             val, carry = s % 10, s // 10
#             l.val = val
#             prev, l = l, l.next
#
#         if carry:
#             prev.next = ListNode(1)
#
#         return head.next


if __name__ == '__main__':
    s = Solution()
    l1_node1 = ListNode(3)
    l1_node2 = ListNode(4)
    l1_node3 = ListNode(2)
    l1_node3.next = l1_node2
    l1_node2.next = l1_node1

    l2_node1 = ListNode(4)
    l2_node2 = ListNode(6)
    l2_node3 = ListNode(5)
    l2_node3.next = l2_node2
    l2_node2.next = l2_node1

    result = s.addTwoNumbers(l1_node3, l2_node3)
    while True:
        print(result.val)
        result = result.next
        if result is None:
            break
