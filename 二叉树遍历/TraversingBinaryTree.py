"""
@File    :   TraversingBinaryTree.py.py
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/2/12 19:48   LiuHe      1.0         二叉树遍历 BFS DFS
                                         其中深度优先分为先序遍历、中序遍历、后序遍历
"""
from 常用数据结构 import stack
from queue import Queue


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
        深度优先 DFS 前序遍历为例
        广度优先 BFS
    """
    def __init__(self, tree):
        self._tree = tree

    def DFS_stack(self, root):
        """
        使用栈实现
        深度优先 前序遍历
        :param root: 树根节点
        :return: 输出列表
        """
        print_arr = []
        if root is None:
            return
        stack.ArrayStack.push(root)
        while not stack.ArrayStack.is_empty():
            t = stack.ArrayStack.pop()
            if t.get_right() is not None:
                stack.ArrayStack.push(t.get_right())
            if t.get_left() is not None:
                stack.ArrayStack.push(t.get_left())
            print_arr.append(t.get_value())

        return print_arr

    def DFS_recursion(self, root):
        """
        递归实现
        深度优先 前序遍历
        :param root: 树根节点
        :return: 输出该节点
        """
        print(root.get_value())
        if root.get_left() is not None:
            next_node = root.get_left()
            self.DFS_recursion(next_node)
        if root.get_right() is not None:
            next_node = root.get_right()
            self.DFS_recursion(next_node)

    def BFS_stack(self, root):
        """
        广度优先
        使用队列实现 先进先出
        :param root: 树根节点
        :return: 输出列表
        """
        print_arr = []
        Queue.put(root)
        while not Queue.empty():
            t = Queue.get()
            print_arr.append(t.get_value())
            if t.get_left() is not None:
                Queue.put(t.get_left())
            if t.get_right() is not None:
                Queue.put(t.get_left())

        return print_arr

