"""
最长连续递增序列

给定一个未经排序的整数数组，找到最长且连续的的递增序列。

示例 1:
输入: [1,3,5,4,7]
输出: 3
解释: 最长连续递增序列是 [1,3,5], 长度为3。
尽管 [1,3,5,7] 也是升序的子序列, 但它不是连续的，因为5和7在原数组里被4隔开。

示例 2:
输入: [2,2,2,2,2]
输出: 1
解释: 最长连续递增序列是 [2], 长度为1。
注意：数组长度不会超过10000。
"""


class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0

        max_len = 1
        temp_len = 1
        for i in range(1, nums_len):
            if nums[i] > nums[i - 1]:
                temp_len += 1
                print(temp_len)
            else:
                max_len = max(temp_len, max_len)
                temp_len = 1
        max_len = max(temp_len, max_len)

        return max_len


if __name__ == '__main__':
    s = Solution()
    result = s.findLengthOfLCIS([1, 3, 5, 7])
    print(result)

    # result = s.findLengthOfLCIS([2, 2, 2, 2, 2])
    # print(result)
    #
    # result = s.findLengthOfLCIS([])
    # print(result)
