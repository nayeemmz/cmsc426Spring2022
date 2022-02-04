---
layout: page
mathjax: true
title: Panorama Stitching
permalink: /2019/proj/p2/
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
11:59PM, Sunday, Nov. 10, 2019

<a name='intro'></a>
## Introduction

The aim of this project is to implement an end-to-end pipeline for panorama stitching. We all use the panorama mode on our smart-phones--you'll implement a pipeline which does the same basic thing!

This document just provides an overview of what you need to do.  For a full breakdown of how each step in the pipeline works, see <a href="/cmsc426fall2019/pano/">the course notes for this project</a>.

<a name='system_overview'></a>
## System Overview

Here's a system diagram, showing each step in your panorama-stitching pipeline:

<div class="fig figcenter fighighlight">
  <img src="/cmsc426fall2019/assets/proj2/system_diagram.png" width="100%">
</div>

A brief description of each step (you'll implement the steps **in bold**):

- Cylinder Projection:  Project images onto a cylinder, to reduce distortion at the panorama's edges.  For this project, it's optional.
- Detect Corners:  identify corner points in your images.  (You can just use OpenCV's [`cornerHarris`](https://docs.opencv.org/4.1.2/dd/d1a/group__imgproc__feature.html#gac1fc3598018010880e370e2f709b4345))
- **ANMS**: pick out the stronger corner points.
- **Feature Descriptors**: create descriptors for the corner points, so they can be matched between images (in the next step).
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
Please find the starter code at [this link](/cmsc426fall2019/assets/proj2/project2.zip).
This also includes three sets of "training images". Twenty-four hours before the due date, we'll distribute a "test set" of two more sets of images (look out for an announcement on Piazza).

When writing your program, you can assume that input images will always follow the filename convention "1.jpg", "2.jpg", etc.

<a name='sub'></a>
## Submission Guidelines

<b> We will deduct points if your submission does not comply with the following guidelines.</b>

Please submit the project <b> once </b> for your group -- there's no need for each member to submit it.

### File tree and naming

Your submission on Canvas must be a zip file, following the naming convention **YourDirectoryID_proj2.zip**.  For example, xyz123_proj2.zip.  The file **must have the following directory structure**:

- YourDirectoryID_proj2.zip/
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

Logistics and bookkeeping you **must** include at the top of your report (-5 points for each one that's missing):
 - The name of each group member. - A brief (one paragraph or less) description of what each group member contributed to the project.

Include visualizations of the output of each stage in your pipeline (as shown in the system diagram
on page 2), and a description of what you did for each step.  Assume that we're familiar with the
project, so you don't need to spend time repeating what's already in the course notes.  Instead, focus
on any interesting problems you encountered and/or solutions you implemented.

Be sure to include the output panoramas for **all five image sets** (from the training **and** test sets).  Because you have limited time in which to access the "test set" images, we won't expect in-depth analysis of your results for them.

As usual, your report must be full English sentences, **not** commented code. There is a word limit of 1500 words and no minimum length requirement.

<a name='coll'></a>
## Collaboration Policy
We encourage you to work closely with your groupmates, including collaborating on writing code.  With students outside your group, you may discuss methods and ideas but may not share code.

For the full collaboration policy, including guidelines on citations and limitations on using online resources, see <a href="http://www.cs.umd.edu/class/fall2019/cmsc426-0201/">the course website</a>.

## Acknowledgements
This fun project was inspired by a similar project in UPenn's <a href="https://alliance.seas.upenn.edu/~cis581/wiki/index.php?title=CIS_581:_Computer_Vision_%26_Computational_Photography">CIS581</a> (Computer Vision & Computational Photography).
