i = 0
while(i<2):
    for j in range(1,4):
        if i != 0 and i != 1 and i < 1.8 :
            print(f'I={i:.1f} J={j+i:.1f}')
        else:
            print(f'I={i:.0f} J={j+i:.0f}')
    i = i + 0.2


 