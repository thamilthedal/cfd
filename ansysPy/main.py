import h5py
import numpy as np
from utils import print_group, extract_data, get_filenames

# 3 D Data-extraction

#print("\n\n\nCase File Structure")
f = h5py.File('src/test.cas.h5', 'r')
#print_group(f)
data = f['meshes']['1']['cells']['zoneTopology']['dimension']

print(data[0])

#Partition ID
data = f['meshes']['1']['cells']['partition']['1']['partition-ids']
ID = np.array(data)
print("ID Obtained")

print(ID[0])

fileNames = get_filenames('src', 'dat.h5')
for i in fileNames:
    g = h5py.File(i, 'r')
    #print_group(g)
    [Cell_Variables, Cell_Data] = extract_data(g, 'cells')
    [Face_Variables, Face_Data] = extract_data(g, 'faces')
    print(i.split('/')[-1].split('.dat.h5')[0])
    print(f"Max Temperature on Faces: {max(Face_Data[12])}")
