def FibArray(n):
    a = 0
    b = 1
    for __ in range(n):
        a, b = b, a + b
    return a

def pisano_period(m):
    period = [0]
    for i in range(1, 10000):
        if FibArray(i) != period[0]:
            period.append(FibArray(i) % m)
        if period[i] == 0:
            period.pop()
            break
    return period

def fib_mod(n, m):
    period = pisano_period(m)
    per_len = int(len(pisano_period(m))) 
    index = n % per_len 
    return period[index]
