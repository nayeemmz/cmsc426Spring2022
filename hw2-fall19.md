---
layout: page
mathjax: true
title: Clustering using GMM
permalink: /2019/hw/hw2/
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
11:59PM, Tuesday, Oct. 12, 2019

<a name='intro'></a>
## Introduction

A linear combination of Gaussian distributions forms a superposition formulated as a probabilistic model known as a Gaussian Mixture Model. 
The purpose of this homework is to practice Gaussian Mixture Models (GMM). More specifically you are required to use GMM's to cluster 2D data that will be provided to you.


There are two types of models that you will be building for this project:
- Data clustering using a single Gaussian Model.
- Data clustering using a Gaussian Mixture Model (GMM).

<a name='problem'></a>
## What you need to do
The data for this homework has been generated using three different Gaussian distributions, mixed together and shuffled. As a result there are three different distributions forming three different clusters. Your goal is to find those clusters. That means, for each of the distributions of the mixture model you would need to find their means ($$\mu$$), mixture coefficients ($$\pi$$) and the covariance matrices ($$\Sigma$$).

You may download the data from [here](/cmsc426fall2019/assets/hw2/data.csv). This data can be visualized as follows:
<center>
<div class="fig fighighlight">
  <img src="/cmsc426fall2019/assets/hw2/hw2_data.png" width="50%">
  <div class="figcaption">
  </div>
  <div style="clear:both;"></div>
</div>
</center>

<a name='pro'></a>
### Problem Statement

1. Write Python code to cluster the three distributions using a [Single Gaussian](https://nayeemmz.github.io/cmsc426fall2019/hw2colorseg/#gaussian) [30 points]
2. Write Python code to cluster the three distributions using a [Gaussian Mixture Model](https://nayeemmz.github.io/cmsc426fall2019/hw2colorseg/#gmm) [40 points] 
3. Plot all the GMM ellipsoids [10 points]. 
4. Write a report [20 points]

You are **NOT** allowed to use any built-in Python library code for GMM. To draw ellipses you may find the following [documentation](https://matplotlib.org/devdocs/gallery/statistics/confidence_ellipse.html) helpful.


### File tree and naming

Your submission on Canvas must be a zip file, following the naming convention **YourDirectoryID_proj1.zip**.  For example, xyz123_proj1.zip.  The file **must have the following directory structure**.

YourDirectoryID_proj1.zip.
 - results/.  - your plots
 - GMM.ipynb - include both Single Gaussian as well as GMM code.
 - report.pdf

### Report

For each section of the project, explain briefly what you did, and describe any interesting problems you encountered and/or solutions you implemented.  You must include the following details in your writeup:

- Your choice of initialization method.
- Explain why GMM is better than a single Gaussian.
- Present your clustering results for the datasets and show the Gaussians for each in a 2D heat map or a 3D scatter plot.
The following [link](https://matplotlib.org/mpl_toolkits/mplot3d/tutorial.html) would help with the 3D scatter plot. 
- Explain strengths and limitations of clustering using GMM. 
- Explain the effect of picking fewer or more number of Gaussians in GMM on clustering this data.

As usual, your report must be full English sentences, **not** commented code. There is a word limit of 1500 words and no minimum length requirement

<a name='coll'></a>
## Collaboration Policy
You are encouraged to discuss the ideas with your peers. However, the code should be your own, and should be the result of you exercising your own understanding of it. If you reference anyone else' code in writing your project, you must properly cite it in your code (in comments) and your writeup. For the full honor code refer to the CMSC426 Fall 2019 website.
