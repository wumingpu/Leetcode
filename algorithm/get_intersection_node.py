"""
相交链表
编写一个程序，找到两个单链表相交的起始节点。

例如，下面的两个链表：
A:          a1 → a2
                   ↘
                     c1 → c2 → c3
                   ↗
B:     b1 → b2 → b3
在节点 c1 开始相交。

注意：
如果两个链表没有交点，返回 null.
在返回结果后，两个链表仍须保持原有的结构。
可假定整个链表结构中没有循环。
程序尽量满足 O(n) 时间复杂度，且仅用 O(1) 内存。

致谢:
特别感谢 @stellari 添加此问题并创建所有测试用例。
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


# class Solution(object):
#     def getIntersectionNode(self, headA, headB):
#         """
#         :type head1, head1: ListNode
#         :rtype: ListNode
#         """
#         headA_list = []
#         headB_list = []
#         while headA is not None:
#             headA_list.append(headA)
#             headA = headA.next
#         while headB is not None:
#             headB_list.append(headB)
#             headB = headB.next
#         # print(headA_list)
#         # print(headB_list)
#
#         len_list = min(len(headA_list), len(headB_list))
#         for i in range(-1, -1-len_list, -1):
#             if headA_list[i] != headB_list[i]:
#                 if i == len_list:
#                     return "No intersection"
#                 else:
#                     return "Intersected at '"+str(headA_list[i].next.val)+"'"


"""
最快
"""
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        p1, p2 = headA, headB
        while p1 != p2:
            p1 = headB if p1 == None else p1.next
            p2 = headA if p2 == None else p2.next
            print(None if p1 is None else p1.val, None if p2 is None else p2.val)
        return p1


def create_link_list(l_list, common_list=None):
    dummy_node = ListNode(-1)
    curr_node = dummy_node
    for i in l_list:
        curr_node.next = ListNode(i)
        curr_node = curr_node.next
    if common_list is not None:
        curr_node.next = common_list
    return dummy_node.next


if __name__ == '__main__':
    s = Solution()
    listC = create_link_list([10, 20, 30, 40])
    listA = create_link_list([1, 2], listC)
    listB = create_link_list([5, 6, 8], listC)
    result = s.getIntersectionNode(listA, listB)

    # while result is not None:
    #     print(result.val)
    #     result = result.next
    print(result.val)