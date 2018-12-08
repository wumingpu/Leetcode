"""
排序链表
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:
输入: 4->2->1->3
输出: 1->2->3->4

示例 2:
输入: -1->5->3->4->0
输出: -1->0->3->4->5
"""


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        ori_list = []
        while head is not None:
            # print(head.val)
            ori_list.append(head.val)
            head = head.next

        ori_list.sort()
        ret = self.create_link_list(ori_list)
        return ret


    def create_link_list(self, l_list):
        dummy_node = ListNode(-1)
        curr_node = dummy_node
        for i in l_list:
            curr_node.next = ListNode(i)
            curr_node = curr_node.next
        return dummy_node.next


"""
快排自实现
"""
# class Solution:
#     # @param {ListNode} head
#     # @return {ListNode}
#     def sortList(self, head):
#         hat = ListNode(None)
#         hat.next = head
#         self.quick_sort(hat, None)
#         return hat.next
#
#     # requirement: hat is not None
#     def quick_sort(self, hat, tail):
#         if hat.next is tail or hat.next.next is tail:
#             return
#
#         hat1, hat2, hat3 = hat, hat.next, ListNode(None)
#         tail1, tail2, tail3 = hat1, hat2, hat3
#         p, pivot = hat2.next, hat2.val
#         while p is not tail:
#             if p.val < pivot:
#                 tail1.next, tail1, p = p, p, p.next
#             elif p.val == pivot:
#                 tail2.next, tail2, p = p, p, p.next
#             else:
#                 tail3.next, tail3, p = p, p, p.next
#
#         # Caution: DO NOT change the order of these three line codes below.
#         tail3.next = tail
#         tail2.next = hat3.next
#         tail1.next = hat2
#
#         self.quick_sort(hat1, hat2)
#         self.quick_sort(tail2, tail)


def create_link_list(l_list):
    dummy_node = ListNode(-1)
    curr_node = dummy_node
    for i in l_list:
        curr_node.next = ListNode(i)
        curr_node = curr_node.next
    return dummy_node.next


if __name__ == '__main__':
    s = Solution()
    ll1 = create_link_list([4, 2, 1, 3])
    result = s.sortList(ll1)

    while result is not None:
        print(result.val)
        result = result.next
    # print(result)