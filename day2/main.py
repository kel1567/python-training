a = int(input())
b = int(input())
c = int(input())
if a == 0 and b == 0 and c == 0:
    print(0)
else:
    if a == 0:
        a = 1
    if b == 0:
        b = 1
    if c == 0:
        c = 1
    print(a * b * c)
