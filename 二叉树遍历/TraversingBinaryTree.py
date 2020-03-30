"""
@File    :   TraversingBinaryTree.py.py
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/2/12 19:48   LiuHe      1.0         ���������� BFS DFS
                                         ����������ȷ�Ϊ�������������������������
"""
from �������ݽṹ import stack
from queue import Queue


class TreeNode(object):
    """
    ����������ڵ�
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
    ����������
        ������� DFS ǰ�����Ϊ��
        ������� BFS
    """
    def __init__(self, tree):
        self._tree = tree

    def DFS_stack(self, root):
        """
        ʹ��ջʵ��
        ������� ǰ�����
        :param root: �����ڵ�
        :return: ����б�
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
        �ݹ�ʵ��
        ������� ǰ�����
        :param root: �����ڵ�
        :return: ����ýڵ�
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
        �������
        ʹ�ö���ʵ�� �Ƚ��ȳ�
        :param root: �����ڵ�
        :return: ����б�
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

