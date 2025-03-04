from model import BangladeshModel
import pandas as pd
"""
    Run simulation
    Print output at terminal
"""

# ---------------------------------------------------------------

# run time 5 x 24 hours; 1 tick 1 minute
# run_length = 5 * 24 * 60

# run time (ticks)
run_length = 7200
scenario_number = 0 #modified. Only changes the title of the CSV. The remaining is not implemented @Daniela
df=pd.DataFrame(columns=['road','scenario','seed', 'Average driving time', 'Bridge with biggest delays', 'Bridge with biggest delays value', 'Total delay time',
                         'Average delay time per truck', 'Broken bridges']) #modified
seeds=range(1,10) #modified
for n, seed in enumerate(seeds):

    #Probably here add scenarios for loop?

    sim_model = BangladeshModel(seed=seed)

    # Check if the seed is set
    print("SEED " + str(sim_model._seed))

    # One run with given steps
    for i in range(run_length):
        sim_model.step()

    #Data Collection

    df.loc[n, 'road'] = 'N1'
    df.loc[n, 'scenario'] = scenario_number
    df.loc[n, 'seed'] = seed
    average_time = sim_model.get_average_driving_time()
    df.loc[n, 'Average driving time'] = average_time  # append the value to the DataFrame
    print(f"Average driving time: {average_time} mins")



    bridge_delay = sim_model.get_biggest_bridge_delay()
    if bridge_delay==(None,0):
        (bridge,value) = sim_model.get_biggest_bridge_delay()

    else:
        bridge, value = next(iter(bridge_delay.items()))

    df.loc[n, 'Bridge with biggest delays'] = bridge  # append the value to the DataFrame
    df.loc[n, 'Bridge with biggest delays value'] = value

    print(f"'Bridge with biggest delays': {bridge_delay} mins")


    total_delay = sim_model.get_total_delay_time()
    df.loc[n, 'Total delay time'] = total_delay  # append the value to the DataFrame
    print(f"'Total delay time': {total_delay} mins")

    average_delay = sim_model.get_average_delay_time()
    df.loc[n, 'Average delay time per truck'] = average_delay  # append the value to the DataFrame
    print(f"Average delay time per truck: {average_delay} mins")

    broken_bridges = sim_model.get_broken_bridges()
    df.loc[n, 'Broken bridges'] = broken_bridges  # append the value to the DataFrame
    print(f"Broken bridges: {broken_bridges} mins")

    df.to_csv(f'scenario{scenario_number}_summary.csv', index=False, sep=';')


    # Save the collected data ONLY from Vehicles to a CSV file
    sim_model.save_data(f'Vehicles-scenario{scenario_number}-seed {seed}.csv') #modified


