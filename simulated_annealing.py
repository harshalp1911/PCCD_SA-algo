# simulated_annealing.py
import random
import math
from cost_function import compute_cost



class SimulatedAnnealing:
    def __init__(self, components, weight_matrix, initial_temp=100.0, cooling_rate=0.95, max_iter=500):
        self.components = components
        self.weight_matrix = weight_matrix
        self.temperature = initial_temp
        self.cooling_rate = cooling_rate
        self.max_iter = max_iter
        self.current_solution = [[c.name] for c in components]  # start with all separate
        self.best_solution = self.current_solution.copy()
        self.best_cost = compute_cost(self.best_solution, self.components, self.weight_matrix)

    def run(self):
        for _ in range(self.max_iter):
            new_solution = self.perturb(self.current_solution.copy())
            new_cost = compute_cost(new_solution, self.components, self.weight_matrix)
            delta = new_cost - self.best_cost

            if delta < 0 or random.random() < math.exp(-delta / self.temperature):
                self.current_solution = new_solution
                if new_cost < self.best_cost:
                    self.best_solution = new_solution
                    self.best_cost = new_cost

            self.temperature *= self.cooling_rate

        return self.best_solution, self.best_cost

    def perturb(self, solution):
        # Random merge or split operation
        if random.random() < 0.5 and len(solution) > 1:
            # merge two random groups
            i, j = random.sample(range(len(solution)), 2)
            solution[i] += solution[j]
            del solution[j]
        else:
            # split one group
            group_idx = random.randint(0, len(solution) - 1)
            if len(solution[group_idx]) > 1:
                split_point = random.randint(1, len(solution[group_idx]) - 1)
                new_group = solution[group_idx][split_point:]
                solution[group_idx] = solution[group_idx][:split_point]
                solution.append(new_group)
        return solution
