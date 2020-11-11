#!/usr/bin/env python
# -*- coding: utf-8 -*-


# TODO: Importez vos modules ici
import numpy as np
import matplotlib.pyplot as plt


# TODO: Définissez vos fonctions ici (il en manque quelques unes)
def linear_values() -> np.ndarray:
    return np.array([np.linspace(-1.3, 2.5, 64 )])


def coordinate_conversion(cartesian_coordinates: np.ndarray) -> np.ndarray:

    return np.array([])


def find_closest_index_np(values: np.ndarray, number: float) -> int:
    return sorted([(i, values[i]) for i in range(values.size)], key= lambda element : abs(element[1] - number))[0][0]
    return np.abs(values - number).argmin()


def courbe():
    y = 𝑥**2 * sin⁡(1∕𝑥**2 )+𝑥
    x = np.linspace(-1, 1, 250)
    
    plt.plot([50,100,150,200], [1,2,3,4])
    plt.show()




if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici

    pass
