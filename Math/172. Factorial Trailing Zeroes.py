# -*- coding: utf-8 -*-
"""Untitled23.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/157SrUGfMAfYQo4vJMdxgGwjcqd-6D89z
"""

class Solution:
    def trailingZeroes(self, n: int) -> int:
        count=0
        while n>=5:
            count+=n//5
            n//=5
        return count