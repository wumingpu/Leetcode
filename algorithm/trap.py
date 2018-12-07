"""
接雨水

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。



上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
"""


class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        len_height = len(height)
        if len_height == 0:
            return 0
        # 找到最高柱子的索引
        # max_num = max(height)
        # max_index = height.index(max_num)
        max_index = 0
        move_peak = 0
        trap_rain = 0
        for i in range(1, len_height):
            if height[i] > height[max_index]:
                max_index = i

        # 从前向最高柱子移动
        for i in range(0, max_index):
            if move_peak < height[i]:
                # 遇到了新高峰
                move_peak = height[i]
            else:
                # 没有遇到
                trap_rain += move_peak - height[i]

        move_peak = 0
        # 从后向最高柱子移动
        for j in range(len_height - 1, max_index, -1):
            if move_peak < height[j]:
                move_peak = height[j]
            else:
                trap_rain += move_peak - height[j]

        return trap_rain


if __name__ == '__main__':
    s = Solution()
    result = s.trap([0, 1, 0, 1, 1, 0, 1, 3, 2, 1, 2, 1])
    print(result)
