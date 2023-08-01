import numpy as np
import pandas as pd

# Node Coordinates
def get_node_data(f):
    data = f['meshes']['1']['nodes']['coords']['4']
    node_Data = pd.DataFrame(columns=['X', 'Y'])
    node_Data['X'] = data[:,0]
    node_Data['Y'] = data[:, 1]
    node_Data.index = node_Data.index + 1
    print("Node Coordinates Obtained!")
    return node_Data

# TO-DO - TRY TO REPLACE WITH MELT WORKFLOW SIMILAR TO CELL_DATA
def get_face_point(dir, node_df, face_df):
    A = 0.5*node_df[dir].iloc[face_df['Node_0']-1]
    B = 0.5*node_df[dir].iloc[face_df['Node_1']-1]
    C = np.add(list(A), list(B))
    return C

# Face Coordinates
def get_face_data(f, node_Data):
    face_node_list = f['meshes']['1']['faces']['nodes']['1']['nodes']
    face_number_of_nodes = f['meshes']['1']['faces']['nodes']['1']['nnodes']
    face_Data = pd.DataFrame(columns = ['N_nodes', 'Node_0', 'Node_1', 'X', 'Y'])
    face_Data['N_nodes'] = face_number_of_nodes
    face_Data['face_id'] = face_Data.index + 1
    face_node_list = np.array(face_node_list).reshape(int(len(face_node_list)/2), 2)
    face_Data['Node_0'] = face_node_list[:, 0]
    face_Data['Node_1'] = face_node_list[:, 1]
    face_Data['X'] = get_face_point('X', node_Data, face_Data)
    face_Data['Y'] = get_face_point('Y', node_Data, face_Data)
    face_Data['Cell_0'] = f['meshes']['1']['faces']['c0']['1']
    cell_1 = np.array(f['meshes']['1']['faces']['c1']['1'])
    add_length = len(face_Data['Cell_0']) - len(cell_1)
    cell_1 = np.append(cell_1, np.zeros(add_length))
    face_Data['Cell_1'] = cell_1
    print("Face Coordinates Obtained")
    return face_Data[['X', 'Y', 'face_id', 'Cell_0', 'Cell_1']]


def get_cell_data(f, face_Data):
    cell_Data = face_Data.melt( id_vars=["face_id", "X", "Y"], 
                                value_vars = ['Cell_0', 'Cell_1'], 
                                value_name = 'cell_id')\
                                .drop(columns = ['variable'])\
                                .groupby('cell_id')\
                                .mean()[1:]\
                                [['X', 'Y']]
    cell_Data.index = cell_Data.index.astype(int)
    print("Cell Coordinates Obtained")
    return cell_Data

def mesh_data_extract(f):
    node_Data = get_node_data(f)
    face_Data = get_face_data(f, node_Data)
    cell_Data = get_cell_data(f, face_Data)
    return (face_Data[['face_id', 'X', 'Y']], cell_Data)
