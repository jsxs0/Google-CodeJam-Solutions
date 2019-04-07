MAX_BIT = 5


def generate(ans, i):
    ret = 0
    for j in range(MAX_BIT):
        ret += (1 << j) if ans[j][i] == '1' else 0
    return ret


def doit(n, b):
    ans = []
    ret = []
    for i in range(MAX_BIT):
        test_pattern = ''
        k = 1 << i
        for j in range(n):
            test_pattern += '1' if j & k else '0'
        print(test_pattern)
        ans.append(input().split()[0])
    k = 0
    for i in range(n):
        if(k >= (n-b) or generate(ans, k) != i % (1 << (MAX_BIT))):
            ret.append(i)
        else:
            k += 1
    return [str(i) for i in ret]


t = int(input())  # read a line with a single integer
for i in range(1, t + 1):
    x = [int(s) for s in input().split()]
    print(' '.join(doit(x[0], x[1])))
    assert input() == '1'
