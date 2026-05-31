from dp import *

input_file = 'Trabzon_wgs84.geojson'
out_file = 'out.geojson'

epsilon = 0.01

execute_douglas_peucker(input_file, out_file, epsilon)
