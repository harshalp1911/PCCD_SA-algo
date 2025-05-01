def compute_cost(groups, components, weight_matrix):
    component_map = {c.name: c for c in components}
    cost = 0

    for group in groups:
        for i in range(len(group)):
            for j in range(i + 1, len(group)):
                c1 = component_map[group[i]]
                c2 = component_map[group[j]]

                # Reward stronger connections (higher weight = better)
                weight = weight_matrix[c1.index][c2.index]
                cost -= weight  # higher weight reduces cost

                # Penalize different materials
                if c1.material != c2.material:
                    cost += 10

                # Penalize large volume difference
                cost += abs(c1.volume - c2.volume) / 100

    # Penalty for more groups (to encourage consolidation)
    cost += len(groups) * 5
    return cost
