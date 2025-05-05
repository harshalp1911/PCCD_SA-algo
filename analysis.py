#!/usr/bin/env python3
"""
complexity_analysis.py

Measures and plots time and space complexity of the Simulated Annealing algorithm
using your actual uploaded data, varying the number of SA iterations.
"""
import time
import tracemalloc
import sys

# Guard import for plotting with environment-specific installation hint
try:
    import matplotlib.pyplot as plt
except ImportError:
    print(f"ERROR: matplotlib not installed in this environment.\n"
          f"Run:\n    {sys.executable} -m pip install matplotlib")
    sys.exit(1)

from util import load_components, load_weight_matrix
from simulated_annealing import SimulatedAnnealing


def measure(max_iter, components, weight_matrix,
            initial_temp=100.0, cooling_rate=0.95):
    """
    Runs SA with a given max_iter, returns (runtime_sec, peak_memory_mb).
    """
    sa = SimulatedAnnealing(
        components,
        weight_matrix,
        initial_temp=initial_temp,
        cooling_rate=cooling_rate,
        max_iter=max_iter
    )

    tracemalloc.start()
    t_start = time.perf_counter()
    sa.run()
    t_end = time.perf_counter()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    runtime = t_end - t_start
    peak_mb = peak / (1024 * 1024)
    return runtime, peak_mb


def main():
    # Load actual component data and weight matrix
    components = load_components('components.xlsx')
    weight_matrix = load_weight_matrix('initial_weights.xlsx')

    # Define SA iteration settings to test
    iter_values = [100, 200, 500, 1000, 2000]
    times = []
    memories = []

    print("Measuring complexity for SA max_iter values:", iter_values)
    for it in iter_values:
        t, m = measure(it, components, weight_matrix)
        print(f"max_iter={it}: time={t:.3f}s, memory={m:.2f}MB")
        times.append(t)
        memories.append(m)

    # Plot time complexity
    plt.figure()
    plt.plot(iter_values, times, marker='o')
    plt.xlabel('Max iterations')
    plt.ylabel('Execution time (s)')
    plt.title('Time Complexity vs. SA Iterations')
    plt.grid(True)
    plt.savefig('time_complexity.png')
    print("Saved plot: time_complexity.png")

    # Plot space complexity
    plt.figure()
    plt.plot(iter_values, memories, marker='o')
    plt.xlabel('Max iterations')
    plt.ylabel('Peak memory usage (MB)')
    plt.title('Space Complexity vs. SA Iterations')
    plt.grid(True)
    plt.savefig('space_complexity.png')
    print("Saved plot: space_complexity.png")


if __name__ == '__main__':
    main()
