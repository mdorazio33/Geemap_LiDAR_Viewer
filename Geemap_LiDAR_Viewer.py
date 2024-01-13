import os
import geemap

file = r'' # load the path to the file of your choice

lasfile = geemap.read_lidar(file)

lasfile.header

lasfile.header.point_count

list(lasfile.point_format.dimension_names)

lasfile.X

lasfile.Y

lasfile.Z

lasfile.intensity

geemap.view_lidar(file, cmap='terrain', backend='pyvista')