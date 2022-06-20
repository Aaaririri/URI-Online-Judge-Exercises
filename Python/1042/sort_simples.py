n = list(map(int, input().split()))
n_auxiliar = n.copy()
n.sort()

for i in n:
    print(i)
    
print()    

for i in n_auxiliar:
    print(i)