---
layout: page
mathjax: true
title: Image Classification Using Bag of Features and Support Vector Machines
permalink: /proj/p3/
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
11:59 PM, Sunday, April 16, 2021

<a name='intro'></a>
## Introduction
In this homework you will implement an image classifier.You will be building Support Vector Machine (SVM)
classifier to classify images of Caltech-101 dataset.
Supervised classification is a computer vision task of categorizing unlabeled images to different categories or
classes. This follows the training using labeled images of the same categories. You may download Caltech-101 data
set from the following [link](http://www.vision.caltech.edu/Image_Datasets/Caltech101/#Download). All the images of this dataset are stored in folders, named for each category. However, we will be using just three of those categories: airplanes, dolphin and Leopards. You could download those three image datasets from the following [link]( https://nayeemmz.github.io/cmsc426Spring2022/assets/proj3/Caltech-dataset.zip). Since there are fewer dolphins than the other categories, we will use same number of images for the other categories as well. You would
use 90% of these labeled images as training data set to train SVM classifier, after obtaining a bag (histogram) of visual words for each image. The classification would be one-vs-all, where
you would specifically consider one image category at a time to classify and consider it as a positive example and all other
category images as negative examples. Once the classifier is trained you would test the remaining 10% of the data and predict their label for classification
as one of the three categories. This task can be visualized in Figure 1.

<div class="fig fighighlight">
  <img src="/cmsc426Spring2022/assets/proj3/proj3.png" width="100%">
  <div class="figcaption">
  </div>
  <div style="clear:both;"></div>
</div>


<a name='part1'></a>
## Part 1: Implementation (50 pts)


There are three major steps in this approach.

## Creating bag of visual words

You could use Scale-Invariant Feature Transform (SIFT) from you OpenCV contrib library to obtain feature descriptors or any other library for it for the purposes of this project. You could also use HOG features for this project. In addition, you may use the sift code provided at [link]( https://nayeemmz.github.io/cmsc426Spring2022/assets/proj3/sift.ipynb). I will leave that up to you to test. The descriptor for each image will be a matrix of size, $$keypoints \times 128$$. If there are different number of keypoints for different images, you may use only the strongest keypoints determined by the image having the smallest number of keypoints. Once the descriptors for each keypoint are obtained you may stack them for the entire training set. Use this matrix of feature descriptors as a training input to k-Means clustering algorithm. The centroids of the clusters form a visual dictionary vocabulary. Use this visual vocabulary to make a frequency histogram for each image, based on the frequency of vocabularies in them. In other words you are trying to figure out the number of occurrences of each visual vocabulary word in each image. These histograms are the bag of visual words. The length of the histogram is the same as the number of clusters. Please note that the number of clusters is not limited by the number of categories, since it is dependent on the keypoints and visual words surrounding them, you should train K-Means for hundreds of clusters. I have tried 400 but you are free to test other numbers.

Go over the slides to understand SIFT / HoG, K-Means algorithm and bag of visual words (BoVW). While you may use Python libraries to train the Support vector classifier you would write your own code for k-Means algorithm. For a detailed description of the bag of visual words technique, follow the graphic above and read the following [paper](https://www.cs.cmu.edu/~efros/courses/LBMV07/Papers/csurka-eccv-04.pdf).

<!--[Here](/cmsc426fall2019/assets/proj3/regionalextrema.ipynb) is some starter code for extrema detection step.-->

## SVM Classifier Training

Train SVM on the resulting histograms (each histogram is a feature vector, with a label) obtained as a bag of visual words in the previous step. For a thorough understanding of SVM, refer to the heavily cited [paper](https://www.di.ens.fr/~mallat/papiers/svmtutorial.pdf), by Christopher Burges.

You would need to train the classifiers as one vs. all. Wherein only the category that you are training for, is considered to be a positive example and the other two categories are treated as negative examples. You may use svm from sklearn in Python.

## Test your model

Extract the bag of visual words for the test image and then pass it as an input to the SVM models you created during
training to predict its label. That means it would be tested using all the SVM classifiers and assigned the label that gives the highest score.

<a name='part2'></a>
## Part 2: - What to submit (50 points)

1. Show a 3 x 3 confusion matrix with categories as its rows and columns. It is used to determine the
accuracy of your classifier. In this matrix the rows are the actual category label and the columns are the predicted
label. Each cell in this matrix will contain the prediction count. Ideally, we would like all the off-diagonal
numbers in this matrix to be 0’s, however, that is not always possible. For example in the matrix below with
100 images of each of the three categories, airplanes, dolphin, Leopards,
<div class="fig fighighlight">
  <img src="/cmsc426Spring2022/assets/proj3/confusion.png" width="50%">
  <div class="figcaption">
  </div>
  <div style="clear:both;"></div>
</div>
the confusion matrix can be read as, airplane was correctly classified as an airplane, 93 times, and wrongly classified as
dolphin and leopard, two times and five times, respectively. Similarly, dolphin was correctly classified 98 out of 100 times
and leopard was also correctly classified 98% of the time.

2. A plot showing the histogram of the visual vocabulary during the training phase. You can pick any image you
like.

3. Some of the image patches corresponding to the words in the visual vocabulary (cluster centroids).


<a name='sub'></a>
## Submission Guidelines

File tree and naming
Your submission on Canvas must be a zip file, following the naming convention YourDirectoryID_proj3.zip. For
example, xyz123_proj3.zip. The file must have the following directory structure, based on the starter files
- mysvm.ipynb
- report.pdf

### Report

Please include the plot and confusion matrix as mentioned in part 2. Also include your observations about the
prediction of test images.
As usual, your report must be full English sentences,not commented code

<a name='coll'></a>
## Collaboration Policy
You are encouraged to work in groups of three for this project. You may discuss the ideas with your peers from other groups. If you reference anyone else's code in writing your project, you must properly cite it in your code (in comments) and your writeup.  For the full honor code refer to the CMSC426 Spring 2022 website.
