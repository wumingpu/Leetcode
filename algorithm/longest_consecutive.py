"""
最长连续序列
给定一个未排序的整数数组，找出最长连续序列的长度。

要求算法的时间复杂度为 O(n)。

示例:

输入: [100, 4, 200, 1, 3, 2]
输出: 4
解释: 最长连续序列是 [1, 2, 3, 4]。它的长度为 4。
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0

        nums = list(set(nums))
        nums_len = len(nums)
        nums.sort()

        max_len = 1
        temp_len = 1
        for i in range(1, nums_len):
            if (nums[i-1] + 1) == nums[i]:
                temp_len += 1
            else:
                max_len = max(temp_len, max_len)
                temp_len = 1

        max_len = max(temp_len, max_len)
        return max_len


if __name__ == '__main__':
    s = Solution()
    # result = s.longestConsecutive([100, 4, 200, 1, 3, 2])
    # print(result)

    # result = s.longestConsecutive([1, 2, 0, 1])
    # print(result)

    result = s.longestConsecutive([-1, 0])
    print(result)
