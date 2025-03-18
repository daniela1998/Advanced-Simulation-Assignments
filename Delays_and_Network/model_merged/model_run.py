from model import BangladeshModel
import pandas as pd
import random

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
run_length = 5 * 24 * 60

scenario = {
    0: {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0},
    1: {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.05},
    2: {'A': 0.0, 'B': 0.0, 'C': 0.05, 'D': 0.1},
    3: {'A': 0.0, 'B': 0.05, 'C': 0.1, 'D': 0.2},
    4: {'A': 0.05, 'B': 0.1, 'C': 0.2, 'D': 0.4},
}

scenario_range = len(scenario)

# To generate the same seeds for each scenario
def generate_seeds(num_seeds, initial_seed):
    random.seed(initial_seed)
    return [random.randint(0, 2**32 - 1) for _ in range(num_seeds)]

# Generate a list of 5 seeds based on an initial seed
initial_seed = 1234567
seeds = generate_seeds(5, initial_seed)

for n in range(scenario_range):
    data_list = []
    for seed in seeds:
        sim_model = BangladeshModel(seed=seed, probabilities = scenario,  scenario = n)

        # One run with given steps
        for i in range(run_length):
            sim_model.step()

        # Get broken bridges and their conditions
        broken_bridges, conditions = sim_model.get_broken_bridges()

data_list.append({
                    'Road': 'N1', # to modify
                    'Scenario': 1,
                    'Seed': seed,
                    'Average_driving_time': sim_model.get_average_driving_time(),
                    'Total_waiting_time': sim_model.get_total_delay_time(),
                    'Average_waiting_time': sim_model.get_average_delay_time(),
                    'Broken_bridges': ', '.join(broken_bridges),
                    'Condition': ', '.join(conditions)  # Add broken bridge conditions
                })  
                
  
df = pd.DataFrame(data_list)

# save to csv
df.to_csv(f'../experiment/scenario{n}.csv', index=False)
