def gcd(a, b):
    if a == 0:
        return b
    if b == 0:
        return a
    if a >= b:
        return gcd(a % b, b)
    elif b >= a:
        return gcd(a, b % a)

print(gcd(48, 32))