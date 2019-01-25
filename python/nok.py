def nod(n1, n2):
    if n1 == n2:
        return n1

    d = n1 - n2

    if d < 0:
        d = -d
        div = nod(n1, d)
    else:
        div = nod(n2, d)

    return div

a = int(input())
b = int(input())

print(int(a * b / nod(a, b)))
