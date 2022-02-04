---
layout: page
mathjax: true
title: Panorama Stitching
permalink: /pano/
---
**This article is written by <a href="http://chahatdeep.github.io/">Chahat Deep Singh</a>** (chahat[at]terpmail.umd.edu) **and modified by Yu Fang.**

Please contact Yu Fang for any errors in this version.

Table of Contents:

- [Introduction](#intro)
- [Adaptive Non-Maximal Suppression](#anms)
- [Feature Descriptor](#feat-descriptor)
- [Feature Matching](#feat-matching)
- [RANSAC to estimate Robust Homography](#homography)
- [Cylinderical Projection](#cyl-projection)
- [Blending Images](#blending)

<a name='intro'></a>
## Introduction

The purpose of this project is to stitch two or more images in order to create one seamless panorama image using techniques described in the [paper](http://matthewalunbrown.com/papers/cvpr05.pdf) by Matthew Brown et al. Each image should have few repeated local features (around $$30$$--$$50\%$$ or more, empirically chosen). In this project, you need to capture multiple such images. Note that your camera motion should be limited to purely translational or purely rotational around the camera center. The following method of stitching images should work for most image sets but you'll need to be creative for working on harder image sets.


<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/pano/delicate-arch-set.jpg" width="100%">
  <div class="figcaption"> Fig. 1: Image Set for Panorama Stitching: Delicate Arch (at Arches National Park, Utah) </div><br>
  <img src="/cmsc426fall2019/assets/pano/delicate-arch-pano.jpg" width="100%">
  <div class="figcaption"> Fig. 2: Panorama image of the Delicate Arch </div>
</div>


For this project, let us consider a set of sample images with much stronger corners as shown in the Fig. 3.
<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/pano/pano-image-set.png" width="100%">
  <div class="figcaption"> Fig. 3: Sample image set for panorama stitching </div>
</div>


<a name='anms'></a>
## 2. Adaptive Non-Maximal Suppression (or ANMS)
The objective of this step is to detect corners such that they are equally distributed across the image in order to avoid weird artifacts in warping. Corners in the image can be detected using `cv2.cornerHarris` function with the appropriate parameters. The output is a matrix of corner scores: the higher the score, the higher the probability of that pixel being a corner. You can visualize the output using a [surface plot](https://matplotlib.org/examples/mplot3d/surface3d_demo.html).

To find particular strong corners that are spread across the image, first we need to find $$N_\text{strong}$$ corners. You can find the local maxima of the corner response, i.e. the "strong" corners, using the function `imregionalmax` provided in the startup code. However, when you take a real image, the corner is never perfectly sharp, each corner might get a lot of hits out of the $$N_\text{strong}$$ corners---we want to choose only the $$N_\text{best}$$ best corners after ANMS. In essence, you will get a lot more corners than you should! ANMS will try to find corners which are local maxima.

<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/pano/anms.png" width="100%">
  <div class="figcaption"> If you follow the pseudocode exactly, you will quickly run into efficiency issues because for loops in python are extremely slow. You have to translate the pseudocode into vectorized numpy code. Think about what the pseudocode actually means. Hint: can you find the coordinates of all the points that suppress a point using <a href="https://docs.scipy.org/doc/numpy/user/basics.indexing.html#boolean-or-mask-index-arrays">boolean indexing</a>? How can you calculate the distances from those points to the current point using <a href="https://docs.scipy.org/doc/numpy/user/theory.broadcasting.html#array-broadcasting-in-numpy">broadcasting</a>? How can you find the minimum distance? It is possible to trim down the double for loops into a single one with only three lines of code in each iteration. Further optimizations might be possible with spatial data structures.</div>
</div>

Fig 4. shows the output after ANMS. Clearly, the corners are spread across the image.
<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/pano/anms-output.png" width="100%">
  <div class="figcaption"> Fig. 4: Output of ANMS on first 2 images. Note that if you are using matplotlib to plot the corners. You have to flip the indices to get the (x,y) coordinates, since the first index of a matrix indexes vertical direction (columns), and the second index indexes horizontal direction (rows), whereas (x,y) coordinates is exactly the opposite. </div>
</div>

<a name='feat-descriptor'></a>
## 3. Feature Descriptor
In the previous step, you found the feature points (locations of the N best best corners after ANMS are called the feature points). You need to describe each feature point by a feature vector, this is like encoding the information at each feature points by a vector. One of the easiest feature descriptor is described next.

Take a patch of size $$40 \times 40$$ centered around the subpixel position of the key point (See figure 4 of the [paper](http://matthewalunbrown.com/papers/cvpr05.pdf)). You can take the upper left corner as the subpixel position of a pixel so that the pixel position of (0,0) is at the origin. You might also need to do some padding for features near the edges.

<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/pano/subpixel.png" width="30%">
</div>

Now apply Gaussian blur (feel free to play around with the parameters, check out the [image filtering](https://docs.opencv.org/master/d4/d86/group__imgproc__filter.html) section of OpenCV's documentation). Now, sub-sample the blurred output (this reduces the dimension) to $$8 \times 8$$ using a spacing of $$5$$ pixels. Then reshape to obtain a $$64 \times 1$$ vector. Standardize this $$64 \times 1$$ vector to have zero mean and variance of 1 (This can be done by subtracting all values by mean and then dividing by the standard deviation of all the components). Standardization is used to remove bias and some illumination effect.

<a name='feat-match'></a>
## 4. Feature Matching
In the previous step, you encoded each key point by a $$64\times1$$ feature vector. Now, you want to match the feature points in the two images so you can stitch the images together. In computer vision terms, this step is referred to as  finding feature correspondences within the 2 images. Pick a point in image 1, compute the distance (or squared distance) between all points in image 2. Take the ratio of best match (lowest distance) to the second best match (second lowest distance) and if this is below some ratio keep the matched pair otherwise reject it. Repeat this for all points in image 1. You will be left with only the confident feature correspondences and these points will be used to estimate the transformation between the 2 images also called **Homography**. You can use the `drawMatches` function provided in the startup code, which is simply a wrapper around [`cv2.drawMatches`](https://docs.opencv.org/master/d4/d5d/group__features2d__draw.html), to visualize the corresponding features. You would get something similar to Fig. 5 for the first two images.

<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/pano/matches2.png" width="100%">
  <div class="figcaption"> Fig. 5: Matches of the first 2 images. </div>
</div>

<a name='homography'></a>
## 5. RANSAC to estimate Robust Homography
We now have matched all the features correspondences but not all matches will be right. To remove incorrect matches, we will use a robust method called **Random Sampling Consensus** or **RANSAC** to compute the homography.

The steps of RANSAC are:
1. Select the coordinates (not matrix indices) of four feature pairs (at random), $$p_i$$ from image 1, $$p_i^\prime$$ from image 2.
2. Compute homography $$H$$ (exact). Use the function `est_homography` that is provided to you. Do not use OpenCV's `cv2.findHomography` function, because RANSAC is included in its implementation.
3. Apply the homography to the coordinates of each point $$p_i$$ from image 1. If the distance (or squared distance) between the matching point in image 2 $$\vec{p}_i^\prime$$ and the estimated point $$Hp_i$$ is below some threshold, then we call it an inlier. Here, $$Hp_i$$ computed using the `apply_homography` function given to you. Collect the coordinates of all the inliers and the corresponding points in image 2, giving you pair $$(\vec{p}_i, \vec{p}_i^\prime)$$.
4. Repeat the last three steps until you have exhausted $$N_\text{max}$$ number of iterations (specified by user) or you found more than percentage of inliers (Say $$90\%$$ for example).
5. Keep largest set of inliers.
6. Re-compute least-squares $$\hat{H}$$ estimate on all of the inliers. Use the function `est_homography` given to you.

<a name='cyl-projection'></a>
## 6. Cylindrical Projection
When we are try to stitch a lot of images with translation, a simple projective transformation (homography) will produce substandard results and the images will be stretched/shrunken to a large extent over the edges. Fig. 6 below highlights the stitching with bad distortion at the edges. Check <a href="https://graphics.stanford.edu/courses/cs178/applets/projection.html">this implementation/demo</a> of cylindrical projection from Stanford Computer Graphics department.

<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/pano/distortion.png" width="100%">
  <div class="figcaption"> Fig. 6: Panorama stitched using projective transform showing bad distortion at edges. </div>
</div>

To overcome such distortion problem at the edges, we will be using cylindrical projection on the images first before performing other operations. Essentially, this is a pre-processing step. The following equations transform between normal image coordinates and cylindrical coordinates:

$$
\begin{align*}
   x' &= f \cdot \tan \left(\cfrac{x-x_c}{f}\right)+x_c\\
   y' &=  \cfrac{y-y_c}{\cos\left(\cfrac{x-x_c}{f}\right)}+y_c
\end{align*}
$$

In the above equations, $$f$$ is the focal length of the lens in pixels (feel free to experiment with values, generally values range from 100 to 500, however this totally depends on the camera and can lie outside this range). The original image coordinates are $$(x, y)$$ and the transformed image coordinates (in cylindrical coordinates) are $$(x' ,y')$$. $$x_c$$ and $$y_c$$ are the image center coordinates. Note that $$x$$ is the column number and $$y$$ is the row number in numpy.

<p style="background-color:#ddd; padding:5px"><b>Note:</b> You might need to use numpy.meshgrid and vectorized code to speed up the computation. Using loops will TAKE FOREVER!</p>

A sample input image and its cylindrical projection is shown in Fig. 7.

<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/pano/input_image.png" width="60%">
  <img src="/cmsc426fall2019/assets/pano/cylinderical_image.png" width="60%">
  <div class="figcaption"> Fig. 7: Original Image vs Cylindrical Projection. </div>
</div>

<p style="background-color:#ddd; padding:5px"><b>Note: The above equations talk about pixel coordinates, NOT pixel values (intensities).</b> The idea is you compute the coordinate transformation and copy paste pixel values to these new pixel coordinates (in all 3 RGB channel).</p>

However, when you compute the values of $$(x',y')$$ they might not be integers. A simple way to get around this is to use round or actually interpolate the values. If you decide to round the coordinates off you might be left
with black pixels, fill them using some weighted combination of its neighbours (Gaussian works best). A trivial way to do this is to blur the image and copy paste pixel values on-to original image where there were pure black pixels. (You can also initialize pixels to NaN’s instead of zeros to avoid removing actual zero pixels).

<a name='blending'></a>
## 7. Blending Images:
Panorama can be produced by overlaying the pairwise aligned images to create the final output image. You can use OpenCV's [`cv2.warpPerspective`](https://docs.opencv.org/master/da/d54/group__imgproc__transform.html#gaf73673a7e8e18ec6963e3774e6a94b87) here. Feel free to implement `warpPerspective` or similar function yourself. Again, notice the distinction between matrix indices and coordinates. `cv2.warpPerspective` will warp the coordinates of the image (i.e. $$x$$ is horizontal direction, $$y$$ is vertical direction), not the matrix indices (for `I[m,n]`, $$n$$ is horizontal direction (columns), $$m$$ is vertical direction (rows)). Make sure you estimate the homography using coordinates instead of matrix indices in step 5.

After you have the homography matrix, you need to calculate a bounding box for each image after applying the homography (where do the 4 corners of an image go after applying a homography?). Then you need to find the largest bounding box for all the images after transformation and use the dimension of the bounding box (i.e. coordinates of bottom right corner minus upper left corner) as your canvas size. After obtaining the canvas size, left multiply the homography matrix with a translation matrix to shift the upper-left corner to $$(0,0)$$ so that all the images can fit inside the canvas.

You can apply a bilinear interpolation when you copy pixel values, but taking the maximum or average of pixel values should also works with some visible artifacts. Feel free to use any third party code for warping and transforming images. Fig. 8 shows the panorama output for the image set in Fig. 3.
<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/pano/pano-output.png" width="80%">
  <div class="figcaption"> Fig. 8: Final Panorama output. </div>
</div>

Come up with a logic to blend the common region between images while not affecting the regions which are not common. Here, common means shared region, i.e., a part of first image and part of second image should overlap in the output panorama. Describe what you did in your report. **Feel free to use any third party code to do this.**

<p style="background-color:#ddd; padding:5px"><b>Note:</b> The pipeline talks about how to stitch a pair of images, you need to extend this to work for multiple images. You can re-run your images pairwise or do something smarter.</p>

Your end goal is to be able to stitch any number of given images - maybe 2 or 3 or 4 or 100, your algorithm should work. If a random image with no matches are given, your algorithm needs to report an error.

<p style="background-color:#ddd; padding:5px"><b>Note:</b> When blending these images, there are inconsistency between pixels from different input images due to different exposure/white balance settings or photometric distortions or vignetting. This can be resolved by <a href="http://www.irisa.fr/vista/Papers/2003_siggraph_perez.pdf">Poisson blending</a>. You can use third party code for the seamless panorama stitching.

