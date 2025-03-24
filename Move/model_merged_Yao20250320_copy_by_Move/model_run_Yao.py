from model import BangladeshModel
import pandas as pd
import networkx as nx

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
df.to_csv(f'experiment/scenario{00}.csv', index=False)

# save sim_model.self.path_ids_dict to txt
with open(f'experiment/path_ids_dict.txt', 'w') as f:
    for key, value in sim_model.path_ids_dict.items():
        f.write(f'{key}: {value}\n')
#---------------------------------------------------------------
def get_node_coordinates(node_id):
    # Load the CSV file
    df = pd.read_csv('demo_with_intersection.csv')
    
    # Find the row with the given node_id
    node_row = df[df['node_id'] == node_id]
    
    # Extract the coordinates
    if not node_row.empty:
        x_coord = node_row.iloc[0]['x_coord']
        y_coord = node_row.iloc[0]['y_coord']
        return (x_coord, y_coord)
    else:
        raise ValueError(f"Node ID {node_id} not found in the CSV file.")

# Add the function to the sim_model
BangladeshModel.get_node_coordinates = get_node_coordinates

import matplotlib.pyplot as plt

# save sim_model.self.path_ids_dict to txt
with open(f'experiment/path_ids_dict.txt', 'w') as f:
    for key, value in sim_model.path_ids_dict.items():
        f.write(f'{key}: {value}\n')

# Plot spatial paths
plt.figure(figsize=(10, 8))

'''# Assuming sim_model has a method to get coordinates of nodes
for key, value in sim_model.path_ids_dict.items():
    for path in value:
        x_coords = [sim_model.get_node_coordinates(node)[0] for node in path]
        y_coords = [sim_model.get_node_coordinates(node)[1] for node in path]
        plt.plot(x_coords, y_coords, marker='o')'''

plt.title('Spatial Paths in the Simulation')
plt.xlabel('X Coordinate')
plt.ylabel('Y Coordinate')
plt.savefig(f'experiment/spatial_paths.png')
plt.show()