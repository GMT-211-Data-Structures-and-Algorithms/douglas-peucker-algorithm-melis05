\# Douglas-Peucker Algorithm



GMT 211 - Data Structures and Algorithms  

Hacettepe University, Department of Geomatics Engineering



\## What is it?



The Douglas-Peucker algorithm reduces the number of points in a polyline while preserving its overall shape. It is commonly used in GIS map generalization, cartography, and GPS trajectory compression.



\## How Does it Work?



1\. Connect the first and last point with a straight line

2\. Calculate the perpendicular distance of all intermediate points to this line

3\. Find the point with the maximum distance (dmax)

4\. If `dmax > ε` → keep that point, split into two segments, apply \*\*recursively\*\*

5\. If `dmax ≤ ε` → remove all intermediate points



The larger the `ε` (epsilon), the more points are removed.



\## Project Structure



```

├── dp/

│   ├── \_\_init\_\_.py       # package definition

│   ├── algorithm.py      # DP algorithm

│   └── io\_utils.py       # file read/write operations

├── main.py               # main script

├── test\_dp.py            # unit tests

├── line.txt              # sample text input

├── Trabzon.geojson       # Trabzon coastline data (raw)

├── Trabzon\_wgs84.geojson # Trabzon coastline data (WGS84)

└── out.geojson           # simplified output after DP

```



\## Usage



```python

from dp import \*



input\_file = 'Trabzon\_wgs84.geojson'

out\_file = 'out.geojson'

epsilon = 0.01



execute\_douglas\_peucker(input\_file, out\_file, epsilon)

```



\## Running Tests



```

python test\_dp.py

```



Expected output:

\- epsilon = 6 → \[(1.0, 2.0), (8.0, 6.0)]

\- epsilon = 0.1 → \[(1.0, 2.0), (6.0, -2.0), (9.0, 4.0), (8.0, 6.0)]



\## Requirements



\- Python 3.x

\- No external libraries required (numpy/scipy not used)



\## Limitations



\- Greedy approach, not globally optimal

\- Sensitive to epsilon selection

\- May oversimplify sharp features



