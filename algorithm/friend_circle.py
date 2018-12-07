"""
朋友圈
班上有 N 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 N * N 的矩阵 M，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生互为朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

示例 1:
输入:
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。

示例 2:\
输入:
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
注意：

1.N 在[1,200]的范围内。
2.对于所有学生，有M[i][i] = 1。
3.如果有M[i][j] = 1，则有M[j][i] = 1。
"""


class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        queue = [0]
        cn = 0
        M_len = len(M)
        visited = [0] * M_len
        visited[0] = 1

        while len(queue):
            # print(queue)
            i = queue.pop()
            for j in range(len(M[i])):
                # print("loop", i, j)
                if visited[j] or i == j or M[i][j] == 0:  # 访问过了，自己，不是朋友关系
                    continue
                queue.append(j)  # j属于第i个人的朋友，入队
                visited[j] = 1  # 标记j这个人访问过了

            # print(queue)
            if len(queue) == 0:  # 如果队列不为空，证明，一轮朋友圈还没有遍历完成
                cn += 1  # 一个朋友圈
                if sum(visited) < M_len:  # 还有没有统计到的人
                    idx = visited.index(0)
                    queue.append(idx)
                    visited[idx] = 1
            # print(queue)
        return cn


# class Solution(object):
#     def findCircleNum(self, M):
#         """
#         :type M: List[List[int]]
#         :rtype: int
#         """
#         # 最快
#         if not M or not M[0]:
#             return 0
#
#         number = len(M)
#         res = list(range(number))
#         ret = 0
#
#         while res:
#             current = res.pop()
#             # 对每个人，循环遍历到和它同一个朋友圈的人都被删完了为止
#             stack = [current]
#             while stack:
#                 i = stack.pop()
#                 for j in [x for x in res if M[i][x] == 1]:
#                     res.remove(j)
#                     stack.append(j)
#             ret += 1
#
#         return ret


if __name__ == '__main__':
    s = Solution()
    result = s.findCircleNum(
        [[1, 1, 0],
         [1, 1, 0],
         [0, 0, 1]]
    )
    print(result)
