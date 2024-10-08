import numpy as np

def smooth_image(a, sigma=1):
    return gaussian_filter(a, sigma=sigma)

__all__ = ['rand_array']


def rand_array(shape):
    return np.random.rand(*shape)
