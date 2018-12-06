"""
第k个排列
给出集合 [1,2,3,…,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

说明：

给定 n 的范围是 [1, 9]。
给定 k 的范围是[1,  n!]。

示例 1:
输入: n = 3, k = 3
输出: "213"

示例 2:
输入: n = 4, k = 9
输出: "2314"
"""


# class Solution(object):
#     # 另外一种解法
#     def next_permutation(self, s):
#         # 根据字符串得到其下一个排列
#         i = len(s) - 1
#         while i > 0 and s[i] < s[i - 1]:
#             i -= 1
#         j = i - 1
#         k = i
#         while j >= 0 and k + 1 < len(s) and s[k + 1] > s[j]:
#             k += 1
#         if j >= 0:
#             s[k], s[j] = s[j], s[k]
#
#         s[i:] = s[::-1][:len(s)-i]
#         return s
#
#     def getPermutation(self, n, k):
#         a = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
#         b = [i for i in xrange(1, n + 1)]
#         r = []
#         while b:
#             i = (k - 1) / a[n - 1]
#             r.append(str(b[i]))
#             b.remove(b[i])
#             k = k % a[n - 1]
#             n -= 1
#
#         return "".join(r)

"""
算法过程：

从一个[1，n]的区间内挑数字（也就是代码中的nums)加入答案（直到全挑光)，按什么顺序挑哪个数字呢？我们需要通过数学判断。

挑选过程如下：

比如n=4,证明一共有4!种排序，那我们当前的第k个排序是什么呢？我们先确定这个排序的第一个数字。我们知道对于每个数字开头的序列，在它确定的情况下，一共有(n-1)!种情况。比如1开头的n=4的序列，一共有3！种情况。那我们就可以通过k//(n-1)!来确定这是以哪个数字开头的序列，如果等于0,那就是1，如果等于1那就是2，以此类推

 

算法证明：

该算法无须证明，源于统计学。
--------------------- 
作者：我喝酸奶不舔盖 
来源：CSDN 
原文：https://blog.csdn.net/weixin_41958153/article/details/81234523 
版权声明：本文为博主原创文章，转载请附上博文链接！
"""
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # 0的阶乘一直到9!
        # 因为题目说了n<=9
        fac = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]
        # 找到对应的n应该对应的fac坐标,就是在第一项确定的情况一下，有(n-1)!种组合
        i = n - 1
        # 构建序列，这个num是用来储存我们当前可以添加的数的，也是为避免重复
        num = list(range(1, n + 1))
        ret = ""
        while i >= 0:
            # a用来获得我们要求的那一位在num里的下标
            a, b = k // fac[i], k % fac[i]
            # print(a)
            # 如果刚好整除干净，证明还在上一层
            if b == 0:
                a -= 1

            if a >= 0:
                ret += str(num[a])
                del num[a]
                i -= 1
            k = b
            # 如果刚好整除完，则我们已经可以知道接下来的排序情况了，它一定是最大的
            # 所以把剩下的可选的数字reverse来制造这种效果
            if b == 0:
                for i in reversed(num):
                    ret += str(i)
                break
        return ret


if __name__ == '__main__':
    s = Solution()
    result = s.getPermutation(2, 2)
    print(result)

    result = s.getPermutation(3, 3)
    print(result)

    result = s.getPermutation(4, 10)
    print(result)
