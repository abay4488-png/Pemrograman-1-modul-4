a, b = map(int, input().split())

if a < b:
    print(" - ".join(f"{i} {j}" for i, j in zip(range(a, b + 1), range(b, a - 1, -1))))
    
else:
    print(" - ".join(f"{i} {j}" for i, j in zip(range(a, b - 1, -1), range(b, a + 1))))