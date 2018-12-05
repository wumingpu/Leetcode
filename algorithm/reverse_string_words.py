"""
给定一个字符串，逐个翻转字符串中的每个单词。

示例:

输入: "the sky is blue",
输出: "blue is sky the".
说明:

无空格字符构成一个单词。
输入字符串可以在前面或者后面包含多余的空格，但是反转后的字符不能包括。
如果两个单词间有多余的空格，将反转后单词间的空格减少到只含一个。
进阶: 请选用C语言的用户尝试使用 O(1) 空间复杂度的原地解法。
"""


class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        strip_s = s.strip(' ')

        if strip_s == "":
            return ""
        list_s = strip_s.split(' ')
        list_s = list(filter(lambda x: x != '', list_s))
        # print(list_s)
        list_s.reverse()
        return ' '.join(list_s)


if __name__ == '__main__':
    s = Solution()
    result = s.reverseWords("123  456")
    print(result)