#!/usr/bin/env python
from anti_instagram import logger, wrap_test_main
from anti_instagram.kmeans import scaleandshift1, scaleandshift2
from anti_instagram.utils import (L1_image_distance, L2_image_distance,
    random_image)
import numpy as np

def assert_L1_small(img1, img2, threshold=0.1):
    diff_L1 = L1_image_distance(img1, img2)
    diff_L2 = L2_image_distance(img1, img2)
    logger.info('diff_L2: %f' % diff_L2)
    logger.info('diff_L1: %f' % diff_L1)
    assert diff_L1 <= threshold, diff_L1
    
def anti_instagram_test_correctness():
    logger.info('This is going to test that algorithm 1 and 2 give same results')
    
    id_scale, id_shift = [1.0, 1.0, 1.0], [0.0, 0.0, 0.0]
    img = random_image(480, 640)

    logger.info('algo 1 respects the identity')
    a = scaleandshift1(img, id_scale, id_shift)
    assert_L1_small(img, a)

    logger.info('algo 2 respects the identity')
    b = scaleandshift2(img, id_scale, id_shift)
    assert_L1_small(img, b)

    logger.info('algo 1 and 2 give the same output with random inputs')

    scale = np.random.rand(3)
    shift = np.random.rand(3)
    
    img1 = scaleandshift1(img, scale, shift)
    img2 = scaleandshift2(img, scale, shift)
    assert_L1_small(img1, img2)


if __name__ == '__main__':
    wrap_test_main(anti_instagram_test_correctness) 
