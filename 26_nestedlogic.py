'''Your local library needs your help! Given the expected and actual return dates for a library book, create a program that calculates the fine (if any). The fee structure is as follows:

If the book is returned on or before the expected return date, no fine will be charged (i.e.: fine=0) .
If the book is returned after the expected return day but still within the same calendar month and year as the expected return date, fine=15 Hackos * (the no.of days late).
If the book is returned after the expected return month but still within the same calendar year as the expected return date, the fine=500 Hackos * (the no.of months lates).
If the book is returned after the calendar year in which it was expected, there is a fixed fine of 10000 Hackos.

Sample Input

STDIN       Function
-----       --------
9 6 2015    day = 9, month = 6, year = 2015 (date returned)
6 6 2015    day = 6, month = 6, year = 2015 (date due)
Sample Output

45'''

n = input()
x = list(map(int, n.split()))
m = input()
y = list(map(int, m.split()))
z=0
if y[2] < x[2]:
    z = 10000
elif y[2] == x[2]:
    if y[1] < x[1]:
        z = 500*(x[1]-y[1])
    elif y[0] < x[0]:
        z = 15*(x[0]-y[0])

print(z)