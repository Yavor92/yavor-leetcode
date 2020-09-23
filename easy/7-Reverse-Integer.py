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


class Solution(object):

    def reverse(self, x: int) -> int:
        y = x
        rev = 0
        INTMAX = 2147483648
        INTMIN = -2147483647
        if x < 0:
            x = -x
        while x != 0:
            pop = x % 10
            x //= 10
            if (rev > INTMAX/10) or (rev == INTMAX and pop > 7):
                return 0
            if (rev < INTMIN/10) or (rev == INTMIN and pop < -8):
                return 0
            rev = rev * 10 + pop
        return rev if y >= 0 else -rev


if __name__ == '__main__':
    solu = Solution()
    rev = solu.reverse(-123)
    print(rev)
