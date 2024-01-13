# Geemap_LiDAR_Viewer

This repository showcases a short demonstration of how to use Geemap to view LiDAR data. Geemap is a Python package that allows for interactive mapping with the Google Earth Engine. In other words, it enables users to interactively visualize and analyze GEE datasets.

It is highly useful for creating visualizations for areas where Earth Engine data is available. In my demonstration, I used a LAS file for an area near Waupaca, Wisconsin. However, Geemap takes many other file types in addition to LAS. Also, since LiDAR data is typically very large in size, defining a URL as a path is a good alternative if your local machine does not possess sufficient storage capacity. Otherwise, you may download your Earth Engine data files and use them locally from your machine.

Prior to running this code, be sure to have geemap and gdown installed. This can be done either through the command line via pip install geemap and pip install gdown. These packages may also be downloaded from within a Jupyter environment via !pip install geemap and !pip install gdown as well.
