n = int(input("Enter any number:"))
remainder = n % 2
set1 = [2, 3, 4, 5]
set2 = list(range(6,21))
if remainder == 1:
    print('Weird')
elif remainder == 0 and n in set1:
    print('Not weird')
elif remainder == 0 and n in set2:
    print('Weird')
elif remainder == 0 and n > 20:
    print('Not weird')
else:
    print('Not weird')
    
