"""
给定一个包含了一些 0 和 1的非空二维数组 grid , 一个 岛屿 是由四个方向 (水平或垂直) 的 1 (代表土地) 构成的组合。你可以假设二维矩阵的四个边缘都被水包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为0。)

示例 1:
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
对于上面这个给定矩阵应返回 6。注意答案不应该是11，因为岛屿只能包含水平或垂直的四个方向的‘1’。

示例 2:
[[0,0,0,0,0,0,0,0]]
对于上面这个给定的矩阵, 返回 0。

注意: 给定的矩阵grid 的长度和宽度都不超过 50。
"""


# class Solution(object):
#     def maxAreaOfIsland(self, grid):
#         """
#         :type grid: List[List[int]]
#         :rtype: int
#         """
#         height = len(grid)
#         if height == 0:
#             return 0
#         width = len(grid[0])
#         if width == 0:
#             return 0
#
#         max_sum = 0
#         for i in range(height):
#             for j in range(width):
#                 if grid[i][j] == 1:  # 找到当前的位置为1，从此处开始深度优先搜索。
#                     # print(grid)
#                     sum1 = self.dfs(grid, i, j, height, width)
#                     max_sum = max(sum1, max_sum)
#         return max_sum
#
#     def dfs(self, grid, x0, y0, height, width):
#         sum1 = 1
#         grid[x0][y0] = 0  # 确定当前元素为1，赋值为0，避免被再次搜索
#         direct = [[0, 1], [0, -1], [1, 0], [-1, 0]]  # 分别定义下  上   右  左四个方向
#         for i in range(4):
#             x = x0 + direct[i][0]  # 横向
#             y = y0 + direct[i][1]  # 纵向
#             if x>=0 and x<height and y>=0 and y<width:
#                 # print(x, y, width, height)
#                 if grid[x][y] == 1:  # 确保被搜索位置在一个合法的位置
#                     sum1 += self.dfs(grid, x, y, height, width)
#         return sum1


class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        s = 0

        def do(i, j):
            grid[i][j] = -1
            count = 1
            if i > 0 and grid[i - 1][j] == 1:
                count += do(i - 1, j)
            if i < m - 1 and grid[i + 1][j] == 1:
                count += do(i + 1, j)
            if j > 0 and grid[i][j - 1] == 1:
                count += do(i, j - 1)
            if j < n - 1 and grid[i][j + 1] == 1:
                count += do(i, j + 1)
            return count

        for i in range(0, m):
            for j in range(0, n):
                if grid[i][j] == 1:
                    area = do(i, j)
                    if area > s:
                        s = area
        return s


if __name__ == '__main__':
    s = Solution()
    result = s.maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                                [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                                [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]])

    print(result)

