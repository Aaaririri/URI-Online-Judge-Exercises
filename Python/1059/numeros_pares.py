b = 0
c = 0
for i in range(6):
    a = float(input())
    if a > -1:
        b += 1 
        c += a


print(f'{b} valores positivos')
print(f'{c/b:.1f}')

