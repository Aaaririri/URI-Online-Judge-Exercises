i = int(input())
print(f'{i//360} ano(s)')
i = i % 365
print(f'{i//30} mes(es)')
i = i % 30
print(f'{i} dia(s)')