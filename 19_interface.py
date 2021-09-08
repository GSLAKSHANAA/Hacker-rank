'''The AdvancedArithmetic interface and the method declaration for the abstract divisorSum(n) method are provided for you in the editor below.

Complete the implementation of Calculator class, which implements the AdvancedArithmetic interface. The implementation for the divisorSum(n) method must return the sum of all divisors of n.
Sample Input

6
Sample Output

I implemented: AdvancedArithmetic
12
Explanation

The integer 6 is evenly divisible by ,1,2,3 and 6. Our divisorSum method should return the sum of these numbers, which is 1+2+3+6=12. The Solution class then prints 
I implemented: AdvancedArithmetic on the first line, followed by the sum returned by divisorSum (which is 12) on the second line.'''

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError
class Calculator(AdvancedArithmetic):
    def divisorSum(self, n):
        temp = []
        for i in range(1, n+1):
            if n%i == 0:
                temp.append(i)
        return sum(temp)


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)