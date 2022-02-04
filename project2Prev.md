---
layout: page
mathjax: true
title: Clustering using GMM
permalink: /proj/pnnn/
---

Table of Contents:
- [Deadline](#due)
- [Introduction](#intro)
- [What you need to do](#problem)
  - [Problem Statement](#pro)
- [Submission Guidelines](#sub)
- [Collaboration Policy](#coll)

<a name='due'></a>
## Deadline
11:59PM, Sunday, March 15, 2020

<a name='intro'></a>
## Part I - Introduction

A linear combination of Gaussian distributions forms a superposition formulated as a probabilistic model known as a Gaussian Mixture Model. 
The purpose of this homework is to practice Gaussian Mixture Models (GMM). More specifically you are required to use GMM's to cluster 2D data that will be provided to you.


There are two types of models that you will be building for this project:
- Data clustering using a single Gaussian Model.
- Data clustering using a Gaussian Mixture Model (GMM).

<a name='problem'></a>
## What you need to do
The data for this homework has been generated using three different Gaussian distributions, mixed together and shuffled. As a result there are three different distributions forming three different clusters. Your goal is to find those clusters. That means, for each of the distributions of the mixture model you would need to find their means ($$\mu$$), mixture coefficients ($$\pi$$) and the covariance matrices ($$\Sigma$$).

You may download the data from [here](/cmsc426Spring2020/assets/proj2/data.csv). This data can be visualized as follows:
<center>
<div class="fig fighighlight">
  <img src="/cmsc426Spring2020/assets/proj2/p2_data.png" width="50%">
  <div class="figcaption">
  </div>
  <div style="clear:both;"></div>
</div>
</center>

<a name='pro'></a>
### Problem Statement

1. Write Python code to cluster the three distributions using a [Single Gaussian](https://nayeemmz.github.io/cmsc426Spring2020/p2colorseg/#gaussian) [20 points]
2. Write Python code to cluster the three distributions using a [Gaussian Mixture Model](https://nayeemmz.github.io/cmsc426Spring2020/p2colorseg/#gmm) [20 points] 
 


You are **NOT** allowed to use any built-in Python library code for GMM. To draw ellipses you may find the following [documentation](https://matplotlib.org/devdocs/gallery/statistics/confidence_ellipse.html) helpful.


<a name='intro'></a>
## Part II - Introduction

Have you ever played with these adorable Nao robots? Click on the image to watch a cool demo.

<a href="http://www.youtube.com/watch?feature=player_embedded&v=Gy_wbhQxd_0
" target="_blank"><img src="http://img.youtube.com/vi/Gy_wbhQxd_0/0.jpg"
alt=" Nao robot demo " width="480" height="360" border="0" /></a>

Nao robots are star players in RoboCup, an annual autonomous robot soccer competitions.
We are planning to build the Maryland RoboCup team to compete in RoboCup 2020, we need your help.
Would you like to help us in Nao's soccer training? We need to train Nao to detect a soccer ball and estimate the depth of the ball to know how far to kick.

Nao's training has two phases:
- Color Segmentation using Gaussian Mixture Model (GMM)
- Ball Distance Estimation

<a name='problem'></a>
## What you need to do
To make logistics easier, we have collected camera data from Nao robot on behalf of you and saved the data in the form of color images. Click [here](https://drive.google.com/file/d/17XiM86JqHqko4JC00-E4w4sPKnzh2iMz/view?usp=sharing) to download. The image names represent the **depth** of the ball from Nao robot in centimeters. **The test dataset is [here](https://drive.google.com/file/d/17tNn3YIVR-8kqoBgJNK58YY4UBnQmm4q/view?usp=sharing) to download**.

<a name='pro'></a>
### Problem Statement

Please read the [tutorial](https://nayeemmz.github.io/cmsc426Spring2020/colorseg/) before moving on to the assignment.

1. Prepare the data: Extract the regions of the ball from each of the training images. For example, you can use the [*roipoly*](https://github.com/jdoepfert/roipoly.py) function to do so. Please note that since it is a Python script you would have to extract these features outside of the Jupyter notebook. The image pixels obtained this way are the data that you will use to train your color model.
2. Model the "orange" ball using a [Single Gaussian](https://nayeemmz.github.io/cmsc426Spring2020/colorseg/#gaussian). [10 points]
3. Model the "orange" ball using a [Gaussian Mixture Model](https://nayeemmz.github.io/cmsc426Spring2020/colorseg/#gmm). Here you need to experiment with the parameters yourself. You may use the Python code from the previous homework. [10 points]
4. Plot all the [GMM ellipsoids](https://nayeemmz.github.io/cmsc426Spring2020/colorseg/#different-cases-for-sigma-in-gmm). We have provided a [function](/cmsc426Spring2020/assets/proj2/draw_ellipsoid.ipynb) for you. [10 points].
5. Estimate the [distance](https://nayeemmz.github.io/cmsc426Spring2020/colorseg/#distest) to the ball. For each image in the test sets, you should put a bitmask image of the ball location in the `results` folder. Add a suffix to indicate the distance to camera. For example, if you estimate that the ball in `1.jpg` is 40 units away from camera, name the file `1_40.jpg`. If you can't estimate the distance, name the file `1_failed.jpg` [10 points].


### File tree and naming

Your submission on Canvas must be a zip file, following the naming convention **YourDirectoryID_proj2.zip**. For example, xyz123_proj2.zip. The file **must have the following directory structure**.

YourDirectoryID_proj2.zip.
 - train_images/.
 - test_images/.
 - results/.
 - colorseg.ipynb
 - report.pdf [20 points]
 - ... (models, training data, etc.)

### Report

For each section of the project, explain briefly what you did, and describe any interesting problems you encountered and/or solutions you implemented. You must include the following details in your writeup:

- Your choice of color space, initialization method and number of Gaussians in the GMM.
- Explain why GMM is better than a single Gaussian.
- Present your distance estimate and segmentation results for each test image.
- Explain strengths and limitations of your algorithm. Also, explain why the algorithm failed on some test images.

As usual, your report must be full English sentences, **not** commented code. There is a word limit of 1500 words and no minimum length requirement

<a name='coll'></a>
## Collaboration Policy
You are encouraged to work on this project in groups of three at the most. The code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the CMSC426 Spring 2020 website.
