---
layout: page
mathjax: true
title: Panorama Stitching
permalink: /2021/hw/hw2/
---

Table of Contents:
- [Deadline](#due)
- [Introduction](#intro)
- [System Overview](#system_overview)
  - [Problem Statement](#pro)
- [Submission Guidelines](#sub)
- [Collaboration Policy](#coll)

<a name='due'></a>
## Deadline
11:59PM, Tuesday, April 06, 2021

<a name='intro'></a>
## Introduction

The aim of this project is to implement an end-to-end pipeline for panorama stitching. We all use the panorama mode on our smart-phones--you'll implement a pipeline which does the same basic thing!

This document just provides an overview of what you need to do.  For a full breakdown of how each step in the pipeline works, see <a href="/cmsc426Spring2021/pano/">the course notes for this project</a>.

<a name='system_overview'></a>
## System Overview

Here's a system diagram, showing each step in your panorama-stitching pipeline:

<div class="fig figcenter fighighlight">
  <img src="/cmsc426Spring2021/assets/hw2/system_diagram.png" width="100%">
</div>

A brief description of each step (you'll implement the steps **in bold**):

- Cylinder Projection:  Project images onto a cylinder, to reduce distortion at the panorama's edges.  For this project, it's optional.
- Detect Corners:  identify corner points in your images.  (You can just use OpenCV's [`cornerHarris`](https://docs.opencv.org/4.1.2/dd/d1a/group__imgproc__feature.html#gac1fc3598018010880e370e2f709b4345))
- **ANMS**: pick out the stronger corner points.
- **Feature Descriptors**: create descriptors for the corner points, so they can be matched between images (in the next step). You may use a library to find the SIFT descriptors or your own code from the previous project.
- **Feature Matching**: Match feature descriptors from different images, to find possible point correspondences.
- **RANSAC and Homography Estimation**: refine the feature point matches, and use the correspondences to estimate homographies between images.
- **Image Warping (and Blending)**: Use the estimated homographies to warp the images onto one another, and apply blending to reduce the appearance of seams where they fit together.
    - For blending in this project, you can simply average the pixel values of overlapping images or take the maximum.

### Point Distribution:
- ANMS: 25pts
- Feature Descriptors: 15pts
- Feature Matching: 15pts
- RANSAC and Homography Estimation: 20pts
- Image Warping (and Blending): 25pts


## Project Files and Starter Code
Please find the starter code at [this link](/cmsc426Spring2021/assets/hw2/hw2.zip).
This also includes three sets of "training images". Twenty-four hours before the due date, we'll distribute a "test set" of two more sets of images (look out for an announcement on Piazza).

When writing your program, you can assume that input images will always follow the filename convention "1.jpg", "2.jpg", etc.

<a name='sub'></a>
## Submission Guidelines

<b> We will deduct points if your submission does not comply with the following guidelines.</b>


### File tree and naming

Your submission on Canvas must be a zip file, following the naming convention **YourDirectoryID_hw2.zip**.  For example, xyz123_hw2.zip.  The file **must have the following directory structure**:

- YourDirectoryID_hw2.zip/
    - code/
        - panorama.ipynb
    - images/
        - input/
        - custom1,2/
        - (all of the other train and test images)
    - report.pdf

In the Jupyter notebook, your code should load the images in `images/input/` and display a resulting panorama in the end.

### Report
**You will be graded primarily based on your report.**  We want
you to demonstrate an understanding of the concepts involved in the project, and to show the output
produced by your code.


Include visualizations of the output of each stage in your pipeline (as shown in the system diagram
on page 2), and a description of what you did for each step.  Assume that we're familiar with the
homework, so you don't need to spend time repeating what's already in the course notes.  Instead, focus
on any interesting problems you encountered and/or solutions you implemented.

Be sure to include the output panoramas for **all five image sets** (from the training **and** test sets).  Because you have limited time in which to access the "test set" images, we won't expect in-depth analysis of your results for them.

As usual, your report must be full English sentences, **not** commented code. There is a word limit of 750 words and no minimum length requirement.

<a name='coll'></a>
## Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup.  For the full honor code refer to the CMSC426 Spring 2021 website.

## Acknowledgements
This fun homework was inspired by a similar project in UPenn's <a href="https://alliance.seas.upenn.edu/~cis581/wiki/index.php?title=CIS_581:_Computer_Vision_%26_Computational_Photography">CIS581</a> (Computer Vision & Computational Photography).