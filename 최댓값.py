def test():
    d = []
    for _ in range(9):
        a = int(input())
        d.append(a)
    print(max(d), d.index(max(d))+1, sep="\n")
    return

test()