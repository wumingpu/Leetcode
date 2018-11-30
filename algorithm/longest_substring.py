"""
给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

示例 1:
输入: "abcabcbb"
输出: 3
解释: 因为无重复字符的最长子串是 "abc"，所以其长度为 3。

示例 2:
输入: "bbbbb"
输出: 1
解释: 因为无重复字符的最长子串是 "b"，所以其长度为 1。

示例 3:
输入: "pwwkew"
输出: 3
解释: 因为无重复字符的最长子串是 "wke"，所以其长度为 3。
     请注意，你的答案必须是 子串 的长度，"pwke" 是一个子序列，不是子串。
"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        # 暴力版
        if len(s) == 0:  # 空字符串
            return 0
        if len(s.strip(" ")) == 0:  # 如果全是空格
            return 1
        str_len = len(s)+1
        max_len = 0
        for i in range(str_len):
            for j in range(i, str_len):
                if j - i <= max_len:
                    continue
                # 切割字符串
                sub_str = s[i:j]
                len_ori = len(sub_str)
                sub_list = list(sub_str)
                # 去重
                len_unique = len(set(sub_list))
                # print(i, j)
                if len_ori > len_unique:
                    break
                else:
                    max_len = len_ori if len_ori > max_len else max_len
        return max_len


if __name__ == '__main__':
    s = Solution()
    # result = s.lengthOfLongestSubstring("abcabcbb")
    # print(result)

    result = s.lengthOfLongestSubstring("c")
    print(result)
    #
    # str = "c"
    # print(str[0:1])
