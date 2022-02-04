---
layout: page
mathjax: true
title: Implementation of Scale Invariant Feature Transform (SIFT)
permalink: /2020/hw/hw2/
---

Table of Contents:
- [Due Date](#due)
- [Introduction](#intro)
- [Part 1: Implementation](#part1)
- [Part 2: What to submit](#part2)
- [Submission Guidelines](#sub)
- [Collaboration Policy](#coll)

<a name='due'></a>
## Due Date
11:59 PM, Monday, April 13, 2020

<a name='intro'></a>
## Introduction
In this homework you will implement Scale Invariant Feature Transform (SIFT). We will practice it on a set of images from Caltech-101 dataset that you would use in a later project as well. You may download Caltech-101 data
set from the following [link](http://www.vision.caltech.edu/Image_Datasets/Caltech101/#Download). All the images of this dataset are stored in folders, named for each category. However, we will be using just three of those categories: airplanes, dolphin and Leopards. If you would like to try for other categories too, please feel free to do so.  


<a name='part1'></a>
## Part 1: Implementation (70 pts)

You are expected to implement all the parts of the code without using any in-built libraries except for the basic operations from Numpy and Matplotlib for showing results. You may find functions such as imregionalmin, and imregionalmax useful for this project. In addition you may use Scipy for Gaussian filters and if you need cv2 for modifying images such as changing size etc.


<a name='part2'></a>
## Part 2: - What to submit (30 points)

1. hw2.ipynb - A jupyter notebook with the SIFT implementation. You should write different definitions (functions) for each step of the code to make it modular and easy to test and verify.
2. Few sample images of airplanes, dolphins, and, Leopards and display the key point locations for the feature descriptors using small circles. Something like the following image:
      <center>
      <div class="fig fighighlight">
        <img src="/cmsc426Spring2020/assets/hw2/dolphin_keypoints.jpg" width="50%">
        <div class="figcaption">
        </div>
        <div style="clear:both;"></div>
      </div>
        </center>
      You can pick any images you like.
 3. A report describing the key aspects of the homework including the problems you encountered and how you solved them.


<a name='sub'></a>
## Submission Guidelines

Your submission on Canvas must be a zip file, following the naming convention YourDirectoryID_hw2.zip. For
example, xyz123_hw2.zip. The file must have the following directory structure, 
- hw2.ipynb
- report.pdf

### Report

Please include the original images and SIFT feature descriptor locations for all the images you choose to discuss in your report. Also include your observations about the
feature descriptors pertaining to each class of images. For example, was it easier to find keypoints in one category of images versus others, etc.
As usual, your report must be full English sentences,not commented code

<a name='coll'></a>
## Collaboration Policy
This is not a group homework so everyone should work on it separately. You may discuss the ideas with your peers. If you reference anyone else's code in writing your homework, you must properly cite it in your code (in comments) and your writeup.  For the full honor code refer to the CMSC426 Spring 2020 website
