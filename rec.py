def stringreverse(s, n):
    if len(s) == n:
        return ""
    return stringreverse(s,n+1)+s[n]


a = stringreverse('nahas', 0)
print(a)


def fact(n):
    if n <= 1:
        return n
    return n*fact(n-1)

a=fact(5)
print(a)


def pali(s):

    def check(s, st, en):
        if st >= en:
            return True
        if s[st] != s[en]:
            return False
        return check(s, st + 1, en - 1)

    return check(s, 0, len(s) - 1)


a = pali('najan')
print(a)