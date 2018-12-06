"""
搜索旋转排序数组
假设按照升序排序的数组在预先未知的某个点上进行了旋转。

( 例如，数组 [0,1,2,4,5,6,7] 可能变为 [4,5,6,7,0,1,2] )。

搜索一个给定的目标值，如果数组中存在这个目标值，则返回它的索引，否则返回 -1 。

你可以假设数组中不存在重复的元素。

你的算法时间复杂度必须是 O(log n) 级别。

示例 1:
输入: nums = [4,5,6,7,0,1,2], target = 0
输出: 4

示例 2:
输入: nums = [4,5,6,7,0,1,2], target = 3
输出: -1
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        # 旋转后的序列规律：
        # 1. 中间数小于最右边的数，右半段有序；
        # 2. 中间数大于最右边的数，左半段有序。
        print(nums)
        nums_len = len(nums)
        if nums_len == 0:
            return -1

        left_index = 0
        right_index = nums_len - 1
        while left_index <= right_index:
            mid_index = int((right_index + left_index) / 2)
            # print(mid_index)
            if nums[mid_index] == target:
                return mid_index
            elif nums[mid_index] < nums[right_index]:
                # 中间数小于右边数，右边有序
                if (nums[mid_index] < target) and (nums[right_index] >= target):
                    # 目标数在右边
                    left_index = mid_index + 1
                else:
                    right_index = mid_index - 1
            else:
                # 中间数小于右边数，左边有序
                if (nums[left_index] <= target) and (nums[mid_index] > target):
                    # 目标在左边
                    right_index = mid_index - 1
                else:
                    left_index = mid_index + 1
        return -1


# class Solution(object):
#     def search(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#         # 递归，比上面的方法快两倍
#         def chercher(l, target, debut, fin):
#             if fin < debut:
#                 return -1
#             mid = int((fin + debut) / 2)
#
#             vmid = l[mid]
#             if vmid == target:
#                 return mid
#
#             if l[debut] <= target < l[mid]:
#                 return chercher(l, target, debut, mid - 1)
#             if l[mid] < target <= l[fin]:
#                 return chercher(l, target, mid + 1, fin)
#             if l[mid] > l[fin]:
#                 return chercher(l, target, mid + 1, fin)
#             else:
#                 return chercher(l, target, debut, mid - 1)
#
#         return chercher(nums, target, 0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    result = s.search([4, 5, 6, 7, 0, 1, 2], 0)
    print(result)