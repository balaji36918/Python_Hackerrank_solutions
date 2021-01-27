"""
#Using while statement
n = int(input())
i = 1
while i<= n:
    print(i, end = "")
    i = i + 1
    
"""

#Using an Identifier
n = int(input())
print(*range(1, n+1), sep="")
