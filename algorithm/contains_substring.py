"""
给定两个字符串 s1 和 s2，写一个函数来判断 s2 是否包含 s1 的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

示例1:
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").


示例2:
输入: s1= "ab" s2 = "eidboaoo"
输出: False


注意：
输入的字符串只包含小写字母
两个字符串的长度都在 [1, 10,000] 之间
"""
"""
思路是使用每个字母的数量统计，然后进行窗口移动，拿s1依次进行移动对比s2.
"""


# class Solution:
#     def checkInclusion(self, s1, s2):
#         """
#         :type s1: str
#         :type s2: str
#         :rtype: bool
#         """
#         if s1 == "" or s2 == "":
#             return False
#         if len(s1) > len(s2):
#             return False
#         if s1 == s2:
#             return True
#         if s1 in s2:
#             return True
#         s2_list = list(s2)
#         index_list = []
#         for s_item in s1:
#             try:
#                 index = s2_list.index(s_item)
#                 print(index)
#             except ValueError:
#                 print("Value Error")
#                 return False
#
#             s2_list[index] = '#'
#             index_list.append(index)
#             print(s2_list)
#
#         index_list.sort()
#
#         first_index = index_list.pop(0)
#         print(first_index)
#         print(index_list)
#         for i_index in index_list:
#             if i_index == first_index+1:
#                 first_index += 1
#                 continue
#             else:
#                 return False
#         return True


class Solution:
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        if s1 == "" and s2 == "":
            return False
        if len(s1) > len(s2):
            return False

        list_s1 = []
        list_s2 = []
        diff = []
        for i in range(26):
            list_s1.append(0)
            list_s2.append(0)
            diff.append(0)

        ord_a = ord('a')
        len_s1 = len(s1)
        len_s2 = len(s2)
        list_str_s1 = list(s1)
        list_str_s2 = list(s2)
        for i_idx in range(len_s1):
            list_s1[ord(list_str_s1[i_idx])-ord_a] += 1
            list_s2[ord(list_str_s2[i_idx])-ord_a] += 1

        for i in range(26):
            diff[i] = list_s2[i] - list_s1[i]

        for i in range(len_s1, len_s2):
            # print("---------第", i-len_s1, '次----------')
            # print(list_s1)
            # print(list_s2)
            # print(diff)
            if self.is_same(diff) is True:
                return True
            diff[ord(list_str_s2[i-len_s1])-ord_a] -= 1
            diff[ord(list_str_s2[i])-ord_a] += 1
        if self.is_same(diff) is True:
            return True
        else:
            return False

    def is_same(self, diff):
        for i in diff:
            if i != 0:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    result = s.checkInclusion("ab", "eidbaooo")
    print(result)

    # result = s.checkInclusion("adc", "dcda")
    # print(result)
    # str1 = "abcb"
    # str1.replace() = '#'
    # print(str1)

    # list111 = [2,10,5,30,6,9,8]
    # list111.sort()
    # print(list111)
    # list111.pop(0)
    # print(list111)

    # res = ord('c') - ord('a')
    # print(res)

