"""
给定一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？找出所有满足条件且不重复的三元组。

注意：答案中不可以包含重复的三元组。

例如, 给定数组 nums = [-1, 0, 1, 2, -1, -4]，

满足要求的三元组集合为：
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""


# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # 超时
#         n_len = len(nums)
#         if n_len < 3:
#             return []
#         res_list = set()
#         nums.sort()
#         print(nums)
#         for n1 in range(n_len):
#             for n2 in range(n1+1, n_len):
#                 for n3 in range(n2+1, n_len):
#                     print([nums[n1], nums[n2], nums[n3]])
#                     if nums[n1] + nums[n2] + nums[n3] == 0:
#                         # res_list.append([nums[n1], nums[n2], nums[n3]])
#                         res_list.add(str([nums[n1], nums[n2], nums[n3]]))
#         return list(map(lambda x: eval(x), res_list))


# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # 超时
#         n_len = len(nums)
#         if n_len < 3:
#             return []
#         res_list = set()
#         nums.sort()
#         print(nums)
#         for n1 in range(n_len):
#             for n2 in range(n1+1, n_len):
#                 num_find = 0 - (nums[n1] + nums[n2])
#                 try:
#                     n3 = nums.index(num_find, n2+1, n_len)
#                     res_list.add(str([nums[n1], nums[n2], nums[n3]]))
#                 except ValueError:
#                     # print("Value Error")
#                     continue
#         return list(map(lambda x: eval(x), res_list))


# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # 最快
#         l = len(nums)
#         if l < 3:
#             return []
#
#         nums.sort()
#
#         ret = []
#         #三数相同，只能是0
#         if nums.count(0) >= 3:
#             ret.append([0,0,0])
#
#         #同正、同负，无结果
#         if nums[0] >= 0 or nums[-1] <= 0:
#             return ret
#
#         #二数相同
#         prev = None
#         doubles = []
#         for x in nums:
#             if prev is not None and prev == x and x not in doubles[-1:]:
#                 doubles.append(x)
#             prev = x
#
#         for x in doubles:
#             if x == 0:
#                 continue
#             sval = -x*2
#             if sval in nums:
#                 if sval > 0:
#                     ret.append([x, x, sval])
#                 else:
#                     ret.append([sval, x, x])
#
#         #各不相同
#         nums = list(set(nums))
#         nums.sort()
#         print nums
#
#         neg_len = abs(nums[0])
#         pos_len = abs(nums[-1])
#         max_len = max(neg_len, pos_len)+1
#         negmaps = [False]*max_len #负数
#         posmaps = [False]*max_len #正数
#         for x in nums:
#             if x < 0:
#                 negmaps[-x] = True
#             elif x > 0:
#                 posmaps[x] = True
#
#         # 包含0
#         if 0 in nums:
#             for x in xrange(1, max_len):
#                 if negmaps[x] and posmaps[x]:
#                     ret.append([-x, 0, x])
#
#         # 不包含0
#         sep = None
#         for i in xrange(len(nums)):
#             if nums[i] >= 0:
#                 sep = i
#                 break
#
#         # 两负一正
#         for i in xrange(sep):
#             for j in xrange(sep-1, i, -1):
#                 sval = -(nums[i]+nums[j])
#                 if sval > pos_len:
#                     break
#                 if posmaps[sval]:
#                     ret.append([nums[i], nums[j], sval])
#
#         # 两正一负
#         if nums[sep] == 0:
#             sep += 1
#         for i in xrange(sep, len(nums)):
#             if nums[i]*2 > neg_len:
#                 break
#             for j in xrange(i+1, len(nums)):
#                 sval = nums[i]+nums[j]
#                 if sval > neg_len:
#                     break
#                 if negmaps[sval]:
#                     ret.append([-sval, nums[i], nums[j]])
#
#         return ret


class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_hash = {}
        result = list()
        for num in nums:
            nums_hash[num] = nums_hash.get(num, 0) + 1
        if 0 in nums_hash and nums_hash[0] >= 3:
            result.append([0, 0, 0])

        neg = list(filter(lambda x: x < 0, nums_hash))
        pos = list(filter(lambda x: x >= 0, nums_hash))

        for i in neg:
            for j in pos:
                dif = 0 - i - j
                if dif in nums_hash:
                    if dif in (i, j) and nums_hash[dif] >= 2:  # 有重复的值例如[-1   -1   2]
                        result.append([i, j, dif])
                    if dif < i or dif > j:  # 避免出现重复的结果
                        print([i, j, dif])
                        result.append([i, j, dif])

        return result


# class Solution(object):
#     def threeSum(self, nums):
#         """
#         :type nums: List[int]
#         :rtype: List[List[int]]
#         """
#         # 我的提交
#         nums.sort()
#         res =[]
#         i = 0
#         for i in range(len(nums)):
#             if i == 0 or nums[i]>nums[i-1]:
#                 l = i+1
#                 r = len(nums)-1
#                 while l < r:
#                     s = nums[i] + nums[l] +nums[r]
#                     if s ==0:
#                         res.append([nums[i],nums[l],nums[r]])
#                         l +=1
#                         r -=1
#                         while l < r and nums[l] == nums[l-1]:
#                             l += 1
#                         while r > l and nums[r] == nums[r+1]:
#                             r -= 1
#                     elif s>0:
#                         r -=1
#                     else :
#                         l +=1
#         return res


if __name__ == '__main__':
    s = Solution()
    result = s.threeSum([-1, 0, 1, 2, -1, -4])
    print(result)
