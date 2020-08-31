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


class ListNode(object):

    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):

    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = [int(i) for i in (str(int(self.re_build(l1)) + int(self.re_build(l2))))]
        result.reverse()
        root = ListNode(result[0])
        rnext = root
        for i in result[1:]:
            rnext.next = ListNode(i)
            rnext = rnext.next
        return root

    def re_build(self, a):
        if a.next is None:
            return str(a.val)
        else:
            return self.re_build(a.next) + str(a.val)


if __name__ == '__main__':
    l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next.next = ListNode(3)
    l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next.next = ListNode(4)
    solu = Solution()
    results = solu.addTwoNumbers(l1, l2)
    results = solu.re_build(results)
    print(results)