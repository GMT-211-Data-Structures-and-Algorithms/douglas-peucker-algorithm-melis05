# Douglas-Peucker Algorithm

GMT 211 - Data Structures and Algorithms

Hacettepe University, Department of Geomatics Engineering

## What is it?

The Douglas-Peucker algorithm attempts to preserve the overall shape of a polyline while reducing the number of points in the polyline. It is used in GIS map generalization, cartography, and GPS track compression.

## How the Algorithm Works?

1. Connect the first and last points.
2. Calculate the **perpendicular distances** of all intermediate points to this line.
3. Find the furthest point (dmax).
4. If `dmax > ε` → preserve that point, split it into two parts, apply **recursive**.
5. If `dmax ≤ ε` → delete all intermediate points.

As `ε` (epsilon) increases, more points are deleted (more simplification).

## Project Structure

```
douglas_peucker/
├── dp/
│ ├── __init__.py # package definition
│ ├── algorithm.py # DP algorithm
│ └── io_utils.py # file reading/writing
├── main.py # main working file
├── test_dp.py # tests
├── line.txt # sample txt input
└── README.md
```

## Usage
### With GeoJSON file:
```python
from dp import *
input_file = 'bodrum.geojson'
out_file = 'out.geojson'
epsilon = 0.01

execute_douglas_peucker(input_file, out_file, epsilon)
```
### With a text file:
```python
from dp import *

input_line = convert_coordinates_to_line('line.txt')
result = douglas_peucker(input_line, epsilon=6)
for point in result:
print(point[0], point[1])
```
## Running Tests

```bash
python test_dp.py
```
## Requirements

- Python 3.x
- No external libraries required (numpy/scipy not used)

## Limitations

- Not globally optimal as it is a greedy approach
- Sensitive to ε selection
- Can oversimplify sharp features