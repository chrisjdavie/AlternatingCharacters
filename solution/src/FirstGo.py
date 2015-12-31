'''
Solving the Alternating Characters hackerrank puzzle

https://www.hackerrank.com/challenges/alternating-characters

---------------------

Problem Statement

Shashank likes strings in which consecutive characters are different. For example, he likes ABABA, while he doesn't like ABAA. Given a string containing characters A and B only, he wants to change it into a string he likes. To do this, he is allowed to delete the characters in the string.

Your task is to find the minimum number of required deletions.

Input Format

The first line contains an integer T, i.e. the number of test cases. 
The next T lines contain a string each.

Output Format

For each test case, print the minimum number of deletions required.

Constraints

1<=T<=10 
1<= length of string <=105

---------------------

Alternatively - count the number of characters which are the same as the previous one.

Created on 31 Dec 2015

@author: chris
'''

for _ in range(input()):
    inputString = raw_input().strip()
    
    lastChar = 'C'
    immediateRepetitions = 0
    for compChar in inputString:
        if compChar != lastChar:
            lastChar = compChar
        else:
            immediateRepetitions += 1
    print immediateRepetitions