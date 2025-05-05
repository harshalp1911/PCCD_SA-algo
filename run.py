
try:
    import pandas as pd
except ImportError:
    print("ERROR: pandas (and openpyxl) not installed. Run:\n    pip install pandas openpyxl")
    exit(1)

import os
import pandas as pd
from component import Component
from util import load_components, load_weight_matrix
from simulated_annealing import SimulatedAnnealing
from cost_function import compute_cost

def main():
    # Debug info
    print(f"▶️ run.py executing: {__file__}")
    print(f"▶️ Working directory: {os.getcwd()}\n")

    # Locate input files
    script_dir      = os.path.dirname(os.path.abspath(__file__))
    components_file = os.path.join(script_dir, 'components.xlsx')
    weights_file    = os.path.join(script_dir, 'initial_weights.xlsx')

    # --- Print raw input data ---
    df_comp = pd.read_excel(components_file, header=None)
    print("▶️ Raw components.xlsx data:")
    print(df_comp.to_string(index=False), "\n")

    df_wt = pd.read_excel(weights_file, header=None)
    print("▶️ Raw initial_weights.xlsx data:")
    print(df_wt.to_string(index=False), "\n")

    # --- Load into your objects/matrices ---
    components    = load_components(components_file)
    weight_matrix = load_weight_matrix(weights_file)

    print(f"Loaded {len(components)} components.")
    print(f"Weight matrix shape: {weight_matrix.shape}\n")

    # Configure and run SA
    sa = SimulatedAnnealing(
        components,
        weight_matrix,
        initial_temp=100.0,
        cooling_rate=0.95,
        max_iter=1000
    )
    best_solution, best_cost = sa.run()

    # Output results
    print("▶️ Final Groups:")
    for group in best_solution:
        print(" ", group)
    print(f"\nTotal Cost: {best_cost:.2f}\n")

    # Highlight best 2-part merge
    two_part = [g for g in best_solution if len(g) == 2]
    if two_part:
        a, b = two_part[0]
        print(f"Best pair to merge: {a} ↔ {b}")
    else:
        print("No 2-component groups found.")

if __name__ == "__main__":
    main()
