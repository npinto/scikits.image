import os.path

import numpy as np
from numpy.testing import *

from scikits.image import data_dir
from scikits.image.io import imread
from scikits.image import data_dir
from scikits.image.morphology import *

lena = np.load(os.path.join(data_dir, 'lena_GRAY_U8.npy'))

class TestMorphology():

    def morph_worker(self, img, fn, morph_func, strel_func):
        matlab_results = np.load(os.path.join(data_dir, fn))
        k = 0
        for expected_result in matlab_results:
            mask = strel_func(k)
            actual_result = morph_func(lena, mask)
            assert_equal(expected_result, actual_result)
            k = k + 1

    def test_erode_diamond(self):
        self.morph_worker(lena, "diamond-erode-matlab-output.npy",
                          greyscale_erode, diamond)

    def test_dilate_diamond(self):
        self.morph_worker(lena, "diamond-dilate-matlab-output.npy",
                          greyscale_dilate, diamond)

    def test_open_diamond(self):
        self.morph_worker(lena, "diamond-open-matlab-output.npy",
                          greyscale_open, diamond)

    def test_close_diamond(self):
        self.morph_worker(lena, "diamond-close-matlab-output.npy",
                          greyscale_close, diamond)

    def test_tophat_diamond(self):
        self.morph_worker(lena, "diamond-tophat-matlab-output.npy",
                          greyscale_white_top_hat, diamond)

    def test_bothat_diamond(self):
        self.morph_worker(lena, "diamond-bothat-matlab-output.npy",
                          greyscale_black_top_hat, diamond)

    def test_erode_disk(self):
        self.morph_worker(lena, "disk-erode-matlab-output.npy",
                          greyscale_erode, disk)

    def test_dilate_disk(self):
        self.morph_worker(lena, "disk-dilate-matlab-output.npy",
                          greyscale_dilate, disk)

    def test_open_disk(self):
        self.morph_worker(lena, "disk-open-matlab-output.npy",
                          greyscale_open, disk)

    def test_close_disk(self):
        self.morph_worker(lena, "disk-close-matlab-output.npy",
                          greyscale_close, disk)
