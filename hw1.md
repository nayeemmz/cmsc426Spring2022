---
layout: page
mathjax: true
title: Linear Least Squares
permalink: /2022/hw/hw1/
---

Table of Contents:
- [Due Date](#due)
- [Introduction](#intro)
- [What you need to do](#problem)
  - [Problem Statement](#pro)
- [Submission Guidelines](#sub)
- [Collaboration Policy](#coll)

<a name='due'></a>
## Due Date 
11:59PM, Tuesday, February 15, 2022

<a name='intro'></a>
## Introduction

This home work is designed to test your understanding of mathematics tutorial discussed in this [link](https://nayeemmz.github.io/cmsc426Spring2022/math-tutorial/). The task is to fit the line to two dimensional data points using different linear least square techniques discussed in the tutorials:

- Line fitting using Linear Least Squares
- Reduce overfitting using Regularization (ridge regression)

<a name='problem'></a>
## What you need to do

The 2D points data is provided in the form of .csv files (click [here](/cmsc426Spring2022/assets/hw1/data.zip) to download). The visualization of data with different noise level is shown in the following figure.

<div class="fig fighighlight">
  <img src="/cmsc426Spring2022/assets/hw1/data.jpg" width="100%">
  <div class="figcaption">
  </div>
  <div style="clear:both;"></div>
</div>

Please note that dataset 4 was generated specifically to test overfitting and to fine tune the regularization parameter, $$lambda$$ to overcome overfitting. This is a single variable data, so you would need to create higher dimensional data (as shown in class). Also, mean center your data before applying ridge regression.
<a name='pro'></a>
### Problem Statement 

- Write Python code to visualize geometric interpretation of eigenvalues/covariance matrix as discussed in this  [link](http://www.visiondummy.com/2014/04/geometric-interpretation-covariance-matrix/) [40 points]  
- Write Python code for least squares line fitting with and without regularization ( ridge regression ) [40 points]. 
- Discuss your results for line fitting in a report. [20 points]

<a name='sub'></a>
## Submission Guidelines

<b> If your submission does not comply with the following guidelines, you'll be given ZERO credit </b>

### File tree and naming

Your submission on Canvas must be a zip file, following the naming convention **YourDirectoryID_hw1.zip**.  For example, xyz123_hw1.zip.  The file **must have the following directory structure**, 

YourDirectoryID_hw1.zip.
 - data/. 
 - plot_eigen.ipynb
 - least_square.ipynb
 - report.pdf


### Report
For each section of the homework, explain briefly what you did, and describe any interesting problems you encountered and/or solutions you implemented.  You must include the following details in your writeup:

- Your understanding of eigenvectors and eigenvalues
- Reducing overfitting for each dataset
- Limitation of ridge regression


As usual, your report must be full English sentences, **not** commented code. There is a word limit of 750 words and no minimum length requirement

<a name='coll'></a>
## Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup.  For the full honor code refer to the CMSC426 Spring 2022 website.
