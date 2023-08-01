from meshData import mesh_data_extract
from utils import extract_data, get_filenames
import h5py

# Mesh Data extracted for 2D mesh
f = h5py.File('src/test2.cas.h5', 'r')
printgroup(f)
face_Data, cell_Data = mesh_data_extract(f)

# Variable Data extraction for 3D or 2D data
g = h5py.File('src/test.dat.h5', 'r')
printgroup(g)
[Cell_Variables, Cell_Data] = extract_data(g, 'cells')
[Face_Variables, Face_Data] = extract_data(g, 'faces')
