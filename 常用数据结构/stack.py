"""
@File    :   stack.py    
@Contact :   13132515202@163.com

@Modify Time      @Author    @Version    @Description
------------      -------    --------    -----------
2020/2/11 20:34   LiuHe      1.0         实现栈
"""


class ArrayStack(object):
    """
    数组栈
        进栈
        出栈
        查看栈顶元素
        打印栈
        栈长度
    """
    def __init__(self):
        self._data = []

    def is_empty(self):
        return len(self._data) == 0

    def push(self, data):
        self._data.append(data)

    def pop(self):
        if self.is_empty():
            print("当前栈空")
        else:
            return self._data.pop()

    def top(self):
        if self.is_empty():
            print("当前栈空")
        else:
            return self._data[-1]

    def print_stack(self):
        pass
