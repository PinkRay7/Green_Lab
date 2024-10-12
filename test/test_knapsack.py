import pytest
from source.knapsack_bf import knapsack_bf_solver

def test_knapsack_basic():
    values = [300, 200, 400, 500]
    weights = [2, 1, 5, 3]

    assert knapsack_bf_solver(10, len(values), values, weights) == 1200
    assert knapsack_bf_solver(5, len(values) - 1, values, weights) == 500
    assert knapsack_bf_solver(0, len(values), values, weights) == 0
    assert knapsack_bf_solver(10, 0, values, weights) == 0