"""
反转链表
反转一个单链表。

示例:
输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
进阶:
你可以迭代或递归地反转链表。你能否用两种方法解决这道题？
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        dummy_node = ListNode(-1)
        curr_node = dummy_node
        ori_list = []
        while head is not None:
            # dummy_node.next = head
            # curr_node = head
            ori_list.append(head.val)
            head = head.next

        ori_len = len(ori_list)
        for idx in range(ori_len-1, -1, -1):
            curr_node.next = ListNode(ori_list[idx])
            curr_node = curr_node.next

        return dummy_node.next


"""
遍历求解
"""
# class Solution:
#     def reverseList(self, head):
#         """
#         :type head: ListNode
#         :rtype: ListNode
#         """
#         cur, prev = head, None
#         while cur:
#             cur.next, prev, cur = prev, cur, cur.next
#         return prev


"""
递归求解
"""
# class Solution:
#     def __reverse(self, prev, curr):
#         if curr == None:
#             return prev
#         tmp = curr.next
#         curr.next = prev
#         prev = curr
#         curr = tmp
#         return self.__reverse(prev, curr)
#
#     def reverseList(self, head):
#         if head == None:
#             return None
#         curr = head.next
#         prev = head
#         head.next = None
#         return self.__reverse(prev, curr)


def create_link_list(l_list):
    dummy_node = ListNode(-1)
    curr_node = dummy_node
    for i in l_list:
        curr_node.next = ListNode(i)
        curr_node = curr_node.next
    return dummy_node.next


if __name__ == '__main__':
    s = Solution()
    ll1 = create_link_list([1, 2, 3, 4, 5])
    result = s.reverseList(ll1)

    while result is not None:
        print(result.val)
        result = result.next
    # print(result)
