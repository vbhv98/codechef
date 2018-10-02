n, k = list(map(int, input().split()))

if n <= k:
    print(1)
else:
    a = [1]*n
    prev = k
    for i in range(k, n):
        a[i] = prev
        prev = (prev*2 - a[i-k])%1000000007
    print(a[-1])
