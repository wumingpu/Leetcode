"""
给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的 两个 整数。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

示例:
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
"""


# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         # 暴力法
#         num_index = 0
#         for num in nums:
#             num_need_find = target - num
#             try:
#                 index_need_find = nums.index(num_need_find)
#                 if num_index == index_need_find:
#                     num_index += 1
#                     continue
#             except ValueError:
#                 num_index += 1
#                 continue
#             return [num_index, index_need_find]


class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hash = {}
        for i in range(0, len(nums)):
            if nums[i] in hash:
                if (target - nums[i]) in hash:
                    return [hash[target - nums[i]], i]
            else:
                hash[nums[i]] = i
                if (target - nums[i]) in hash and i != hash[target - nums[i]]:
                    return [hash[target - nums[i]], i]
        return []


if __name__ == '__main__':
    s = Solution()
    # result = s.checkInclusion("ab", "eidbaooo")
    # print(result)

    result = s.twoSum([3,2,4], 6)
    print(result)