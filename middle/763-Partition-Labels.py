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

    def partitionLabels(self, S: str) -> List[int]:
        storage_container = {word: num for num, word in enumerate(S)}
        start, end = 0, 0
        result = list()
        for i in range(len(S)):
            if i <= end:
                if storage_container[S[i]] > end:
                    end = storage_container[S[i]]
            elif i > end:
                result.append(i - start)
                start = i
                end = storage_container[S[i]]
        result.append(len(S)-start)
        return result


if __name__ == '__main__':
    solu = Solution()
    words = "ababcbacadefegdehijhklij"
    resu = solu.partitionLabels(words)
    print(resu)