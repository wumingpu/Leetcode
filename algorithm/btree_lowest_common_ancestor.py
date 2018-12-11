"""
二叉树的最近公共祖先
给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。

百度百科中最近公共祖先的定义为：“对于有根树 T 的两个结点 p、q，最近公共祖先表示为一个结点 x，满足 x 是 p、q 的祖先且 x 的深度尽可能大（一个节点也可以是它自己的祖先）。”

例如，给定如下二叉树:  root = [3,5,1,6,2,0,8,null,null,7,4]

        _______3______
       /              \
    ___5__          ___1__
   /      \        /      \
   6      _2       0       8
         /  \
         7   4
示例 1:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 1
输出: 3
解释: 节点 5 和节点 1 的最近公共祖先是节点 3。

示例 2:
输入: root = [3,5,1,6,2,0,8,null,null,7,4], p = 5, q = 4
输出: 5
解释: 节点 5 和节点 4 的最近公共祖先是节点 5。因为根据定义最近公共祖先节点可以为节点本身。
说明:

所有节点的值都是唯一的。
p、q 为不同节点且均存在于给定的二叉树中。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class BTree(object):
    def __init__(self, data_list):
        # 初始化即将传入的列表的迭代器
        self.it = iter(data_list)

    def createBiTree(self, bt=None):
        try:
            # 步进获取下一个元素
            next_data = next(self.it)
            # 如果当前列表元素为'#', 则认为其为 None
            if next_data is None:
                bt = None
            else:
                bt = BTNode(next_data)
                bt.lchild = self.createBiTree(bt.lchild)
                bt.rchild = self.createBiTree(bt.rchild)
        except Exception as e:
            print(e)

        return bt

    # 先序遍历函数
    def preOrderTrave(self, bt):
        if bt is not None:
            print(bt.key, end=" ")
            self.preOrderTrave(bt.lchild)
            self.preOrderTrave(bt.rchild)

    # 中序遍历函数
    def inOrderTrave(self, bt):
        if bt is not None:
            self.inOrderTrave(bt.lchild)
            print(bt.key, end=" ")
            self.inOrderTrave(bt.rchild)

    # 后序遍历函数
    def postOrderTrave(self, bt):
        if bt is not None:
            self.postOrderTrave(bt.lchild)
            self.postOrderTrave(bt.rchild)
            print(bt.key, end=" ")


class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """




if __name__ == '__main__':
    s = Solution()
    data_list = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    btree = BTree(data_list)
    btree_root = btree.createBTree()
    # result =
    # c1 = btree_root
    # c2_1 = btree_root.left
    # c2_2 = btree_root.right
    # c3_1 = c2_1.left
    # c3_2 = c2_1.right
    # c3_3 = c2_2.left
    # c3_4 = c2_2.right
    # c4_1 = c3_2.left
    # c4_2 = c3_2.right
    # print(c1.val)
    # print(c2_1.val, c2_2.val)
    # print(c3_1.val, c3_2.val, c3_3.val, c3_4.val)
    # print(c4_1.val, c4_2.val)
    btree.preOrderTrave(btree_root)