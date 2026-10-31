masukan = input().split()
kelipatan = int(masukan[0])
simbol = masukan[1]

for i in range(1, 51, 1):
    if i % kelipatan == 0 :
        print(simbol, end=" ")
    else :
        print(i, end=" ")