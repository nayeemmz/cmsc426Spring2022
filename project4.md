---
layout: page
mathjax: true
title: Implementation of Convolutional Neural Networks using Numpy and Tensorflow
permalink: /proj/p4/
---

Table of Contents:
- [Deadline](#due)
- [Introduction](#intro)
- [Implementation Overview](#system_overview)
- [Submission Guidelines](#sub)
- [Collaboration Policy](#coll)

<a name='due'></a>
## Deadline
11:59 PM, May 20, 2021

<a name='intro'></a>
## Introduction
In this project you will implement a Convolutional Neural Network (CNN) in two different ways: 
  * a step by step approach using Numpy, and  
  * using Tensorflow framework to perform classification of Cifar10  dataset.
 
The goal of this assignment is to help you understand CNN's by building their different components. You will be applying your Tensorflow CNN implementation on the CIFAR10 dataset classification. In both approaches some of the components include, forward convolution, backward convolution, zero padding, max-pooling and average-pooling. Backpropagation code is provided to you.

In order to help you implement this you are provided with [starter code](/cmsc426Spring2021/assets/proj4/project4-starterFiles.zip) that contains two Jupyter notebooks and images necessary for this project. The files <i>cnn-with-backprop.ipynb</i> and <i>Cifar10ClassificationUsingCNN.ipynb</i> are to be used for the step by step approach and the Tensorflow framework approach, respectively. The descriptions of these files are as follows:

<ul>

  <li> cnn-with-backprop.ipynb - backpropagation algorithm is implemented in this file. Start with this file.
  </li>
  <li> Cifar10ClassificationUsingCNN.ipynb is to be used for our second approach using Tensorflow framework.
 </li>
</ul>



A detailed description of these files is being skipped here because an elaborate documentation has been included in each one of these files. The comments in the files are self explanatory and include locations where you are required to fill in your code. In addtion, you may refer to the Artificial Neural Networks and Convolutional Neural Networks lectures covered in class.


<a name='system_overview'></a>
## What to Implement

Most of the implementation details are provided to you in the Jupyter notebooks. You would be required to write code in these files identified by the comments in them. 


<a name='sub'></a>
## Submission Guidelines
You are required to submit the following files:
 * cnn-with-backprop.ipynb for the step by step approach to build a Convolutional Neural Network. (40 points)
 * Cifar10ClassificationUsingCNN.ipynb for the Tensorflow framework approach to classify CIFAR10 data . (40 points)
 * Report should contain a detailed description of the answers to the questions inside the second Jupyter notebook as a markdown. Some of those questions are included in the Jupyter notebook (20 points)
 


Please add a new markdown cell at the top of your Jupyter notebooks and include
 - The name of each group member.
 - A brief (one paragraph or less) description of what each group member contributed to the project.

<a name='coll'></a>
## Collaboration Policy
We encourage you to work closely with your groupmates, including collaborating on writing code.  With students outside your group, you may discuss methods and ideas but may not share code.

For the full collaboration policy, including guidelines on citations and limitations on using online resources, see <a href="http://www.cs.umd.edu/class/Spring2021/cmsc426-0101/">the course website</a>.
