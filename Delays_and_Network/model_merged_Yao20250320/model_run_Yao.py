from model import BangladeshModel
import pandas as pd

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
run_length = 1 * 24 * 60

scenario = {
    0: {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0},
    1: {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.05},
    2: {'A': 0.0, 'B': 0.0, 'C': 0.05, 'D': 0.1},
    3: {'A': 0.0, 'B': 0.05, 'C': 0.1, 'D': 0.2},
    4: {'A': 0.05, 'B': 0.1, 'C': 0.2, 'D': 0.4},
}

# run time 1000 ticks
# run_length = 1000

seed = 1234567

sim_model = BangladeshModel(seed=seed, probabilities = scenario,  scenario = 0)

# Check if the seed is set
print("SEED " + str(sim_model._seed))

data_list = []

# One run with given steps
for i in range(run_length):
    sim_model.step()

data_list.append({
                    'Road': 'N1', # to modify
                    'Scenario': 0,
                    'Seed': seed,
                    'Average_driving_time': sim_model.get_average_driving_time(),
                    'Total_waiting_time': sim_model.get_total_delay_time(),
                    'Average_waiting_time': sim_model.get_average_delay_time(),
                    'Broken_bridges': ', '.join(sim_model.get_broken_bridges()),
                    'Average_truck_speeds': sim_model.get_truck_speeds()

                })

df = pd.DataFrame(data_list)

# save to csv
df.to_csv(f'../experiment/scenario{00}.csv', index=False)

