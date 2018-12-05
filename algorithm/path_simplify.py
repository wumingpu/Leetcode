"""
给定一个文档 (Unix-style) 的完全路径，请进行路径简化。

例如，
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"

边界情况:

你是否考虑了 路径 = "/../" 的情况？
在这种情况下，你需返回 "/" 。
此外，路径中也可能包含多个斜杠 '/' ，如 "/home//foo/" 。
在这种情况下，你可忽略多余的斜杠，返回 "/home/foo" 。
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        list_path = path.strip('/').split('/')
        list_stack = []
        # print(list_path)
        for i in list_path:
            if i == "..":
                if len(list_stack) > 0:
                    list_stack.pop()
                continue
            if i == "." or i == "":
                continue
            list_stack.append(i)

        # print(list_stack)
        simplify_path = '/'.join(list_stack)
        # print(simplify_path)
        if path.startswith("/"):
            return "/" + simplify_path
        return simplify_path


# class Solution(object):
#     def simplifyPath(self, path):
#         """
#         :type path: str
#         :rtype: str
#         """
#         # 最快
#         path = path.split("/")
#         stack = []
#         for p in path:
#             if p in ["", "."]:
#                 continue
#             if p == "..":
#                 if stack:
#                     stack.pop()
#             else:
#                 stack.append(p)
#         return "/" + "/".join(stack)


if __name__ == '__main__':
    s = Solution()
    result = s.simplifyPath("/a/./b/../../c/")
    print(result)

    result = s.simplifyPath("///")
    print(result)

    result = s.simplifyPath("/home/../../..")
    print(result)

    result = s.simplifyPath("/..")
    print(result)

    result = s.simplifyPath("/home//foo/..")
    print(result)

    result = s.simplifyPath("/a/./b///../c/../././../d/..//../e/./f/./g/././//.//h///././/..///")
    print(result)

