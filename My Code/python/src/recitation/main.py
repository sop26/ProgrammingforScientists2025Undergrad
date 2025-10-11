"""
main.py — simple combination function with built-in tests.

First, install pytest
    pip install pytest (Windows)
    pip3 install pytest (macOS/Linux)

Run tests with:
    python -m pytest main.py (Windows)
    python3 -m pytest main.py (macOS/Linux)
"""

def combination(n: int, k: int) -> int:
    """Return C(n, k) with basic input validation."""
    if not isinstance(n, int) or not isinstance(k, int):
        raise TypeError("n and k must be integers")
    if n < 0 or k < 0:
        raise ValueError("n and k must be non-negative")
    if k > n:
        raise ValueError("k cannot be greater than n")

    # symmetry
    if k > n - k:
        k = n - k

    if k == 0 or k == n:
        return 1
    if k == 1:
        return n

    result = 1
    i = 1
    while i <= k:   
        result = (result * (n - k + i)) // i
        i = i + 1
    return result


# def test_bray_cutis():
#     s1 = {"penguins": 5, "pirates": 10, "steelers": 2, "riverhands": 0}
#     s2 = {"penguins": 20, "pirates": 8, "steelers": 500, "riverhands": 0}
#     assert approx_equal(bray_curtis_distance(s1, s2), 0.94485)
    
# def approx_equal(a, b):
#     return abs(a-b) <= 1e-5

# -------------------------
# Pytest tests live here too
# -------------------------

def test_combination_all():
    # Each tuple is (n, k, expected)
    cases = [
        (10, 0, 1),
        (10, 10, 1),
        (12, 1, 12),
        (8, 7, 8),
        (10, 4, 210),
        (10, 6, 210),
    ]

    i = 0
    while i < len(cases):   
        n, k, expected = cases[i]
        actual = combination(n, k)
        assert actual == expected, f"case {i} failed: C({n},{k})={actual}, expected {expected}"
        i = i + 1
    print("passed all tests!")