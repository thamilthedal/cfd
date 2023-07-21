import os
import numpy as np

def extract_data(f, group):
    Variables = []
    Data = []
    for i in list(f['results']['1']['phase-1'][group].keys()):
        if 'SV_' in i:
            Variables.append(i.split('SV_')[1])
            Data.append(np.array(f['results']['1']['phase-1'][group][i]['1']))

    return [Variables, Data]

def get_filenames(sourceDir, extension):
    i = 0
    fileNames = []
    for top, dirs, files in os.walk(sourceDir):
        for filename in files:
            if filename.endswith(extension):
                new_file_path = top + '/' + filename
                fileNames.append(new_file_path)
                i += 1
    print(f"Found {i} files with {extension}\n")

    return fileNames

def print_group(group):
    for i in list(group.keys()):
        try:
            if list(group[i].keys()):
                print(f"{group.name}/{i}/")
                print_group(group[i])
        except:
            print(group[i].name, group[i].dtype, group[i].shape)

