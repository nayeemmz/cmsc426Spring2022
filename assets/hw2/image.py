import numpy as np
from scipy import ndimage
from matplotlib import pyplot as plt

def imregionalmax(image, footprint):
    """Find the regional max of an ND image. An approximation of MATLAB's
    imregionalmax function. Result only differs when surrounding pixels
    have the same value as the center.

    Parameters:
    - image: the input image
    - footprint: a boolean ndarray specifying which neighboring pixels should be considered
                 for thresholding, see scipy.ndimage.generate_binary_structure.
    Returns:
    - a bitmask image, where '1' indicates local maxima.
    Author:
    - Yu Fang
    References:
    - https://github.com/bhardwajvijay/Utils/blob/master/utils.cpp
    - https://stackoverflow.com/questions/5550290/find-local-maxima-in-grayscale-image-using-opencv
    """
    # dialate the image so that small values are replaced by local max
    local_max = ndimage.grey_dilation(image, footprint=footprint, mode='reflect')
    # non-local max pixels (excluding pixel w/ constant 3x3 neighborhood)
    # will be replaced by local max, so the values will increase. remove them.
    # so the result is either local max or constant neighborhood.
    max_mask = image >= local_max
    # erode the image so that high values are replaced by local min
    local_min = ndimage.grey_erosion(image, footprint=footprint, mode='reflect')
    # only local min pixels and pixels w/ constant 3x3 neighborhood
    # will stay the same, otherwise pixels will be replaced by the local
    # min and become smaller. We only take non-local min, non-constant values.
    min_mask = image > local_min
    # boolean logic hack
    #   (local max || constant) && (!local min && !constant)
    # = local max && !local min && !constant
    # = local max && !constant
    return (max_mask & min_mask).astype(np.uint8)
  
def imregionalmin(image, footprint):
    """Find the regional min of an ND image. An approximation of MATLAB's
    imregionalmin function. Result only differs when surrounding pixels
    have the same value as the center.

    Parameters:
    - image: the input image
    - footprint: a boolean ndarray specifying which neighboring pixels should be considered
                 for thresholding, see scipy.ndimage.generate_binary_structure.
    Returns:
    - a bitmask image, where '1' indicates local maxima.
    Author:
    - Yu Fang
    References:
    - https://github.com/bhardwajvijay/Utils/blob/master/utils.cpp
    - https://stackoverflow.com/questions/5550290/find-local-maxima-in-grayscale-image-using-opencv
    """
    # erode the image so that high values are replaced by local min
    local_min = ndimage.grey_erosion(image, footprint=footprint, mode='reflect')
    # non-local min pixels (excluding pixel w/ constant 3x3 neighborhood)
    # will be replaced by local min, so the values will decrease. remove them.
    # so the result is either local min or constant neighborhood.
    min_mask = image <= local_min
    # dialate the image so that small values are replaced by local max
    local_max = ndimage.grey_dilation(image, footprint=footprint, mode='reflect')
    # only local max pixels and pixels w/ constant 3x3 neighborhood
    # will stay the same, otherwise pixels will be replaced by the local
    # max and become larger. We only take non-local max, non-constant values.
    max_mask = image < local_max
    # boolean logic hack
    #   (local min || constant) && (!local max && !constant)
    # = local min && !local max && !constant
    # = local min && !constant
    return (max_mask & min_mask).astype(np.uint8)

def show_image(img, scale=1.0):
    plt.figure(figsize=scale* plt.figaspect(1))
    plt.imshow(img, interpolation='nearest')
    plt.gray() 
    plt.axis('off')
    plt.show()