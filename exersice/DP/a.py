def fib(n: int, mod: int = None) -> int:
    fibo = (0, 1)
    for _ in range(n):
        fibo = (fibo[1], (fibo[0] + fibo[1]) % mod)

    return fibo[1]


n = int(input())

print(fib(n, 10**9 + 7))
