from os import path
import json

from cjio import cityjson
from cjio import tiling

p = '/home/balazs/Development/cjio/example_data/delft.json'
dout = '/home/balazs/Development/cjio/tmp/data'
with open(p, 'r') as f:
    cm = cityjson.CityJSON(file=f)

bbox = cm.update_bbox()
grid_idx = tiling.create_grid(bbox, 2)

for idx, bbox in grid_idx.items():
    print(idx, bbox)
    print("cm", len(cm.j['CityObjects']))
    s = cm.get_subset_bbox((bbox[0], bbox[1], bbox[3], bbox[4]), invert=False)
    print("s", len(s.j['CityObjects']))
    print("---------------")
    pout = path.join(dout,'{}.json'.format(idx))
    with open(pout, 'w') as fo:
        json_str = json.dumps(s.j, indent=2)
        fo.write(json_str)