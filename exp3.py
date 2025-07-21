import math
import random

def objective_function(x):
    return x ** 2

def neighbor(x):
    return x + random.uniform(-1, 1)


def simulated_annealing(initial_temp, cooling_rate, stopping_temp, max_iterations):
    current_x = random.uniform(-10, 10) 
    current_energy = objective_function(current_x)

    best_x = current_x
    best_energy = current_energy

    temperature = initial_temp
    iteration = 0

    while temperature > stopping_temp and iteration < max_iterations:
        new_x = neighbor(current_x)
        new_energy = objective_function(new_x)

        delta_energy = new_energy - current_energy

        if delta_energy < 0 or random.uniform(0, 1) < math.exp(-delta_energy / temperature):
            current_x = new_x
            current_energy = new_energy

            if current_energy < best_energy:
                best_x = current_x
                best_energy = current_energy

        temperature *= cooling_rate
        iteration += 1

    return best_x, best_energy

best_solution, best_value = simulated_annealing(
    initial_temp=1000, cooling_rate=0.95, stopping_temp=1e-8, max_iterations=1000
)

print("Best solution (x):", best_solution)
print("Best value (f(x)):", best_value)
