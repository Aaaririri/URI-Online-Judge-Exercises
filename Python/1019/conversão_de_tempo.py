a = int(input())
h = 0
m = 0
s = 0
while(a>= 3600):
    a = a - 3600
    h = h + 1


while(a>=60):
    a = a - 60
    m = m + 1

s = a
print(f'{h}:{m}:{s}')
