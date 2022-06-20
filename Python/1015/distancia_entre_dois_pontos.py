p1 = tuple(map(float, input().split()))
p2 = tuple(map(float, input().split()))
r = ((p2[0]-p1[0]) ** 2 + (p2[1]-p1[1]) ** 2) ** 0.5
print(f'{r:.4f}')