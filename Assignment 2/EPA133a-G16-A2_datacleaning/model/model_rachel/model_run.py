from model import BangladeshModel

"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
# run_length = 5 * 24 * 60

# run time (ticks)
run_length = 7200

seed = 1234567

sim_model = BangladeshModel(seed=seed)

# Check if the seed is set
print("SEED " + str(sim_model._seed))

# One run with given steps
for i in range(run_length):
    sim_model.step()

average_time = sim_model.get_average_driving_time()
print(f"Average driving time: {average_time} mins")

bridge_delay = sim_model.get_biggest_bridge_delay()
print(f"Bridge with biggest delays: {bridge_delay}")

total_delay = sim_model.get_total_delay_time()
print(f"Total delay time: {total_delay} minutes")

average_delay = sim_model.get_average_delay_time()
print(f"Average delay time per truck: {average_delay} minutes")

broken_bridges = sim_model.get_broken_bridges()
print(f"Broken bridges: {broken_bridges}")
