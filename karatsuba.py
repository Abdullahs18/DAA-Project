"""
Karatsuba Integer Multiplication - Divide and Conquer
CS2009 - Design and Analysis of Algorithms
"""

import random
import os
import time
import math


def karatsuba(x, y):
    # Base case
    if x < 10 or y < 10:
        return x * y

    # Determine the size of the numbers
    n = max(len(str(abs(x))), len(str(abs(y))))
    m = n // 2

    # Split
    power = 10 ** m
    a, b = divmod(x, power)   # x = a * 10^m + b
    c, d = divmod(y, power)   # y = c * 10^m + d

    # Three recursive multiplications
    ac = karatsuba(a, c)
    bd = karatsuba(b, d)
    ad_bc = karatsuba(a + b, c + d) - ac - bd

    return ac * (10 ** (2 * m)) + ad_bc * (10 ** m) + bd


def brute_force_multiply(x, y):
    return x * y


def generate_large_integer(num_digits, seed=None):
    if seed is not None:
        random.seed(seed)
    if num_digits <= 0:
        return 0
    first = random.randint(1, 9)
    rest = [random.randint(0, 9) for _ in range(num_digits - 1)]
    digits = [first] + rest
    return int("".join(map(str, digits)))


def save_dataset(pairs, filepath):
    with open(filepath, 'w') as f:
        f.write(f"{len(pairs)}\n")
        for x, y in pairs:
            f.write(f"{x}\n{y}\n")


def load_dataset(filepath):
    with open(filepath, 'r') as f:
        n = int(f.readline().strip())
        pairs = []
        for _ in range(n):
            x = int(f.readline().strip())
            y = int(f.readline().strip())
            pairs.append((x, y))
    return pairs


def run_benchmark(x, y):
    start = time.perf_counter()
    result = karatsuba(x, y)
    elapsed = time.perf_counter() - start
    return result, elapsed


if __name__ == "__main__":
    os.makedirs("datasets/karatsuba", exist_ok=True)
    # 10 files with pairs of large integers, varying digit lengths
    digit_sizes = [100, 120, 140, 160, 180, 200, 220, 240, 260, 300]
    for i, d in enumerate(digit_sizes):
        pairs = []
        for j in range(5):  # 5 pairs per file
            seed_val = i * 100 + j
            x = generate_large_integer(d, seed=seed_val)
            y = generate_large_integer(d, seed=seed_val + 50)
            pairs.append((x, y))
        path = f"datasets/karatsuba/input_{i+1}_d{d}.txt"
        save_dataset(pairs, path)

        # Quick verify first pair
        x0, y0 = pairs[0]
        result, t = run_benchmark(x0, y0)
        expected = x0 * y0
        status = "OK" if result == expected else "FAIL"
        print(f"File {i+1}: digits={d}, time={t*1000:.3f}ms, verify={status}")
    print("Done generating Karatsuba datasets.")
