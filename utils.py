# MIT License
# 
# Copyright (c) 2020 Yavor92
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class ListNode(object):

    def __init__(self, x, next=None):
        self.val = x
        self.next = next


class Node:

    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# 树状数组
class BIT(object):

    def __init__(self, n):
        self.tree = [0] * (n+1)
        self.n = n

    def lowbit(self, x: int):
        return x & (-x)

    def update(self, x: int, d: int):
        while x <= self.n:
            self.tree[x] += d
            x += self.lowbit(x)

    def query(self, x: int):
        ans = 0
        while x:
            ans += self.tree[x]
            x -= self.lowbit(x)
        return ans


# 线段树
class SegNode(object):

    def __init__(self, left: int, right: int):
        self.lo = left
        self.hi = right
        self.add = 0
        self.lchild = None
        self.rchild = None
