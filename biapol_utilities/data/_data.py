# -*- coding: utf-8 -*-

from skimage import io
import numpy as np
import matplotlib
import os

data_dir = os.path.abspath(os.path.dirname(__file__))


def blobs():
    """Gray-level "blobs" image [1].

    Can be used for segmentation and denoising examples.

    Returns
    -------
    blobs : (256, 254) uint8 ndarray
        Blobs image.

    References
    ----------
    .. [1] https://imagej.nih.gov/ij/images/
    """
    return io.imread(os.path.join(data_dir, "blobs.png"))


def hourglass():
    """Gray-level 4D hourglass image [1].

    Can be used for polar transformations, tracking, dimentionality reduction.

    Returns
    -------
    hourglass : (50, 100, 200, 200) uint8 ndarray
        Hourglass 3D+t image depicting an unrealisitc bright half-circle
        droplet sliding through the glass wall.

    References
    ----------
    .. [1] Created with a Fiji macro by Marcelo Leomil Zoccoler
    """
    return io.imread(os.path.join(data_dir, "hourglass.tif"))


def labels_colormap():
    if not hasattr(labels_colormap, "labels_cmap"):
        state = np.random.RandomState(1234567890)

        lut = state.rand(65537, 3)
        lut[0, :] = 0
        labels_colormap.labels_cmap = matplotlib.colors.ListedColormap(lut)
    return labels_colormap.labels_cmap
