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

from typing import List
from utils import BIT


class Solution(object):

    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        sum = 0
        length = len(nums)
        preSum = [0] * (length + 1)
        for i in range(length):
            sum += nums[i]
            preSum[i + 1] = sum

        allNumbers = set()
        for pre in preSum:
            allNumbers.add(pre)
            allNumbers.add(pre - lower)
            allNumbers.add(pre - upper)

        allNumbers = list(allNumbers)
        allNumbers.sort()

        values = {v: k for k, v in enumerate(allNumbers)}

        ret = 0
        bit = BIT(len(values))
        for j in range(len(preSum)):
            left = values[preSum[j] - upper]
            right = values[preSum[j] - lower]
            ret += bit.query(right+1) - bit.query(left)
            bit.update(values[preSum[j]] + 1, 1)
        return ret


if __name__ == '__main__':
    data = [-2, 5, -1]
    lower = -2
    upper = 2
    solu = Solution()
    print(solu.countRangeSum(data, lower, upper))
