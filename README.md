# CS2009 — Divide-and-Conquer Algorithm Implementation

This repository contains the implementation, benchmarking, and visualization of two classical divide-and-conquer algorithms for the CS2009 Design and Analysis of Algorithms course.

## Project Overview
This project provides an experimental evaluation of the **Closest Pair of Points** problem and **Karatsuba Integer Multiplication**. Both algorithms were implemented in pure Python and include an interactive, browser-based graphical interface for visualizing the recursive steps of each algorithm.

## Features
- **Closest Pair of Points**: An $O(n \log n)$ divide-and-conquer implementation.
- **Karatsuba Multiplication**: An $O(n^{1.585})$ divide-and-conquer implementation.
- **Interactive Visualization**: A browser-based GUI (HTML5/CSS3/JavaScript) enabling step-by-step observation of recursive decomposition and subproblem merging.
- **Benchmarking**: Performance analysis conducted across ten input datasets of varying sizes, comparing empirical results against theoretical complexity.

## Algorithms
### 1. Closest Pair of Points
The implementation uses a divide-and-conquer approach that sorts points by x-coordinate and recursively solves subproblems. The merge step identifies the closest pair in a strip of width $2\delta$ around the dividing line, achieving an overall complexity of $T(n) = 2T(n/2) + O(n) = O(n \log n)$.

### 2. Karatsuba Multiplication
This algorithm computes the product of two large $n$-digit integers by reducing four recursive multiplications to three, utilizing the identity: 
$Result = ac \cdot 10^{2m} + (ad+bc) \cdot 10^m + bd$.
This yields a complexity of $T(n) = 3T(n/2) + O(n) = O(n^{1.585})$, significantly outperforming the $O(n^2)$ schoolbook multiplication.

## Getting Started
### Prerequisites
- **Python 3.12** or higher.
- A modern web browser (for the GUI).
- No external numerical libraries are required.

### Running the Visualizer
The graphical interface is located in `gui/visualizer.html`.
1. Open `gui/visualizer.html` in any modern browser.
2. Use the file upload functionality to load dataset files.
3. Use the speed controls or the "Step Forward" button to analyze execution.

### Running Benchmarks
The benchmarking scripts are located in the `algorithms/` directory.
- `algorithms/closest_pair.py`: Run for Closest Pair performance metrics.
- `algorithms/karatsuba.py`: Run for Karatsuba performance metrics.
- The experiments use `time.perf_counter()` for timing.

## Experimental Results
Performance tests were conducted on an Ubuntu 24 Linux environment.
- **Closest Pair**: Empirical data confirmed $O(n \log n)$ growth as input sizes increased from 100 to 600 points.
- **Karatsuba**: Results verified against Python's native multiplication, with timing consistent with $O(n^{1.585})$ theoretical predictions.

## References
- Cormen, T.H., Leiserson, C.E., Rivest, R.L., & Stein, C. (2022). *Introduction to Algorithms*, 4th Edition.
- Karatsuba, A., & Ofman, Y. (1962). *Multiplication of Many-Digital Numbers by Automatic Computers*.
- Kleinberg, J., & Tardos, E. (2005). *Algorithm Design*.
- Levitin, A. (2011). *Introduction to the Design and Analysis of Algorithms*, 3rd Edition.
- Shamos, M.I., & Hoey, D. (1975). *Closest-Point Problems*.
