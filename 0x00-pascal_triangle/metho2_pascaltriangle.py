from math import factorial
"""ncr = n!/r!(n-r)!
"""

rows = int(input("Enter the number of rows: "))

for n in range(rows):
    for space in range(1, rows - n):
        print(end=' ')
    
    for r in range(n+1):
        ncr = factorial(n) // (factorial(r) * factorial(n - r))
        print(ncr, end=' ')
        
    print('')
        