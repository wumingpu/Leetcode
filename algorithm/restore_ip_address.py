"""
给定一个只包含数字的字符串，复原它并返回所有可能的 IP 地址格式。

示例:

输入: "25525511135"
输出: ["255.255.11.135", "255.255.111.35"]
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        self.generateIpAddress("", s)

    def generateIpAddress(self, ip, s):
        n = ip.count('.')
        ip_len = len(ip)
        if n == 3:
            if ip_len - 3 < len(s):
                last_string = s[ip_len]



if __name__ == '__main__':
    sss = Solution()
    result = sss.restoreIpAddresses("25525511135")
    print(result)

    print("255.255.11.135".count('.'))
    print("".count('.'))