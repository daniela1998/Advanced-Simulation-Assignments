import csv
import pandas as pd
from model import BangladeshModel

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
# run_length = 5 * 24 * 60

# Probabilities
scenario_probabilities = {
    1: {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.05},
    2: {'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.10},
    3: {'A': 0.0, 'B': 0.0, 'C': 0.05, 'D': 0.10},
    4: {'A': 0.0, 'B': 0.0, 'C': 0.10, 'D': 0.20},
    5: {'A': 0.0, 'B': 0.05, 'C': 0.10, 'D': 0.20},
    6: {'A': 0.0, 'B': 0.10, 'C': 0.20, 'D': 0.40},
    7: {'A': 0.05, 'B': 0.10, 'C': 0.20, 'D': 0.40},
    8: {'A': 0.10, 'B': 0.20, 'C': 0.40, 'D': 0.80}
}

# run time 1000 ticks
run_length = 1000

seed = 123

sim_model = BangladeshModel(seed=seed, probabilities = scenario_probabilities, scenario = 1 )

# Check if the seed is set
print("SEED " + str(sim_model._seed))

# One run with given steps
for i in range(run_length):
    sim_model.step()

# Collect bridge data
truck_data = sim_model.collect_truck_data()


# Write data to a CSV file
with open('truck_data.csv', 'w', newline='') as f:
    writer = csv.DictWriter(f, fieldnames=['unique_id',  'driving_time'])
    writer.writeheader()
    print(bridge_data)
    for data in bridge_data:
        writer.writerow(data)

print("Truck data has been written to bridge_data.csv")
