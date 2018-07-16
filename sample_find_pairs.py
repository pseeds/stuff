#!/usr/bin/python

def findPairs(values):
  return [ (n, n+1) for n in values if n+1 in values ]

sampleInput = [ 22, 3, 7, 46, 8, 15, 21, 29, 14, 9, 87 ]
print findPairs(sampleInput)
