def fibonacci_normal(num):
    if num == 0:
        return 0
    num1, num2 = 0, 1
    for _ in range(num - 1):  # modified to correct result
        num1, num2 = num2, num1 + num2
    return num2


memo = {}
def fibonacci_memoized(n):
    if n in memo:
        return memo[n]
    if n == 0:
        return 0
    if n == 1 or n == 2:
        return 1
    if n > 2:
        memo[n] = fibonacci_memoized(n - 1) + fibonacci_memoized(n - 2)
    return memo[n]
# def fibonacci_memoized(n):
#     memo = {0: 0, 1: 1}
#     for i in range(2, n + 1):
#         memo[i] = memo[i - 1] + memo[i - 2]
#     return memo[n]
