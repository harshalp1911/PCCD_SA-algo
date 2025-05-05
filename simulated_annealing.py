# simulated_annealing.py
import random
import math
from cost_function import compute_cost

class SimulatedAnnealing:
    def __init__(self, components, weight_matrix,
                 initial_temp=100.0, cooling_rate=0.95, max_iter=500):
        self.components     = components
        self.weight_matrix  = weight_matrix
        self.temperature    = initial_temp
        self.cooling_rate   = cooling_rate
        self.max_iter       = max_iter

        # start with each component on its own
        self.current_solution = [[c.name] for c in components]
        self.best_solution    = [grp.copy() for grp in self.current_solution]

    def run(self):
        current_cost = compute_cost(
            self.current_solution, self.components, self.weight_matrix
        )
        best_cost = current_cost

        for _ in range(self.max_iter):
            # propose a small change
            candidate = self._perturb(
                [grp.copy() for grp in self.current_solution]
            )
            cand_cost = compute_cost(candidate, self.components, self.weight_matrix)
            Δ = cand_cost - current_cost

            # accept if better or with Metropolis probability
            if Δ < 0 or random.random() < math.exp(-Δ / self.temperature):
                self.current_solution = candidate
                current_cost = cand_cost

            # record new best
            if current_cost < best_cost:
                self.best_solution = [grp.copy() for grp in self.current_solution]
                best_cost = current_cost

            # cool down
            self.temperature *= self.cooling_rate

        return self.best_solution, best_cost

    def _perturb(self, solution):
        # 50/50 merge vs. split
        if random.random() < 0.5 and len(solution) > 1:
            # merge two random groups
            i, j = random.sample(range(len(solution)), 2)
            solution[i] += solution[j]
            del solution[j]
        else:
            # split one group
            idx = random.randint(0, len(solution) - 1)
            group = solution[idx]
            if len(group) > 1:
                sp = random.randint(1, len(group) - 1)
                new_grp = group[sp:]
                solution[idx] = group[:sp]
                solution.append(new_grp)
        return solution
