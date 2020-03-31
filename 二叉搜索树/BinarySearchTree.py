# coding=utf-8
"""
@File    :   BinarySearchTree.py    
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/3/31 13:35   LiuHe      1.0          二叉搜素树BST相关思路 基于二叉树的框架
                                          明确节点要做的事情 剩下的交给框架去做
"""


class TreeNode(object):
    """
    定义二叉树
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


def traverse(root):
    """
    框架结构
    :param root: 树根节点
    :return: None
    """
    # 节点需要做的操作
    # 剩下的为框架结构
    traverse(root.get_left())
    traverse(root.get_right())


def is_same_tree(root1, root2):
    """
    判断两棵树是否相同
    :param root1: 树一
    :param root2: 树二
    :return: 判断结果
    """
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    if root1.get_value() != root2.get_value():
        return False

    return is_same_tree(root1.get_left(), root2.get_left()) \
           and \
           is_same_tree(root1.get_right(), root2.get_right())


def is_valid_BST(root, min=None, max=None):
    """
    判断BST的合法性
    root 节点要跟左子树所有节点 右子树所有节点进行比较
    :param root: 树根节点
    :return: 验证结果
    """
    if root is None:
        return True
    if min is not None and root.get_value() <= min.get_value():
        return False
    if max is not None and root.get_value() >= max.get_value():
        return False

    return is_valid_BST(root.get_left(), min, root) \
           and is_valid_BST(root.get_right(), root, max)


def is_in_BST(root, target):
    """
    查找目标值是否在二叉搜索树内
    用到二叉搜索树的特性  左子树都小于节点值 右子树都大于节点值
    :param root: 树根节点
    :param target: 目标值
    :return: 判断结果
    """
    if root is None:
        return False
    if root.get_value() == target:
        return True
    if root.get_value() < target:
        return is_in_BST(root.get_right(), target)
    if root.get_value() > target:
        return is_in_BST(root.get_left(), target)


def insert_in_BST(root, target):
    """
    将目标值插入到二叉搜索树中
    :param root: 树根节点
    :param target: 目标值
    :return: 最终的二叉搜索树
    """
    if root is None:
        return TreeNode(target)
    if root.get_value() < target:
        root.set_right(insert_in_BST(root.get_right(), target))
    if root.get_value() > target:
        root.set_left(insert_in_BST(root.get_left(), target))

    return root


def delet_from_BST(root, target):
    """
    从二叉搜索树中删除一个目标节点
    关键在于删除节点后不能破坏二叉搜索树的定义
    三种情况：
        1.节点刚好是叶节点，则直接删除
        2.节点只有一个非空子节点，则让其子节点直接代替
        3.节点有两个子节点，必须用左子树中最大的节点或者右子树最小的节点来代替
    :param root: 树根节点
    :param target: 目标值
    :return: 删除后的二叉搜索树
    """
    if root is None:
        return None
    if root.get_value() == target:
        if root.get_left() is None:
            return root.get_right()
        if root.get_right() is None:
            return root.get_left()
        min_node = get_min(root.get_right())
        root.set_value(min_node.get_value())
        root.set_right(delet_from_BST(root.get_right(), min_node.get_value()))
    elif root.get_value() < target:
        root.set_right(delet_from_BST(root.get_right(), target))
    elif root.get_value() > target:
        root.set_left(delet_from_BST(root.get_left(), target))

    return root


def get_min(root):
    """
    辅助函数 寻找右子树中最小的节点
    :param root: 树根节点
    :return:
    """
    while root.get_left() is not None:
        root = root.get_left()

    return root

