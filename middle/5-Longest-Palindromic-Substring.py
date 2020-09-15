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

    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        if length < 2 or s == s[::-1]:
            return s
        max_length = 1
        start = 0
        for i in range(1, length):
            even = s[i - max_length: i + 1]
            odd = s[i - max_length-1: i + 1]
            if i - max_length - 1 >= 0 and odd == odd[::-1]:
                start = i - max_length - 1
                max_length += 2
                continue
            if i - max_length >= 0 and even == even[::-1]:
                start = i - max_length
                max_length += 1
        return s[start: start + max_length]


if __name__ == '__main__':
    solu = Solution()
    s = "dbadiweorndcdcdadcdcdbadiweornd"
    print(solu.longestPalindrome(s))