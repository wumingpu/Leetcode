"""
合并区间
给出一个区间的集合，请合并所有重叠的区间。

示例 1:
输入: [[1,3],[2,6],[8,10],[15,18]]
输出: [[1,6],[8,10],[15,18]]
解释: 区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].

示例 2:
输入: [[1,4],[4,5]]
输出: [[1,5]]
解释: 区间 [1,4] 和 [4,5] 可被视为重叠区间。
"""


# Definition for an interval.
class Interval(object):
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


# class Solution(object):
#     def merge(self, intervals):
#         """
#         :type intervals: List[Interval]
#         :rtype: List[Interval]
#         """
#         inter_len = len(intervals)
#         if inter_len == 0:
#             return []
#         merged = [0] * inter_len
#         ret = []
#
#         for i in range(inter_len):
#             head = None
#             tail = None
#             flag = False
#             for j in range(i, inter_len):
#                 if merged[j]:  # merged[j] == 1
#                     print(i, j)
#                     continue
#                 inter = intervals[j]
#                 if head is None:
#                     head = inter.start
#                     tail = inter.end
#                     continue
#                 if head <= inter.start <= tail:  #
#                     print(i, j, [head, tail], [inter.start, inter.end])
#                     tail = max(tail, inter.end)
#                     merged[j] = 1
#                     flag = True
#                     continue
#                 if head <= inter.end <= tail:
#                     print(i, j, [head, tail], [inter.start, inter.end])
#                     head = min(head, inter.start)
#                     merged[j] = 1
#                     flag = True
#                     continue
#                 if inter.start <= head and inter.end >= tail:
#                     print(i, j, [head, tail], [inter.start, inter.end])
#                     merged[j] = 1
#                     flag = True
#                     continue
#
#             merged[i] = 1
#             # print(i, merged)
#             print(i, [head, tail], merged)
#             if head is not None:
#                 ret.append(str([head, tail]))
#                 # if not flag:  # 如果不是判断出来的结果，需要把第一个非1的mergered位置1
#                 #     try:
#                 #         idx = merged.index(0)
#                 #         merged[idx] = 1
#                 #     except ValueError:
#                 #         pass
#         return list(map(lambda x: eval(x), set(ret)))


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        inter_len = len(intervals)
        if inter_len < 2:
            return intervals

        intervals = sorted(intervals, key=lambda x: x.start)
        inter_list = []
        for inter in intervals:
            inter_list.append([inter.start, inter.end])
        # print(inter_list)
        ret = []
        curr = None
        for i in range(1, inter_len):
            last = intervals[i-1]
            curr = intervals[i]
            if curr.start <= last.end:
                curr.end = max(curr.end, last.end)
                curr.start = last.start
            else:
                ret.append(last)
        ret.append(curr)
        return ret


if __name__ == '__main__':
    s = Solution()
    i_list = []
    r_list = []
    temp_list = [[1, 3], [2, 6], [8, 10], [15, 18], [17, 19]]
    # temp_list = [[1, 4],[5, 6]]
    # temp_list = [[1,4],[0,4]]

    for t_item in temp_list:
        i_list.append(Interval(t_item[0], t_item[1]))
    result = s.merge(i_list)
    for r_item in result:
        r_list.append([r_item.start, r_item.end])
    print(r_list)
