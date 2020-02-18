import json

from shapely.geometry import Point
from shapely import wkt


with open('multipolygon.json', 'r') as polygons_data:
    raw_data = polygons_data.read()
districts = json.loads(raw_data)

point = Point(83.096993, 54.820887)

for district in districts:
    m_polygon = wkt.loads(district['boundaries'])
    print(point.within(m_polygon), district['type'], district['fullName'])
