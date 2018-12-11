#!/usr/bin/python3
#-*- coding: utf-8 -*-
#Function: simulate the binary tree in python
#__author__: Tresser
#


class BTNode(object):
    def __init__(self, key=None, lchild=None, rchild=None):
        self.key = key
        self.lchild = lchild
        self.rchild = rchild

class BiTree(object):
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

    # 综合打印
    def printTrave(self, bt):
        print("先序遍历: ", end="")
        self.preOrderTrave(bt)
        print('\n')
        print("中序遍历: ", end="")
        self.inOrderTrave(bt)
        print('\n')
        print("后序遍历: ", end="")
        self.postOrderTrave(bt)
        print('\n')


if __name__ == '__main__':
    # data = input("Please input the node value: ")
    data_list = list([3,5,1,6,2,0,8,None,None,7,4])

    btree = BiTree(data_list)
    root = btree.createBiTree()
    btree.printTrave(root)