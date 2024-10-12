import pytest
from source.coinchange_mem import coinChange

def test_coin_change_basic():
    coins = [1, 2, 5]
    amount = 11
    expected = 3  # 11 = 5 + 5 + 1
    assert coinChange(coins, amount) == expected

def test_coin_change_no_coins():
    coins = []
    amount = 5
    expected = -1  # 不能组成任何金额
    assert coinChange(coins, amount) == expected

def test_coin_change_zero_amount():
    coins = [1, 2, 5]
    amount = 0
    expected = 0  # 0金额不需要任何硬币
    assert coinChange(coins, amount) == expected

def test_coin_change_exact_coins():
    coins = [1, 2, 5]
    amount = 5
    expected = 1  # 5可以用1个5元硬币组成
    assert coinChange(coins, amount) == expected

def test_coin_change_impossible():
    coins = [2]
    amount = 3
    expected = -1  # 3无法用面额为2的硬币组成
    assert coinChange(coins, amount) == expected

def test_coin_change_large_amount():
    coins = [1, 3, 4]
    amount = 6
    expected = 2  # 6 = 3 + 3
    assert coinChange(coins, amount) == expected
