menu = (4.00,4.50, 5.00, 2.00, 1.50)
a,b = map(int, input().split())
c = b * menu[a - 1]
print('Total: R$ %.2f' % c)