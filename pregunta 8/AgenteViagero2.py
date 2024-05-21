import numpy as np
from itertools import permutations

# Crear el array
array = np.array([1, 2, 3, 4, 5, 6, 7, 8])

# Generar todas las permutaciones
all_permutations = list(permutations(array))

# Convertir las permutaciones a un array de numpy
all_permutations_array = np.array(all_permutations)

for i in all_permutations_array:
    print(i)

