"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
说明：

1.num1 和 num2 的长度小于110。
2.num1 和 num2 只包含数字 0-9。
3.num1 和 num2 均不以零开头，除非是数字 0 本身。
4.不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。
"""


class Solution:
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if num1 == "0" or num2 == "0":
            return "0"

        len_num1 = len(num1)
        len_num2 = len(num2)
        list_len = len_num1 + len_num2 - 1

        list_final = []

        add_zero_n1 = 0
        add_zero_n2 = list_len - len_num2
        for n1 in num1:
            list_single = []
            for i in range(add_zero_n1):
                list_single.append(0)
            for n2 in num2:
                list_single.append(int(n1) * int(n2))
            for i in range(add_zero_n2 - add_zero_n1):
                list_single.append(0)
            add_zero_n1 += 1
            list_single.reverse()
            list_final.append(list_single)

        print(list_final)

        item_num = 0
        carry = 0
        list_result = []
        for i in range(list_len):
            item_num = 0
            for j in range(len(list_final)):
                item_num += list_final[j][i]
            print(item_num)
            item_num += carry
            carry = int(item_num / 10)
            item_num = item_num % 10

            list_result.append(item_num)
        if carry > 0:
            list_result.append(carry)

        list_result.reverse()
        print(str(list_result))
        return ''.join(list(map(lambda x: str(x), list_result)))


if __name__ == '__main__':
    s = Solution()
    result = s.multiply("123", "456")
    print(result)
