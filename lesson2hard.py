import random
def numbers():
    n = [3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    result = random.choice(n)
    return result
result = numbers()
print(result)
pass2 = []
for i in range(1, 21):
    for j in range(0, 21):
        s1 = i + j
        p1 = [i, j]
        if result % s1 == 0 and j > i:
            pass2.append(p1)
print(*pass2)