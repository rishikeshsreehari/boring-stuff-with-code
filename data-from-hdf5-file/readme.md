This converter reads an HDF5 file and converts into a dataframe. This specific HDF5 file has values of GHI,DHI,DNI, etc in a 2D matric format. The location formats are available in projections of meters and the code converts it to the respective format. Input porjection string is read from the metdata itself.

The obtained points are checked to see if it falls within a polyon using a shapefile uploaded. 


HDF5 file for reference" https://drive.google.com/file/d/1xQHNgrlrbyNcb6UyV36xh-7zTfg3f8OQ/view?usp=share_link
