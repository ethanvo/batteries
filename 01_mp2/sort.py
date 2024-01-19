#!/usr/bin/env python3
import numpy as np
coordinates_1 = [['Li',         (0.00000, 0.00000, 0.00000)],
['Li',         (1.75465, 1.75465, 1.75465)],
['Li',         (0.00000, 0.00000, 3.50930)],
['Li',         (1.75465, 1.75465, 5.26395)],
['Li',         (0.00000, 3.50930, 0.00000)],
['Li',         (1.75465, 5.26395, 1.75465)],
['Li',         (0.00000, 3.50930, 3.50930)],
['Li',         (1.75465, 5.26395, 5.26395)],
['Li',         (0.00000, 7.01860, 0.00000)],
['Li',         (1.75465, 8.77325, 1.75465)],
['Li',         (0.00000, 7.01860, 3.50930)],
['Li',         (1.75465, 8.77325, 5.26395)],
['Li',         (3.50930, 0.00000, 0.00000)],
['Li',         (5.26395, 1.75465, 1.75465)],
['Li',         (3.50930, 0.00000, 3.50930)],
['Li',         (5.26395, 1.75465, 5.26395)],
['Li',         (3.50930, 3.50930, 0.00000)],
['Li',         (5.26395, 5.26395, 1.75465)],
['Li',         (3.50930, 3.50930, 3.50930)],
['Li',         (5.26395, 5.26395, 5.26395)],
['Li',         (3.50930, 7.01860, 0.00000)],
['Li',         (5.26395, 8.77325, 1.75465)],
['Li',         (3.50930, 7.01860, 3.50930)],
['Li',         (5.26395, 8.77325, 5.26395)],
['Li',         (7.01860, 0.00000, 0.00000)],
['Li',         (8.77325, 1.75465, 1.75465)],
['Li',         (7.01860, 0.00000, 3.50930)],
['Li',         (8.77325, 1.75465, 5.26395)],
['Li',         (7.01860, 3.50930, 0.00000)],
['Li',         (8.77325, 5.26395, 1.75465)],
['Li',         (7.01860, 3.50930, 3.50930)],
['Li',         (8.77325, 5.26395, 5.26395)],
['Li',         (7.01860, 7.01860, 0.00000)],
['Li',         (8.77325, 8.77325, 1.75465)],
['Li',         (7.01860, 7.01860, 3.50930)],
['Li',         (8.77325, 8.77325, 5.26395)]]

coordinates_2 = [['C',         (4.88970, 4.59965, 10.25831)],
['O',          (4.87017, 4.24579, 8.95257)],
['C',          (5.31084, 5.19371, 8.23330)],
['O',          (5.76578, 6.11120, 8.98224)],
['C',          (5.77415, 5.70234, 10.27233)],
['O',          (5.29972, 5.21615, 7.11296)],
['H',          (5.21236, 3.79832, 10.81418)],
['H',          (3.95311, 4.87124, 10.54810)],
['H',          (5.46472, 6.47991, 10.86798)],
['H',          (6.71679, 5.41899, 10.52943)]]

# Find the element in coordinates_1 that is closest to coordinates_2[2] and print the index of that element.
lithium_position = [np.asarray(i[1]) for i in coordinates_1]
lithium_position = np.asarray(lithium_position)
oxygen_position = np.asarray(coordinates_2[5][1])

# sort lithium_position by distance from oxygen_position
distances = np.linalg.norm(lithium_position - oxygen_position, axis=1)
sorted_indices = distances.argsort()
sorted_lithium_position = lithium_position[sorted_indices]

# reorder coordinates_1 by sorted_indices
sorted_coordinates_1 = [coordinates_1[i] for i in sorted_indices]

geometry = [coordinates_2 + sorted_coordinates_1[:i] for i in range(2, len(sorted_coordinates_1), 2)]

# write pyscf input files for each element in geometry
for i, geom in enumerate(geometry):
    with open('geom_{}.xyz'.format(i), 'w') as f:
        f.write('{}\n\n'.format(len(geom)))
        for atom in geom:
            f.write('{} {:10.6f} {:10.6f} {:10.6f}\n'.format(atom[0], atom[1][0], atom[1][1], atom[1][2]))

print(len(coordinates_1))