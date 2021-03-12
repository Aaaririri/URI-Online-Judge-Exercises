d0 = input().split()
d0 = int(d0[1])
t0 = list(map(int, input().split(" : ")))
df = input().split()
df = int(df[1])
tf = list(map(int, input().split(" : ")))
dr = df - d0
tr = [tf[0]-t0[0],tf[1]-t0[1],tf[2]-t0[2]]

if tr[2] < 0:
    tr[2] = 60 + tr[2]
    tr[1] = tr[1] - 1 
 
if tr[1] < 0:
    tr[1] = 60 + tr[1]
    tr[0] = tr[0] - 1  

if tr[0] < 0:
    tr[0] = 24 + tr[0]
    dr = dr - 1  

print(f'{dr} dia(s)')
print(f'{tr[0]} hora(s)')
print(f'{tr[1]} minuto(s)')
print(f'{tr[2]} segundo(s)')