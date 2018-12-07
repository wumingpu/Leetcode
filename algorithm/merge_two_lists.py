"""
合并两个有序链表
将两个有序链表合并为一个新的有序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        # 有一方或两方为空，则返回另一方或None
        if l1 is None or l2 is None:
            return l1 if l2 is None else l2

        dummy_node = ListNode(-1)
        curr_node = dummy_node

        while l1 is not None and l2 is not None:
            num1 = l1.val
            num2 = l2.val
            # max = 0
            if num1 == num2:
                # 两个同时添加至结果链表, 同时进行移位
                # max = num1
                curr_node = self.addNodeToList(curr_node, num1)
                curr_node = self.addNodeToList(curr_node, num2)
                l1 = l1.next
                l2 = l2.next
            elif num1 < num2:
                curr_node = self.addNodeToList(curr_node, num1)
                l1 = l1.next
            else:
                curr_node = self.addNodeToList(curr_node, num2)
                l2 = l2.next

        if l1 is None and l2 is None:
            return dummy_node.next

        l_remain = l1 if l2 is None else l2
        # while l_remain is not None:
        #     curr_node = self.addNodeToList(curr_node, l_remain.val)
        #     l_remain = l_remain.next
        curr_node.next = l_remain  # 和上方注释的code等价
        return dummy_node.next

    def addNodeToList(self, curr, num):
        curr.next = ListNode(num)
        curr = curr.next
        return curr


"""
简洁, 思路相同
"""
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#         if not (l1 and l2):
#             return l1 if l1 else l2
#         first = ListNode(0)
#         head = first
#         while l1 is not None and l2 is not None:
#             if l1.val <= l2.val:
#                 head.next = l1
#                 l1 = l1.next
#             else:
#                 head.next = l2
#                 l2 = l2.next
#             head = head.next
#         if l1:
#             head.next = l1
#         elif l2:
#             head.next = l2
#         return first.next

"""
最快，思路相同
"""
# class Solution(object):
#     def mergeTwoLists(self, l1, l2):
#         """
#         :type l1: ListNode
#         :type l2: ListNode
#         :rtype: ListNode
#         """
#
#         origin = ListNode(0)
#         cur = origin
#         while l2 is not None:
#             while l1 is not None and l2.val > l1.val:
#                 cur.next = l1
#                 cur = cur.next
#                 l1 = l1.next
#             cur.next = l2
#             cur = cur.next
#             l2 = l2.next
#         cur.next = l1 if l2 is None else l2
#         return origin.next


def create_link_list(l_list):
    dummy_node = ListNode(-1)
    curr_node = dummy_node
    for i in l_list:
        curr_node.next = ListNode(i)
        curr_node = curr_node.next
    return dummy_node.next


if __name__ == '__main__':
    s = Solution()
    ll1 = create_link_list([1, 2, 4])
    ll2 = create_link_list([1, 3, 4])
    result = s.mergeTwoLists(ll1, ll2)
    while result is not None:
        print(result.val)
        result = result.next
    print(result)
