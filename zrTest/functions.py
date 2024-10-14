import functools

# general memoize decorator
def memoize(func):
    cache = {}
    @functools.wraps(func)
    def memoized_func(*args):
        if args in cache:
            return cache[args]
        else:
            result = func(*args)
            cache[args] = result
            return result
    memoized_func.cache = cache
    return memoized_func

# unhashable 
def memoize_unhashable(func):
    cache = {}
    @functools.wraps(func)
    def memoized_func(*args):
        key = tuple((tuple(arg) if isinstance(arg, list) else arg) for arg in args)
        if key in cache:
            return cache[key]
        else:
            result = func(*args)
            cache[key] = result
            return result
    return memoized_func

# 1. Fibonacci sequence
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

fibonacci_memo = memoize(fibonacci)
# test
def test_fibonacci():
    n = 10
    print("Fibonacci without memoization:", fibonacci(n))
    print("Fibonacci with memoization:", fibonacci_memo(n))



# 2. 0-1 Knapsack problem
def knapsack(W, n, weights, values):
    if n == 0 or W == 0:
        return 0
    if weights[n - 1] > W:
        return knapsack(W, n - 1, weights, values)
    else:
        return max(
            values[n - 1] + knapsack(W - weights[n - 1], n - 1, weights, values),
            knapsack(W, n - 1, weights, values)
        )

knapsack_memo = memoize(knapsack)
# test
def test_knapsack():
    weights = (10, 20, 30)
    values = (60, 100, 120)
    W = 50
    n = len(weights)
    print("Knapsack without memoization:", knapsack(W, n, weights, values))
    print("Knapsack with memoization:", knapsack_memo(W, n, weights, values))



# 3. Coin Change problem
def coin_change(m, n, coins):
    if n == 0:
        return 1
    if n < 0 or m <= 0:
        return 0
    return coin_change(m - 1, n, coins) + coin_change(m, n - coins[m - 1], coins)

coin_change_memo = memoize(coin_change)
#test
def test_coin_change():
    coins = (1, 2, 3)
    m = len(coins)
    n = 4  
    print("Coin Change without memoization:", coin_change(m, n, coins))
    print("Coin Change with memoization:", coin_change_memo(m, n, coins))



# 4. Levenshtein Distance
def levenshtein_distance(s1, s2, m, n):
    if m == 0:
        return n
    if n == 0:
        return m
    if s1[m - 1] == s2[n - 1]:
        cost = 0
    else:
        cost = 1
    return min(
        levenshtein_distance(s1, s2, m - 1, n) + 1,
        levenshtein_distance(s1, s2, m, n - 1) + 1,
        levenshtein_distance(s1, s2, m - 1, n - 1) + cost
    )

levenshtein_distance_memo = memoize(levenshtein_distance)
#test
def test_levenshtein_distance():
    s1 = "kitten"
    s2 = "sitting"
    m = len(s1)
    n = len(s2)
    print("Levenshtein Distance without memoization:", levenshtein_distance(s1, s2, m, n))
    print("Levenshtein Distance with memoization:", levenshtein_distance_memo(s1, s2, m, n))



# 5. Factorial calculation
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

factorial_memo = memoize(factorial)
#test
def test_factorial():
    n = 5
    print("Factorial without memoization:", factorial(n))
    print("Factorial with memoization:", factorial_memo(n))



# 6. Matrix Chain Multiplication
def matrix_chain_order(i, j, dimensions):
    if i == j:
        return 0
    min_count = float('inf')
    for k in range(i, j):
        count = (
            matrix_chain_order(i, k, dimensions)
            + matrix_chain_order(k + 1, j, dimensions)
            + dimensions[i - 1] * dimensions[k] * dimensions[j]
        )
        if count < min_count:
            min_count = count
    return min_count

matrix_chain_order_memo = memoize(matrix_chain_order)
#test
def test_matrix_chain_order():
    dimensions = (1, 2, 3, 4)
    n = len(dimensions) - 1
    print("Matrix Chain Order without memoization:", matrix_chain_order(1, n, dimensions))
    print("Matrix Chain Order with memoization:", matrix_chain_order_memo(1, n, dimensions))




# 7. Can I Win game
def can_i_win(max_int, desired_total):
    if desired_total <= 0:
        return True
    if (max_int * (max_int + 1)) // 2 < desired_total:
        return False

    memo = {}
    def can_win(used, total):
        if used in memo:
            return memo[used]
        for i in range(max_int):
            curr = 1 << i
            if not used & curr:
                if total + i + 1 >= desired_total:
                    memo[used] = True
                    return True
                if not can_win(used | curr, total + i + 1):
                    memo[used] = True
                    return True
        memo[used] = False
        return False

    return can_win(0, 0)
#test
def test_can_i_win():
    max_int = 10
    desired_total = 11
    print("Can I Win:", can_i_win(max_int, desired_total))



# 8. K-equal sum array partitions
def can_partition_k_subsets(nums, k):
    total_sum = sum(nums)
    if total_sum % k != 0:
        return False
    target = total_sum // k
    nums.sort(reverse=True)
    used = [False] * len(nums)

    @memoize_unhashable
    def backtrack(k, index, current_sum, used):
        if k == 1:
            return True
        if current_sum == target:
            return backtrack(k - 1, 0, 0, used)
        for i in range(index, len(nums)):
            if not used[i] and current_sum + nums[i] <= target:
                used[i] = True
                if backtrack(k, i + 1, current_sum + nums[i], used):
                    return True
                used[i] = False
        return False

    return backtrack(k, 0, 0, used)
#test
def test_can_partition_k_subsets():
    nums = [4, 3, 2, 3, 5, 2, 1]
    k = 4
    print("Can Partition K Subsets:", can_partition_k_subsets(nums, k))



# 9. All Possible Full Binary Trees
class TreeNode:
    def __init__(self, val=0):
        self.val = val
        self.left = None
        self.right = None

def all_possible_fbt(N):
    if N % 2 == 0:
        return []
    if N == 1:
        return [TreeNode(0)]
    result = []
    for left_nodes in range(1, N, 2):
        right_nodes = N - 1 - left_nodes
        left_trees = all_possible_fbt_memo(left_nodes)
        right_trees = all_possible_fbt_memo(right_nodes)
        for left in left_trees:
            for right in right_trees:
                node = TreeNode(0)
                node.left = left
                node.right = right
                result.append(node)
    return result

all_possible_fbt_memo = memoize(all_possible_fbt)
#test
def test_all_possible_fbt():
    N = 7
    trees = all_possible_fbt(N)
    print("Number of Full Binary Trees without memoization:", len(trees))
    memo_trees = all_possible_fbt_memo(N)
    print("Number of Full Binary Trees with memoization:", len(memo_trees))




