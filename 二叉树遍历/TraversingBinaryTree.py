"""
@File    :   TraversingBinaryTree.py.py
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/2/12 19:48   LiuHe      1.0         二叉树遍历 BFS DFS
                                         其中深度优先分为先序遍历、中序遍历、后序遍历
"""


class TreeNode(object):
    """
    定义二叉树节点
    """
    def __init__(self, value):
        self._value = value
        self._left = None
        self._right = None

    def set_left(self, left_data):
        self._left = left_data

    def set_right(self, right_data):
        self._right = right_data

    def get_left(self):
        return self._left

    def get_right(self):
        return self._right

    def get_value(self):
        return self._value


class Traversing(object):
    """
    遍历二叉树
        深度优先 DFS
        广度优先 BFS
    """
    def __init__(self, tree):
        self._tree = tree

    def DFS(self):
        pass

    def BFS(self):
        pass
