def triangle(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 0

    if a+b <= c or a+c <= b or b+c <= a:
        return 0

    if a==b==c:
        return 1

    return 2


a = 1
b = 0
c = 0
print(triangle(a,b,c))