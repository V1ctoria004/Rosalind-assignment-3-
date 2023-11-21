from itertools import product

input_str = 'A B C D E F'
characters = input_str.replace(' ', '')
result = []

for perm in product(characters, repeat = 3):
    result.append(''.join(perm))

for item in result:
    print(item)