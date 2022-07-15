import pandas as pd
import folium
import webbrowser
from folium.plugins import MarkerCluster
from matplotlib import pyplot as plt


def map_locations(data):
    print("this is data", data)
    bike_station_locations = pd.DataFrame(data)

    locations = bike_station_locations[
        ["pickup_latitude", "pickup_longitude", "tpep_pickup_datetime"]
    ]
    locations_df = locations.drop(
        locations[locations.pickup_latitude == 0.0].index
    )

    map = folium.Map(
        location=[
            max(locations_df.pickup_longitude),
            max(locations_df.pickup_latitude),
        ],
        zoom_start=11,
        control_scale=True,
    )

    for index, location_info in locations_df.iterrows():
        folium.Marker(
            [
                location_info["pickup_latitude"],
                location_info["pickup_longitude"],
            ],
            popup=location_info["tpep_pickup_datetime"],
        ).add_to(map)

        map.save("map_1.html")
    webbrowser.open("map_1.html")


# def map_data(data):
#     bike_station_locations = pd.DataFrame(data)
#
#     bike_station_locations = bike_station_locations.head()
#     locations = bike_station_locations[["pickup_latitude",
#                                         "pickup_longitude",
#                                         "tpep_pickup_datetime"]]
#     locations_df = locations.drop(
#         locations[locations.pickup_latitude == 0.0]
#         .index)
#     # Create a Map instance
#     m = folium.Map(location=[
#         max(locations_df.pickup_longitude),
#         max(locations_df.pickup_latitude)],
#         zoom_start=11,
#         control_scale=True)
#
#     locations_df["pickup_longitude"] = locations_df[
#         "pickup_longitude"].apply(
#         lambda geom: locations_df.pickup_longitude)
#     locations_df["tpep_pickup_datetime"] = locations_df[
#         "tpep_pickup_datetime"].apply(
#         lambda geom: locations_df.pickup_latitude)
#
#     # Create a list of coordinate pairs
#     locations = list(zip(locations_df["pickup_longitude"],
#                          locations_df["tpep_pickup_datetime"]))
#
#     # Create a folium marker cluster
#     marker_cluster = MarkerCluster(locations)
#
#     # Add marker cluster to map
#     marker_cluster.add_to(m)
#
#     # Show map
#     m
# import matplotlib.pyplot as plt
# import numpy as np
#
# # Import contextily
# import contextily
# import geopandas as gpd
# import pandas as pd
# # data_url = ""
# geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# geo_df["name"] = "United States of America"
# country = geo_df.loc[geo_df['iso_a3'] == "USA"]
# base = country.plot()
# base.show()
# #
# fig, ax = plt.subplots()
# d = {"x": [-73.9911956787109, -73.9660568237305,
#            -73.9660568237305, -73.958869934082],
#      "y": [40.7441368103027, 40.7624015808106,
#            40.7624015808106, 40.7092475891113]}
#
# ax.plot(d["x"], d["y"], 'o', markersize=3)
#
# contextily.add_basemap(ax)
# plt.show()


# import pandas as pd
# import geopandas as gpd
# import shapely
# # needs 'descartes'
#
# import matplotlib.pyplot as plt
# #
# # d = pd.DataFrame({"x": [-73.9911956787109, -73.9660568237305,
# #            -73.9660568237305, -73.958869934082],
# #      "y": [40.7441368103027, 40.7624015808106,
# #            40.7624015808106, 40.7092475891113]})
# d = pd.read_csv("/home/ninosha/Downloads/daily-2015-01-04.csv")
# gdf = gpd.GeoDataFrame(
#                        crs={'init': 'epsg:4326'},
#                        geometry=[shapely.geometry.Point(xy)
#                                  for xy in zip(d["pickup_longitude"], d
#                            ["pickup_latitude"])])
#
#
# world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# country = world.loc[world['iso_a3'] == "USA"]
# fig = px.scatter_geo(geo_df,
#                     lat=geo_df.geometry.y,
#                     lon=geo_df.geometry.x,
#                     hover_name="name")
# base = country.plot(color='white', edgecolor='black')
# gdf.plot(ax=base, marker='o', color='red', markersize=5)
#
# plt.show()
# import plotly.express as px
# import geopandas as gpd
# import pandas as pd
# d = pd.read_csv("/home/ninosha/Downloads/daily-2015-01-04.csv")
# geo_df = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
# country = geo_df.loc[geo_df['iso_a3'] == "USA"]
#
# fig = px.scatter_geo(geo_df,
#                      lat=d["pickup_latitude"],
#                      lon= d["pickup_longitude"],
#                      hover_name="name")
# fig.show()
# import pandas as pd
# import plotly.graph_objs as go
# import plotly.express as px
# fig = go.Figure()
# for lat, long in d.columns:
#     fig.add_trace(go.Line(x=df.index, y=df[col]))
# fig.show()

# import datetime
# import folium
# from folium.map import *
# from folium import plugins
# from folium.plugins import MeasureControl
# from folium.plugins import FloatImage
# import geopandas as gpd
#
#
# def map_data(data):
#     fig, ax = plt.subplots(figsize=(8, 6))
#     bike_station_locations = pd.DataFrame(data)
#
#     countries = gpd.read_file(
#         gpd.datasets.get_path("naturalearth_lowres"))
#
#     countries[countries["name"] == "United States of America"].plot(
#         color="lightgrey", ax=ax)
#
#     locations = bike_station_locations[["pickup_latitude",
#                                         "pickup_longitude",
#                                         "tpep_pickup_datetime"]]
#     locations_df = locations.drop(
#         locations[locations.pickup_latitude == 0.0]
#         .index
#     )
#     locations_df.plot("pickup_latitude", "pickup_longitude",
#                       kind="scatter", cmap='viridis',
#                       ax=ax)
#
#     # locations_df.plot(x="longitude", y="latitude", kind="scatter",
#     #         c="brightness", colormap="YlOrRd",
#     #         title=,
#     #         ax=ax)
#     # add grid
#     ax.grid(b=True, alpha=0.5)
#     plt.show()
