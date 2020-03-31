"""
@File    :   BinarySearchTree.py    
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/3/31 13:35   LiuHe      1.0          二叉搜素树相关思路 基于二叉树的框架
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


# 框架结构
def traverse(root):
    # 节点需要做的操作
    # 剩下的为框架结构
    traverse(root.get_left())
    traverse(root.get_right())


