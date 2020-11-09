#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.array([np.linspace(-1.3, 2.5, 64 )])


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:

    return np.array([])


def find_closest_index(values: np.ndarray, number: float) -> int:
    return sorted([(i, values[i]) for i in range(values.size)], key= lambda element : abs(element[1] - number))[0][0]
    return np.abs(values - )

if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
