'''Consider a database table, Emails, which has the attributes First Name and Email ID. Given n rows of data simulating the Emails table, print an alphabetically-ordered list of people whose email address ends in @gmail.com.
Sample Input

6
riya riya@gmail.com
julia julia@julia.me
julia sjulia@gmail.com
julia julia@gmail.com
samantha samantha@gmail.com
tanya tanya@gmail.com
Sample Output

julia
julia
riya
samantha
tanya'''

import os
import random
import re
import sys



if __name__ == '__main__':
    N = int(input().strip())
    nw=[]
    for N_itr in range(N):
        first_multiple_input = input().rstrip().split()

        firstName = first_multiple_input[0]

        emailID = first_multiple_input[1]
        if '@gmail.com' in emailID:
            nw.append(firstName)
    
    nw = sorted(nw)
    for item in nw:
        print(item)