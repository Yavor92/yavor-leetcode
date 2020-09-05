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


class Solution(object):

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m, n = len(nums1), len(nums2)
        total_len = m + n

        def get_k_element(k, m, n):
            index_a, index_b = 0, 0
            while True:
                if index_a == m:
                    return nums2[index_b + k - 1]
                if index_b == n:
                    return nums1[index_a + k - 1]
                if k == 1:
                    return min(nums1[index_a], nums2[index_b])

                aci = min(index_a + (k // 2 - 1), m - 1)
                bci = min(index_b + (k // 2 - 1), n - 1)
                pivot_a, pivot_b = nums1[aci], nums2[bci]
                if pivot_a <= pivot_b:
                    k -= aci - index_a + 1
                    index_a = aci + 1
                else:
                    k -= bci - index_b + 1
                    index_b = bci + 1

        if total_len % 2 == 1:
            return get_k_element((total_len+1) // 2, m, n)
        else:
            return get_k_element(total_len // 2, m, n) + get_k_element(total_len // 2 + 1, m, n) / 2
