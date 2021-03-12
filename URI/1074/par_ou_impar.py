i = int(input())
for j in range(0,i):
    x = int(input())
    if x == 0:
        print('NULL')
    elif x%2 != 0 and x > 0:
        print('ODD POSITIVE')
    elif x%2 != 0 and x < 0:
        print('ODD NEGATIVE')
    elif x%2 == 0 and x > 0:
        print('EVEN POSITIVE')
    elif x%2 == 0 and x < 0:
        print('EVEN NEGATIVE')