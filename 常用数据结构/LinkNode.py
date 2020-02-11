"""
@File    :   LinkNode.py.py
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/2/11 19:23   LiuHe      1.0         实现单链表
"""


# 在对象的原理上实现


class Node(object):
    """
    定义节点类
    节点有值域和指针域
        值域存储当前节点值
        指针域指向下一节点
    四种基本操作
        获取value值
        获取next值
        设置value值
        设置next值
    """

    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next

    def set_value(self, new_value):
        self.value = new_value

    def set_next(self, new_next):
        self.next = new_next


class LinkNode(object):
    """
    实现链表并实现几种基本操作
        检测是否为空
        读取列表
        在链表尾部添加元素
        检查元素是否在链表中
        修改指定位置元素值
        删除指定位置元素
        指定位置插入元素
        获取链表长度
    """

    def __init__(self):
        self._head = None
        self._len = 0

    def is_empty(self):
        return self._head is None

    def show(self):
        if self.is_empty() is None:
            print("链表为空")
        else:
            current_node = self._head.get_next()
            print(current_node.get_value())
            while current_node.get_next() is not None:
                current_node = current_node.get_next()

    def add(self, value):
        new_node = Node(value, None)
        if self.is_empty():
            self._head = new_node
        else:
            current_node = self._head.get_next()
            while current_node.get_next() is not None:
                current_node = current_node.get_next()
            current_node.set_next(new_node)
            self._len += 1

    def search(self, value):
        if self.is_empty():
            return None
        else:
            current_node = self._head
            index = 0
            while current_node.get_value != value:
                current_node = current_node.get_next()
                index += 1
            return index

    def modify(self, pos, value):
        if self.is_empty() or self._len < pos + 1:
            print("位置编号大于当前链表长度")
        else:
            index = 0
            current_node = self._head
            while index <= pos:
                current_node = current_node.get_next()
                index += 1
            current_node.set_value(value)

    def remove(self, pos):
        if self.is_empty() or self._len < pos+1:
            print("位置编号大于当前列表长度")
        else:
            index = 0
            current_node = self._head
            while index < pos:
                current_node = current_node.get_next()
                index += 1
            remove_node = current_node.get_next()
            tmp_node = remove_node.get_next()
            current_node.set_next(tmp_node)
            self._len -= 1

    def insert(self, pos, value):
        if self.is_empty() or self._len < pos + 1:
            print("位置编号大于当前链表长度")
        else:
            index = 0
            current_node = self._head
            while index <= pos:
                current_node = current_node.get_next()
                index += 1
            tmp_node = current_node.get_next()
            new_node = Node(value, tmp_node)
            current_node.set_next(new_node)
            self._len += 2

    def get_len(self):
        return self._len

