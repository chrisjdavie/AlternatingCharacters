'''
Inspired by the editorial. Bit code-golfy, loop is more Pythonic

Created on 31 Dec 2015

@author: chris
'''

for _ in range(input()):
    inputString = raw_input().strip()
    immediateRepetitions = 0
    for charI, charIPlus1 in zip(inputString[:-1], inputString[1:]):
        immediateRepetitions += charI == charIPlus1
    print immediateRepetitions