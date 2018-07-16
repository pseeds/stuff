#!/bin/python 
from __future__ import print_function
import math
import os
import random
import re
import sys

stringsArray = []
stringsArray.append("abc")
stringsArray.append("we promptly judged antique ivory buckles for the next prize")
stringsArray.append("we promptly judged antique ivory buckles for the prizes")
stringsArray.append("the quick brown fox jumps over the lazy dog")
stringsArray.append("the quick brown fox jump over the lazy dog")

# Complete the isPangram function below.

def char_range(c1,c2):
  for c in xrange(ord(c1), ord(c2)+1):
    yield chr(c)

for strng in stringsArray:
    
  print(strng)
  isPanagram = 1
  for c in char_range('a', 'z'):
    if c not in strng:
       isPanagram = 0 
       break

  # print(isPanagram, end='')
  print(isPanagram)

print()
