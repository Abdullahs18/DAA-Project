"""
Closest Pair of Points - Divide and Conquer
CS2009 - Design and Analysis of Algorithms
"""

import math
import random
import os
import json
import time


def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def brute_force_closest(points):
    min_dist = float('inf')
    pair = None
    n = len(points)
    for i in range(n):
        for j in range(i + 1, n):
            d = distance(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair


def strip_closest(strip, d):
    min_dist = d
    pair = None
    strip.sort(key=lambda p: p[1])
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and (strip[j][1] - strip[i][1]) < min_dist:
            d_ij = distance(strip[i], strip[j])
            if d_ij < min_dist:
                min_dist = d_ij
                pair = (strip[i], strip[j])
            j += 1
    return min_dist, pair


def closest_pair_rec(pts_sorted_x):
    n = len(pts_sorted_x)
    if n <= 3:
        return brute_force_closest(pts_sorted_x)

    mid = n // 2
    mid_point = pts_sorted_x[mid]

    left_half = pts_sorted_x[:mid]
    right_half = pts_sorted_x[mid:]

    d_left, pair_left = closest_pair_rec(left_half)
    d_right, pair_right = closest_pair_rec(right_half)

    if d_left < d_right:
        d = d_left
        best_pair = pair_left
    else:
        d = d_right
        best_pair = pair_right

    strip = [p for p in pts_sorted_x if abs(p[0] - mid_point[0]) < d]
    d_strip, strip_pair = strip_closest(strip, d)

    if d_strip < d:
        return d_strip, strip_pair
    return d, best_pair


def closest_pair(points):
    pts = sorted(points, key=lambda p: p[0])
    return closest_pair_rec(pts)


def generate_dataset(n, seed=None):
    if seed is not None:
        random.seed(seed)
    points = [(round(random.uniform(-1000, 1000), 4),
               round(random.uniform(-1000, 1000), 4)) for _ in range(n)]
    return points


def save_dataset(points, filepath):
    with open(filepath, 'w') as f:
        f.write(f"{len(points)}\n")
        for p in points:
            f.write(f"{p[0]} {p[1]}\n")


def load_dataset(filepath):
    with open(filepath, 'r') as f:
        n = int(f.readline().strip())
        points = []
        for _ in range(n):
            x, y = map(float, f.readline().strip().split())
            points.append((x, y))
    return points


def run_benchmark(points):
    start = time.perf_counter()
    dist, pair = closest_pair(points)
    elapsed = time.perf_counter() - start
    return dist, pair, elapsed


if __name__ == "__main__":
    os.makedirs("datasets/closest_pair", exist_ok=True)
    sizes = [100, 150, 200, 250, 300, 350, 400, 450, 500, 600]
    for i, sz in enumerate(sizes):
        pts = generate_dataset(sz, seed=i * 42)
        path = f"datasets/closest_pair/input_{i+1}_n{sz}.txt"
        save_dataset(pts, path)
        dist, pair, t = run_benchmark(pts)
        print(f"File {i+1}: n={sz}, min_dist={dist:.6f}, time={t*1000:.3f}ms")
        print(f"  Pair: {pair}")
    print("Done generating closest pair datasets.")
