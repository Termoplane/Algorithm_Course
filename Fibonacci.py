def FibArray(n):
    F = [0 for i in range(n + 1)]
    F[1] = 1
    for i in range(n + 1)[2: n + 1]:
        F[i] = F[i - 1] + F[i - 2]
    return F[n]

n = int(input())

print(FibArray(n))