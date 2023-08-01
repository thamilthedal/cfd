## Post-process ANSYS Fluent HDF5 files in Python for better workflow

I have started working on this idea to develop a module that extracts both mesh and variable data from ANSYS Fluent files (.cas.h5) and (.dat.h5) directly so that I can use it to plot lineplots and contours using Python packages.

### What I manage to do so far?
1. Parse a source Directory and extract all the case and data files present there and store it in a HDF5 File Object.
2. Extract Solution Variables from .dat.h5 file (both Cell-centered variables and Face-centered variables)
3. Extract Node information, i.e., coordinates (X, Y, Z) of nodes, in both 2D and 3D meshes from .cas.h5 file.
4. Compute face-centers for all faces based on the node information collected.
5. Cell-center extraction completed. (@Runinho contributed for this through Stackoverflow.)

---


### What are the different modules more to do after obtaining cell-center data?
- Once cell-center data is obtained, Data Extraction is complete.
- Create a point, that stores Cell_ID for adjacent cells, and the variable at the point can be computed as an average of that adjacent cells.
    - 2 adjacent cells for 1D, 4 for 2D and 6 for 3D
- For line plots,
    - Create a query module and interpolating module to extract line information from the mesh.
    - Interpolation module that also interpolates necessary cell or face variables on that queried line
- For contour,
    - Create a slice module to select a plane from the mesh data.
    - Interpolating the variables on the selected plane and then plot a contour on the same.
- Create other variables based on the default given variables, that should be chosen based on the necessity.

# Goal is to eliminate the need to use CFD-Post for repeated post-processing of multiple cases and datafiles from ANSYS Fluent at a time.
