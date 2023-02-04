note = list(map(int, input().split()))

as_ = [1, 2, 3, 4, 5, 6, 7, 8]
des_ = [8, 7, 6, 5, 4, 3, 2, 1]

if note == as_:
    print("ascending")
elif note == des_:
    print("descending")
else:
    print("mixed")