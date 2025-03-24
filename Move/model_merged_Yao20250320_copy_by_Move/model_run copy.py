from model import BangladeshModel
import pandas as pd
import random
import numpy as np
"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
days = 1
run_length = 1 * 60 * days

scenario = {
    0: {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0},
    1: {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.05},
    2: {'A': 0.0, 'B': 0.0, 'C': 0.05, 'D': 0.1},
    3: {'A': 0.0, 'B': 0.05, 'C': 0.1, 'D': 0.2},
    4: {'A': 0.05, 'B': 0.1, 'C': 0.2, 'D': 0.4},
}

scenario_range = 5
replications = 5
# To generate the same seeds for each scenario
#def generate_seeds(num_seeds, initial_seed):
 #   random.seed(initial_seed)
  #  return [random.randint(0, 2**32 - 1) for _ in range(num_seeds)]

seeds = (np.random.randint(100000, 999999, size=replications)) # 5 scenarios

# Generate a list of 5 seeds based on an initial seed
#initial_seed = 1234567
#seeds = generate_seeds(5, initial_seed)
#seeds = [1,2,3,4,5,6,7]

for n in range(scenario_range):

    data_list = []
    
    for seed in seeds:
        sim_model = BangladeshModel(seed=int(seed), probabilities=scenario, scenario=n)

        for i in range(run_length):
            sim_model.step()

        data_list.append({
                    'Scenario': n,
                    'Seed': seed,
                    'Average_driving_time': sim_model.get_average_driving_time(),
                    'Total_waiting_time': sim_model.get_total_delay_time(),
                    'Average_waiting_time': sim_model.get_average_delay_time(),
                    'Categories'    : ', '.join(sim_model.condition_list),
                    'Broken_bridges': ', '.join(sim_model.get_broken_bridges()),
                    'Average Speed': sim_model.get_truck_speeds()
                })

        df = pd.DataFrame(data_list)

        # save to csv
        df.to_csv(f'../experiment/scenario{n}.csv', index=False)
