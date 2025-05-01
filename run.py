print("▶️  run.py starting…")
from util import load_components, load_weight_matrix
from simulated_annealing import SimulatedAnnealing

COMPONENT_FILE = "components.xlsx"
WEIGHT_FILE = "initial_weights.xlsx"

def main():
    print("▶️  inside main()")
    components = load_components(COMPONENT_FILE)
    weight_matrix = load_weight_matrix(WEIGHT_FILE)

    # DEBUG PRINT EXAMPLE 1
    print("Loaded Components:")
    for c in components:
        print(c.name)
    
    print("\nWeight Matrix Shape:", weight_matrix.shape)



    # SA algorithm function call
    sa = SimulatedAnnealing(components, weight_matrix,
                            initial_temp=100.0,
                            cooling_rate=0.95,
                            max_iter=500)

    best_solution, best_cost = sa.run()
    print("\nBest Grouping Found:")
    for group in best_solution:
        print(group)
    print(f"\nTotal Cost: {best_cost:.2f}")

if __name__ == "__main__":
    main()

