---
layout: page
mathjax: true
title: Eigenfaces for face recognition
permalink: /proj/p1/
---

Table of Contents:
- [Deadline](#due)
- [Introduction](#intro)
- [What you need to do](#problem)
- [Submission Guidelines](#sub)
- [Collaboration Policy](#coll)

<a name='due'></a>
## Deadline
11:59PM, Monday, March 1, 2021

<a name='intro'></a>
## Introduction

Face recognition is 1:K matching problem. That means we have K images in a gallery and a test image. We want to match this test image to every image in the gallery and find a match that is the most similar to the test image. For example, if you are trying to find a match for a test image in a gallery of three images, the face recognition algorithm should find the middle image of the gallery to be the most similar.

<div class="fig fighighlight">
  <img src="/cmsc426Spring2021/assets/proj1/faces.png" width="100%">
  <div class="figcaption">
  </div>
  <div style="clear:both;"></div>
</div>

For a live demo of face recognition in the real time, check out the following [link](https://www.youtube.com/watch?v=wr4rx0Spihs).

In this project the goal is to practice implementation of principal components analysis technique to represent faces in a lower dimensional space and to recognize them. This technique was first presented by Turk and Pentland in their seminal paper [Eigenfaces for Recognition](http://www.face-rec.org/algorithms/PCA/jcn.pdf). You will be implementing this paper following the implementation of the following [case study](http://www.vision.jhu.edu/teaching/vision08/Handouts/case_study_pca1.pdf). You may see some differences between the way the covariance matrix is computed in the original paper and the case study. We will be following the case study so that your implementation is consistent with the rest of the implementation. Specifically use step 6 instead of step 5 to compute covariance matrix. Alternatively, use svd on matrix A instead of the covariance matrix to find the eigen vectors. 

A starter code file to read, display an image and display the pixel values alongwith the training and the test datasets can be downloaded from [here](/cmsc426Spring2021/assets/proj1/StarterFiles.zip).

<a name='problem'></a>
## What you need to do
You are required to do the following:
- Implement PCA to represent faces onto a lower dimensional space. You would need to do some experimentation to pick the appropriate number of basis vectors in the lower dimensional space, let us say K eigenvectors.
- Display some of the top K eigenvectors also called the eigenfaces.
- Show few examples of faces represented as a linear combination of the K eigenvectors and compare it with the original image 
- Perform face recognition in the lower dimensional space on the test images. Pick any test image to show the results.
- Write a report.
 


<a name='sub'></a>
## Submission Guidelines

Please submit the project <b> once </b> for your group -- there's no need for each member to submit
it. Make sure you write the names of all the students who worked on the project.

### File tree and naming

Your submission on Canvas must be a zip file, following the naming convention **YourDirectoryID_proj1.zip**.  For example, xyz123_proj1.zip.  The file **must have the following directory structure**.

YourDirectoryID_proj1.zip.
 - results/. containing some eigen faces and face recognition resulting images.
 - pca.ipynb
 - report.pdf

### Report
Logistics and bookkeeping you **must** include at the top of your report (-5 points for each one that's missing):

 - The name of each group member.
 - A brief (one paragraph or less) description of what each group member contributed to the project.


For each section of the project, explain briefly what you did, and describe any interesting problems you encountered and/or solutions you implemented.  You must include the following details in your writeup:

- how you picked the the lower dimensional basis vectors,
- the lower dimensional representation of a face and how similar or dissimilar it is to the original image.
- Report the accuracy of face recognition. Accuracy is defined as the ratio of the number of test images correctly recognized to the total number of test images.
- discuss briefly what you learned in the project.

As usual, your report must be full English sentences, **not** commented code. There is a word limit of 1500 words and no minimum length requirement

<a name='coll'></a>
## Allowed libraries

numpy, os, matplotlib

<a name='coll'></a>
## Collaboration Policy
You are encouraged to work on this project in groups of three at the most. The code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the CMSC426 Spring 2021 website.
