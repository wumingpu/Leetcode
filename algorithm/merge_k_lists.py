"""
合并K个排序链表
合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

示例:

输入:
[
  1->4->5,
  1->3->4,
  2->6
]
输出: 1->1->2->3->4->4->5->6
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         # 分治法，将任务逐渐的变小，4化为2， 2化为1
#         len_lists = len(lists)
#         if len_lists == 0:
#             return lists
#         if len_lists == 1:
#             return lists[0]
#
#         mid = len_lists // 2
#         left = len_lists % 2  # 是否能除尽，除不尽则需要单独处理最后一个链表
#
#         l1 = lists[0: mid]
#         l2 = lists[mid: 2*mid]
#         r1 = self.mergeKLists(l1)
#         r2 = self.mergeKLists(l2)
#         r = self.merge2Lists(r1, r2)
#         if left:
#             r = self.merge2Lists(r, lists[-1])
#         return r
#
#     def merge2Lists(self, l1, l2):
#         head = ListNode(-1)
#         cur = head
#         while l1 and l2:
#             if l1.val < l2.val:
#                 cur.next = l1
#                 l1 = l1.next
#             else:
#                 cur.next = l2
#                 l2 = l2.next
#
#             cur = cur.next
#
#         if l1:
#             cur.next = l1
#         if l2:
#             cur.next = l2
#         return head.next


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # 加入数组，排序，再加入列表， 效率高
        node_list = []
        for list_head in lists:
            while list_head:
                node_list.append(list_head.val)
                list_head = list_head.next

        if node_list == []:
            return []

        # 排序
        node_list.sort()

        # 重新组合成为链表
        dummy_head = ListNode(-1)
        cur_node = dummy_head
        for node in node_list:
            cur_node.next = ListNode(node)
            cur_node = cur_node.next
        return dummy_head.next


def create_link_list(l_list):
    dummy_node = ListNode(-1)
    curr_node = dummy_node
    for i in l_list:
        curr_node.next = ListNode(i)
        curr_node = curr_node.next
    return dummy_node.next


if __name__ == '__main__':
    s = Solution()
    input_lists = [
        [1, 4, 5],
        [1, 3, 4],
        [2, 6]
    ]
    link_lists = []
    for input_list in input_lists:
        link_lists.append(create_link_list(input_list))
    result = s.mergeKLists(link_lists)

    while result:
        print(result.val)
        result = result.next

