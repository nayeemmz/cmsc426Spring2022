---
layout: page
mathjax: true
permalink: /colorseg/
---

Table of Contents:

- [Color Classification](#colorclassification)
	- [Color Classification using a Single Gaussian](#gaussian)
	- [Color Classification using a Gaussian Mixture Model (GMM)](#gmm)
  - [Different cases for $$\Sigma$$ in GMM](#gmmcases)


<a name='gaussian'></a>
### Clustering using a Single Gaussian
You may think of this problem as assigning a color label to each pixel. Each distribution may represent a red, green or blue cluster. We want to cluster a pixel(point) as red, green or blue as we have a total of three classifiers, one for each color. Let us formulate the problem mathematically. In each classifier, we want to find $$p(C_i \vert x)$$. Here $$C_i$$ denotes the cluster label. So as you expect the first classifier will give you the following $$p(C_1 \vert x)$$, i.e., probability that the pixel is the first cluster or may be belong to the red channel. Note that $$1 - p(C_1 \vert x)$$ gives the probability that the pixel is not from cluster 1 which includes both cluster 2 and 3 points (pixels). 

Estimating $$p(C_i \vert x)$$ directly is too difficult. Luckily, we have Bayes rule to rescue us! Bayes rule applied onto $$p(C_i \vert x)$$ gives us the following:

$$
p(C_i\vert x) = \frac{p(x \vert C_i)p(C_i)}{\sum_{i=1}^K p(x \vert C_i)p(C_i)}
$$


$$p(C_i \vert x)$$ is the conditional probability of a cluster label given the cluster observation and is called the **Posterior**. $$p(x \vert C_i)$$ is the conditional probability of cluster observation given the cluster label and is generally called the **Likelihood**. $$p(C_i)$$ is the probability of that cluster occuring and is called the **Prior**. The prior is used to increase/decrease the probability of certain clusters. If nothing about the prior is known, a common choice is to use a uniform distribution, i.e., all the clusters are equally likely. This type of clustering is an unsupervised learning problem. Unsupervised means that we do not have labeled "training" examples from which we can understand the cluster we are looking for. 

For the purpose of easy discussion, we want to look for the points that are similae to each other and are more likely to come from the same distribution and hence grouped together. The Likelihood is generally modelled as a normal/gaussian distribution given by the following equation:

$$
p(x \vert \mu,\Sigma) = \frac{1}{\sqrt{(2 \pi)^3 \vert \Sigma \vert}}\exp{(\frac{-1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu))} = \mathcal{N(x \vert \mu, \Sigma)}
$$

Here, $$\vert \Sigma \vert$$ denotes the determinant of the matrix $$\Sigma$$. The dimensions of the above terms are as follows: $$\Sigma \in \mathbb{R}^{2 \times 2}, x,\mu \in \mathbb{2 \times 1}, p(x \vert \mu, \Sigma) \in \mathbb{R}^1$$. 

You might be asking why we used a Gaussian distribution to model the likelihood. The answer is simple, when you average a lot of (theoretically $$\infty$$) independently identically distributed random samples, their distribution tends to become a gaussian. This is formally called the [**Central Limit Theorem**](https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/sampling-distribution-mean/v/central-limit-theorem). 

All the math explanation is cool but how do we implement this? It's simpler than you think. All you have to do is find the mean ($$\mu$$) and covariance ($$\Sigma$$) of the likelihood gaussian distribution. Let us assume that we have $$N$$ samples for the cluster where each sample is of size $$\mathbb{R}^{2 \times 1}$$ representing the 2D information at a particular point. The empirical mean $$\mu$$ is computed as follows:

$$
\mu = \frac{1}{N}\sum_{i=1}^N x_i
$$

here $$i$$ denotes the sample number. The empirical co-variance $$\Sigma$$ is compted as follows:

$$
\Sigma = \frac{1}{N}\sum_{i=1}^N (x_i-\mu)(x_i-\mu)^T
$$

Clearly, $$\mu \in \mathbb{2 \times 1}$$ and $$\Sigma \in \mathbb{R}^{2 \times 2}$$. $$\Sigma$$ is an awesome matrix and has some cool properties. Let us discuss a few of them.  

The co-variance matrix $$\Sigma$$ is a square matrix of size $$d \times d$$ where $$d$$ is the length of the vector $$x$$, i.e., $$\Sigma \in \mathbb{R}^{d \times d}$$ if $$x \in \mathbb{R}^{d \times 1}$$. 

<a name='gmm'></a>
### Clustering using a Gaussian Mixture Model (GMM)
However, if you are trying to find clusters for a multi-modal distribution a simple gaussian model will not suffice.
In this case, one has to come up with a weird looking fancy function to bound the points which is generally mathematically very difficult and computationally very expensive. An easy trick mathematicians like to do in such cases (which is generally a very good approximation with less computational cost) is to represent the fancy function as a sum of known simple functions. We love gaussians so let us use a sum of gaussians to model our fancy function. Let us write our formulation down mathematically. Let the posterior be defined by a sum of $$K$$ scaled gaussians given by:

$$
p(C_i \vert x) = \sum_{i=1}^k \pi_i \mathcal{N}(x, \mu_i, \Sigma_i)
$$

Here, $$\pi_i$$, $$\mu_i$$ and $$\Sigma_i$$ respectively define the scaling factor, mean and co-variance of the $$i$$<sup>th</sup> gaussian. The optimization problem in hand is to maximize the probability that the above model is correct, i.e., to find the parameters $$\pi_k, \mu_k, \Sigma_k$$ such that one would maximize the corectness of $$p(C_i \vert x)$$. Just a simple probability function doesnt have very pretty mathematical properties. So a general trick mathematicians/machine learning people follow is to take the logarithm of the probability function and maximize that. This works well because of the [monotonicity](http://mathworld.wolfram.com/MonotonicFunction.html) of the logarithm function. This setup is formally called **Maximum Likelihood Estimation (MLE)** and can be mathematically written as:

$$
\underset{\{ \mu_1, \mu_2, \cdots, \mu_k, \Sigma_1, \Sigma_2, \cdots, \Sigma_k, \pi_1, \pi_2, \cdots, \pi_k\}}{\operatorname{argmax}} \sum_{i=1}^N \ln \sum_{k=1}^K\pi_k\mathcal{N}(x_i \vert \mu_k, \Sigma_k
$$

where $$N$$ is the number of training samples. The above is not a simple function and generally has no closed form solution. To solve for the parameters $$\Theta = \{ \mu_1, \mu_2, \cdots, \mu_k, \Sigma_1, \Sigma_2, \cdots, \Sigma_k, \pi_1, \pi_2, \cdots, \pi_k\}$$ of the above problem, we have to use an iterative procedure, called the Expectation-Maximization algorithm presented as follows: 

- Initialization:
Randomly choose $$\pi_i, \mu_i, \Sigma_i \qquad \forall i \in [1, k]$$. Evaluate log likelihood.
- Alternate until convergence:
	- Expectation Step or E-step: Evaluate the model/Assign points to clusters
	Cluster Weight $$ \gamma_{i,j} = \frac{\pi_i p(x_j \vert C_i)}{\sum_{i=1}^k \pi_i p(x_j \vert C_i)} $$
	\\(j\\) is the data point index, \\(i\\) is the cluster index.
	- Maximization Step or M-step: Evaluate best parameters $$ \Theta $$ to best fit the points
	
	$$ 
	\mu_i = \frac{\sum_{j=1}^N \alpha_{i,j} x_j}{\sum_{j=1}^N \gamma_{i,j}}
	$$
	

	$$ 
	\Sigma_k = \frac{\sum_{j=1}^N \alpha_{i,j} (x_j-\mu_i)(x_j-\mu_i)^T}{\sum_{j=1}^N \gamma_{i,j}}
	$$

	$$ 
	\pi_i = \frac{1}{N}\sum_j \gamma_{i,j}
	$$
	
Convergence is defined as $$\sum_i\vert \vert \mu_i^{t+1} -  \mu_i^{t}\vert \vert \le \tau$$ where $$i$$ denotes the cluster number, $$t$$ denotes the iteration number and $$\tau$$ is some user defined threshold. To understand more about the mathematical derivation which is fairly involved go to [this link](https://alliance.seas.upenn.edu/~cis520/dynamic/2017/wiki/index.php?n=Lectures.EM).

Now that we have estimated/learnt all the parameters in our model, i.e., $$\Theta = \{ \mu_1, \mu_2, \cdots, \mu_k, \Sigma_1, \Sigma_2, \cdots, \Sigma_k, \pi_1, \pi_2, \cdots, \pi_k\}$$ we can estimate the posterior probability using the following equation:

$$
p(C_i \vert x) = \sum_{i=1}^k \pi_i \mathcal{N}(x, \mu_i, \Sigma_i)
$$ 




<!-- When git doesn't push do this: git config --global core.askpass "git-gui--askpass" -->
