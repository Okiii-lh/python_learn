"""
@File    :   BinarySearchTree.py    
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/3/31 13:35   LiuHe      1.0          �������������˼· ���ڶ������Ŀ��
                                          ��ȷ�ڵ�Ҫ�������� ʣ�µĽ������ȥ��
"""


class TreeNode(object):
    """
    ���������
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


# ��ܽṹ
def traverse(root):
    # �ڵ���Ҫ���Ĳ���
    # ʣ�µ�Ϊ��ܽṹ
    traverse(root.get_left())
    traverse(root.get_right())


