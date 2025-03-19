from model import BangladeshModel

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
run_length = 1 * 1 * 5 #run for one hour

# run time 1000 ticks
# run_length = 1000

seed = 1234567

sim_model = BangladeshModel(seed=seed)

# Check if the seed is set
print("SEED " + str(sim_model._seed))

# One run with given steps
for i in range(run_length):
    sim_model.step()

# Print the number of keys in dictionary after all steps
print("Number of paths in path_ids_dict:", len(sim_model.path_ids_dict.keys()))
print("Final path_ids_dict after simulation:", sim_model.path_ids_dict.keys())
