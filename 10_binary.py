'''Task
Given a base-10 integer,n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript.

Example
n=125
The binary representation of 125_10 is 1111101_2. In base 10, there are 5 and 1 consecutive ones in two groups. Print the maximum, 5.

Input Format

A single integer,n.

Constraints
1<=n<=10`6
Output Format

Print a single base-10 integer that denotes the maximum number of consecutive 1's in the binary representation of n.

Sample Input 1

5
Sample Output 1

1
Sample Input 2

13
Sample Output 2

2
Explanation

Sample Case 1:
The binary representation of 5_10 is 101_2, so the maximum number of consecutive 1's is 1.

Sample Case 2:
The binary representation of 13_10 is 1101_2, so the maximum number of consecutive 1's is 2.'''

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    rmd = []
    
    while n > 0:
        rm = n % 2
        n = n//2
        rmd.append(rm)
    
    count,result = 0,0
    
    for i in range(0,len(rmd)):
        if rmd[i] == 0:
            count = 0
        else:
            count +=1
            result = max(result,count)
    
    print(result)

'''n=86
c=0
d=0
while n>0:
    if n%2==1:
        c+=1
        if c>d:
            d=c
    else:
        c=0
    n//=2
print(d)'''