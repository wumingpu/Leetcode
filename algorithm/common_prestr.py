"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:
输入: ["flower","flow","flight"]
输出: "fl"

示例 2:
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

说明:
所有输入只包含小写字母 a-z 。
"""
# 最快版
# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         str = ""
#         if len(strs) == 0:
#             return str
#         print(zip(*strs))
#         for each in zip(*strs):
#             print(each)
#             if len(set(each)) == 1:
#                 str += each[0]
#             else:
#                 return str
#         return str
#     # def _longestCommonPrefix(self,strs):
#     #     prefix = ""
#     #     if len(strs) == 0:
#     # return prefix
#     #     search_len = min(len(item) for item in strs)
#     #     for i in range(search_len):
#     # if len(set(item[i] for item in strs)) != 1:
#     # return prefix
#     # else:
#     # prefix += strs[0][i]
#     # return prefix

# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         # 暴力版
#         if len(strs) == 0:
#             return ""
#         if len(strs) == 1:
#             return strs[0]
#         common_prefix = ""
#         break_flag = False
#         char_index = 0
#         common_set = set()
#         len_strs = len(strs)
#         while True:
#             char_index += 1
#             loop_num = 0
#             for str in strs:
#                 if len(str) < char_index:
#                     break_flag = True
#                     break
#                 common_set.add(str[0 : char_index])
#                 print(common_set)
#                 if len(common_set) > 1:
#                     print("break")
#                     break_flag = True
#                     break
#                 loop_num += 1
#
#             print(loop_num, len_strs)
#             print("-----------")
#             if loop_num >= len_strs:
#                 common_prefix = common_set.pop()
#
#             common_set.clear()
#
#             if break_flag is True:
#                 break
#         return common_prefix


# class Solution:
#     def longestCommonPrefix(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: str
#         """
#         # map版，有bug
#         if len(strs) == 0:
#             return ""
#         if len(strs) == 1:
#             return strs[0]
#         char_index = 0
#         common_prefix = ""
#         while True:
#             char_index += 1
#             sub_str = map(lambda x: x[0:char_index], strs)
#             sub_str = list(sub_str)
#             set_str = set(sub_str)
#             print(set_str)
#             if len(set_str) > 1:
#                 break
#             else:
#                 # if len(set_str) == 0:
#                 #     break
#                 common_prefix = set_str.pop()
#         return common_prefix

class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        # 超简单版
        import os
        return os.path.commonprefix(strs)


if __name__ == '__main__':
    s = Solution()
    list1 = ["flower", "flow", "flight"]
    print(s.longestCommonPrefix(list1))

    list1 = ["", ""]
    print(s.longestCommonPrefix(list1))