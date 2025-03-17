from mesa import Model
from mesa.time import BaseScheduler
from mesa.space import ContinuousSpace
from components import Source, Sink, SourceSink, Bridge, Link, Intersection
import pandas as pd
import matplotlib.pyplot as plt
from collections import defaultdict
import networkx as nx



# ---------------------------------------------------------------
def set_lat_lon_bound(lat_min, lat_max, lon_min, lon_max, edge_ratio=0.02):
    """
    Set the HTML continuous space canvas bounding box (for visualization)
    give the min and max latitudes and Longitudes in Decimal Degrees (DD)

    Add white borders at edges (default 2%) of the bounding box
    """

    lat_edge = (lat_max - lat_min) * edge_ratio
    lon_edge = (lon_max - lon_min) * edge_ratio

    x_max = lon_max + lon_edge
    y_max = lat_min - lat_edge
    x_min = lon_min - lon_edge
    y_min = lat_max + lat_edge
    return y_min, y_max, x_min, x_max


# ---------------------------------------------------------------
class BangladeshModel(Model):
    """
    The main (top-level) simulation model

    One tick represents one minute; this can be changed
    but the distance calculation need to be adapted accordingly

    Class Attributes:
    -----------------
    step_time: int
        step_time = 1 # 1 step is 1 min

    path_ids_dict: defaultdict
        Key: (origin, destination)
        Value: the shortest path (Infra component IDs) from an origin to a destination

        Only straight paths in the Demo are added into the dict;
        when there is a more complex network layout, the paths need to be managed differently

    sources: list
        all sources in the network

    sinks: list
        all sinks in the network

    """

    step_time = 1

    file_name = '../data/demo-4.csv'

    def __init__(self, seed=None, x_max=500, y_max=500, x_min=0, y_min=0):

        self.schedule = BaseScheduler(self)
        self.running = True
        self.path_ids_dict = defaultdict(lambda: pd.Series()) #assigns an empty pandas series to a key that does not exist in the defaultdict
        self.space = None
        self.sources = []
        self.sinks = []
        # MODIFIED: Create an empty NetworkX graph
        #self.G = nx.Graph()
        self.generate_model()



    def generate_model(self):
        """
        generate the simulation model according to the csv file component information

        Warning: the labels are the same as the csv column labels
        """

        df = pd.read_csv(self.file_name)

        # a list of names of roads to be generated
        # TODO You can also read in the road column to generate this list automatically
        roads = ['N1', 'N2']

        df_objects_all = []

        # FROM YAO: Initialize NetworkX graph
        self.G_nx = nx.Graph()

        for road in roads:
            # Select all the objects on a particular road in the original order as in the cvs
            df_objects_on_road = df[df['road'] == road]

            if not df_objects_on_road.empty:
                df_objects_all.append(df_objects_on_road)

                """
                Set the path 
                1. get the serie of object IDs on a given road in the cvs in the original order
                2. add the (straight) path to the path_ids_dict
                3. put the path in reversed order and reindex
                4. add the path to the path_ids_dict so that the vehicles can drive backwards too
                """
                path_ids = df_objects_on_road['id'] #[100000,1000001,1000002,1000003,1000004,1000005,1000006,1000007,1000008,1000009,1000010,1000011,1000012,1000013]
                path_ids.reset_index(inplace=True, drop=True)
                self.path_ids_dict[path_ids[0], path_ids.iloc[-1]] = path_ids #(00,12):[]
                self.path_ids_dict[path_ids[0], None] = path_ids #if the destination is None, the path is straight
                path_ids = path_ids[::-1]
                path_ids.reset_index(inplace=True, drop=True)
                self.path_ids_dict[path_ids[0], path_ids.iloc[-1]] = path_ids
                self.path_ids_dict[path_ids[0], None] = path_ids #if the destination is None, the path is straight

                # Add nodes and edges to NetworkX graph
                for _, row in df_objects_on_road.iterrows():
                    self.G_nx.add_node(row['id'], pos=(row['lon'], row['lat']), model_type=row['model_type'])

                for i in range(len(df_objects_on_road) - 1):
                    self.G_nx.add_edge(df_objects_on_road.iloc[i]['id'], df_objects_on_road.iloc[i + 1]['id'],
                                       weight=df_objects_on_road.iloc[i]['length'])
                print(self.G_nx.nodes)
                print(self.G_nx.edges)
#(100000,1000025):[]
        # put back to df with selected roads so that min and max and be easily calculated
        df = pd.concat(df_objects_all)
        y_min, y_max, x_min, x_max = set_lat_lon_bound(
            df['lat'].min(),
            df['lat'].max(),
            df['lon'].min(),
            df['lon'].max(),
            0.05
        )

        # ContinuousSpace from the Mesa package;
        # not to be confused with the SimpleContinuousModule visualization
        self.space = ContinuousSpace(x_max, y_max, True, x_min, y_min)

        for df in df_objects_all:
            for _, row in df.iterrows():  # index, row in ...

                # create agents according to model_type
                model_type = row['model_type'].strip()
                agent = None

                name = row['name']
                if pd.isna(name):
                    name = ""
                else:
                    name = name.strip()

                if model_type == 'source':
                    agent = Source(row['id'], self, row['length'], name, row['road'])
                    self.sources.append(agent.unique_id)
                elif model_type == 'sink':
                    agent = Sink(row['id'], self, row['length'], name, row['road'])
                    self.sinks.append(agent.unique_id)
                elif model_type == 'sourcesink':
                    agent = SourceSink(row['id'], self, row['length'], name, row['road'])
                    self.sources.append(agent.unique_id)
                    self.sinks.append(agent.unique_id)
                elif model_type == 'bridge':
                    agent = Bridge(row['id'], self, row['length'], name, row['road'], row['condition'])
                elif model_type == 'link':
                    agent = Link(row['id'], self, row['length'], name, row['road'])
                elif model_type == 'intersection':
                    if not row['id'] in self.schedule._agents:
                        agent = Intersection(row['id'], self, row['length'], name, row['road'])

                if agent:
                    self.schedule.add(agent)
                    y = row['lat']
                    x = row['lon']
                    self.space.place_agent(agent, (x, y))
                    agent.pos = (x, y)
                    # MODIFIED: Add node to NetworkX graph
                    #self.G.add_node(agent.unique_id, model_type=model_type, pos=(x, y), length=row['length'])
        #self.G=self.create_network(df)

    '''
    def create_network(self, dataframe):
        #create a network based on the data
        #Add edges ensuring correct connection rules
        for i in range(len(dataframe) - 1):
            node1 = dataframe.iloc[i]["id"]
            node2 = dataframe.iloc[i + 1]["id"]
            length = dataframe.iloc[i]["length"]
            type1 = dataframe.iloc[i]["model_type"]
            type2 = dataframe.iloc[i + 1]["model_type"]

            # Ensure connections follow logical rules:
            # - Do NOT connect two sourcesinks
            # - Links connect elements properly
            if not (type1 == "sourcesink" and type2 == "sourcesink"):
                if node1 in self.G.nodes and node2 in self.G.nodes:
                    self.G.add_edge(node1, node2, weight=length)
        #pos = {}
        #for node in self.G.nodes:
            #pos = nx.get_node_attributes(self.G, 'pos')


        return self.G
    '''
    def get_shortest_path(self, source_node=1000000, target_node=1000013):

        try:
            # Compute shortest path and its length
            shortest_path = nx.shortest_path(self.G, source=source_node, target=target_node, weight="weight")
            total_distance = nx.shortest_path_length(self.G, source=source_node, target=target_node, weight="weight")


            # Print the results
            print(f"Shortest path from {source_node} to {target_node}: {shortest_path}")
            print(f"Total distance: {total_distance} meters")
            return shortest_path
        except nx.NetworkXNoPath:
            print(f"No path found between {source_node} and {target_node}.")
        except nx.NodeNotFound as e:
            print(f"Error: {e}")


    def get_random_route(self, source):
        """
        pick up a random route given an origin
        """
        while True:
            # different source and sink
            sink = self.random.choice(self.sinks)
            if sink is not source:
                break
        print(source,sink)
        if self.path_ids_dict[source,sink].empty: # if this is this (100000:1000025)=[]
            self.path_ids_dict=self.get_shortest_path(source, sink) #(100000:1000025)=[a route]

        return self.path_ids_dict[source, sink]

    # TODO
    def get_route(self, source):
        return self.get_random_route(source)

    def get_straight_route(self, source):
        """
        pick up a straight route given an origin
        """
        return self.path_ids_dict[source, None]

    def step(self):
        """
        Advance the simulation by one step.
        """
        self.schedule.step()

# EOF -----------------------------------------------------------
