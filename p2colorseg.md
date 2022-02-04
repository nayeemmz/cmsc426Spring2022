---
layout: page
mathjax: true
permalink: /p2colorseg/
---

Table of Contents:

- [Color Classification](#colorclassification)
	- [Color Classification using a Single Gaussian](#gaussian)
	- [Color Classification using a Gaussian Mixture Model (GMM)](#gmm)

<a name='gaussian'></a>
### Clustering using a Single Gaussian
You may think of this problem as assigning a color label to each pixel. Each distribution may represent a red, green or blue cluster. We want to cluster a pixel(point) as red, green or blue as we have a total of three classifiers, one for each color. Let us formulate the problem mathematically. In each classifier, we want to find $$p(C_k \vert x)$$. Here $$C_k$$ denotes the cluster label. So as you expect the first classifier will give you the following $$p(C_1 \vert x)$$, i.e., probability that the pixel is the first cluster or may be belong to the red channel. Note that $$1 - p(C_1 \vert x)$$ gives the probability that the pixel is not from cluster 1 which includes both cluster 2 and 3 points (pixels).

Estimating $$p(C_k \vert x)$$ directly is too difficult. Luckily, we have Bayes rule to rescue us! Bayes rule applied onto $$p(C_k \vert x)$$ gives us the following:

$$
p(C_k\vert x) = \frac{p(x \vert C_k)p(C_k)}{\sum_{k=1}^K p(x \vert C_k)p(C_k)}
$$

$$p(C_k \vert x)$$ is the conditional probability of a cluster label given the cluster observation and is called the **Posterior**. $$p(x \vert C_k)$$ is the conditional probability of cluster observation given the cluster label and is generally called the **Likelihood**. $$p(C_k)$$ is the probability of that cluster occurring and is called the **Prior**. The prior is used to increase/decrease the probability of certain clusters. If nothing about the prior is known, a common choice is to use a uniform distribution, i.e., all the clusters are equally likely. This type of clustering is an unsupervised learning problem. Unsupervised means that we do not have labeled "training" examples from which we can understand the cluster we are looking for.

For the purpose of easy discussion, we want to look for the points that are similar to each other and are more likely to come from the same distribution and hence grouped together. The Likelihood is generally modelled as a normal/Gaussian distribution given by the following equation:

$$
p(x \vert \mu,\Sigma) = \frac{1}{\sqrt{(2 \pi)^3 \vert \Sigma \vert}}\exp{(\frac{-1}{2}(x-\mu)^T\Sigma^{-1}(x-\mu))} = \mathcal{N(x \vert \mu, \Sigma)}
$$

Here, $$\vert \Sigma \vert$$ denotes the determinant of the matrix $$\Sigma$$. The dimensions of the above terms are as follows: $$\Sigma \in \mathbb{R}^{2 \times 2}, x,\mu \in \mathbb{2 \times 1}, p(x \vert \mu, \Sigma) \in \mathbb{R}^1$$.

You might be asking why we used a Gaussian distribution to model the likelihood. The answer is simple, when you average a lot of (theoretically $$\infty$$) independently identically distributed random samples, their distribution tends to become a Gaussian. This is formally called the [**Central Limit Theorem**](https://www.khanacademy.org/math/ap-statistics/sampling-distribution-ap/sampling-distribution-mean/v/central-limit-theorem).

All the math explanation is cool but how do we implement this? It's simpler than you think. All you have to do is find the mean ($$\mu$$) and covariance ($$\Sigma$$) of the likelihood Gaussian distribution. Let us assume that we have $$N$$ samples for the cluster where each sample is of size $$\mathbb{R}^{2 \times 1}$$ representing the 2D information at a particular point. The empirical mean $$\mu$$ is computed as follows:

$$
\mu = \frac{1}{N}\sum_{n=1}^N x_n
$$

here $$n$$ denotes the sample number. The empirical co-variance $$\Sigma$$ is computed as follows:

$$
\Sigma = \frac{1}{N}\sum_{n=1}^N (x_n-\mu)(x_n-\mu)^T
$$

Clearly, $$\mu \in \mathbb{2 \times 1}$$ and $$\Sigma \in \mathbb{R}^{2 \times 2}$$. $$\Sigma$$ is an awesome matrix and has some cool properties. Let us discuss a few of them.

The co-variance matrix $$\Sigma$$ is a square matrix of size $$d \times d$$ where $$d$$ is the length of the vector $$x$$, i.e., $$\Sigma \in \mathbb{R}^{d \times d}$$ if $$x \in \mathbb{R}^{d \times 1}$$.

<a name='gmm'></a>
### Clustering using a Gaussian Mixture Model (GMM)
However, if you are trying to find clusters for a multi-modal distribution a simple Gaussian model will not suffice.
In this case, one has to come up with a weird looking fancy function to bound the points which is generally mathematically very difficult and computationally very expensive. An easy trick mathematicians like to do in such cases (which is generally a very good approximation with less computational cost) is to represent the fancy function as a sum of known simple functions. We love Gaussian so let us use a sum of Gaussians to model our fancy function. Let us write our formulation down mathematically. We will model the distribution of our data using a sum of $$K$$ scaled Gaussians:

$$
p(x) = \sum_{k=1}^K \pi_k \mathcal{N}(x, \mu_k, \Sigma_k)
$$

Here, $$\pi_k$$, $$\mu_k$$ and $$\Sigma_k$$ respectively define the scaling factor, mean and covariance of the $$k$$<sup>th</sup> Gaussian. The optimization problem in hand is to maximize the probability that the above model is correct, i.e., to find the parameters $$\pi_k, \mu_k, \Sigma_k$$ such that one would maximize the correctness of $$p(x)$$. Just a simple probability function doesn't have very pretty mathematical properties. So a general trick mathematicians/machine learning people follow is to take the logarithm of the probability function and maximize that. This works well because of the [monotonicity](http://mathworld.wolfram.com/MonotonicFunction.html) of the logarithm function. This setup is formally called **Maximum Likelihood Estimation (MLE)** and can be mathematically written as:

$$
\underset{\{ \mu_1, \mu_2, \cdots, \mu_k, \Sigma_1, \Sigma_2, \cdots, \Sigma_k, \pi_1, \pi_2, \cdots, \pi_k\}}{\operatorname{argmax}} \sum_{n=1}^N \ln \sum_{k=1}^K\pi_k\mathcal{N}(x_n \vert \mu_k, \Sigma_k)
$$

where $$N$$ is the number of training samples. The above is not a simple function and generally has no closed form solution. To solve for the parameters $$\Theta = \{ \mu_1, \mu_2, \cdots, \mu_k, \Sigma_1, \Sigma_2, \cdots, \Sigma_k, \pi_1, \pi_2, \cdots, \pi_k\}$$ of the above problem, we have to use an iterative procedure, called the Expectation-Maximization algorithm presented as follows:

- Initialization:
Randomly choose $$\pi_k, \mu_k, \Sigma_k$$ for any $$k$$ in $$[1, K]$$.
- Alternate until convergence:
	- Expectation Step or E-step: Evaluate the model/Assign points to clusters
	Cluster Weight $$ \gamma_{n,k} = \frac{\pi_k p(x_n \vert C_k)}{\sum_{k=1}^K \pi_k p(x_n \vert C_k)} $$
	\\(n\\) is the data point index, \\(k\\) is the cluster index.
	- Maximization Step or M-step: Evaluate best parameters $$ \Theta $$ to best fit the points

	$$
	\mu_k = \frac{\sum_{n=1}^N \gamma_{n,k} x_n}{\sum_{n=1}^N \gamma_{n,k}}
	$$

	$$
	\Sigma_k = \frac{\sum_{n=1}^N \gamma_{n,k} (x_n-\mu_k)(x_n-\mu_k)^T}{\sum_{n=1}^N \gamma_{n,k}}
	$$

	$$
	\pi_k = \frac{1}{N}\sum_{n=1}^N \gamma_{n,k}
	$$

Convergence is defined as $$\sum_{k=1}^K\| \mu_k^{t+1} -  \mu_k^{t}\| \le \tau$$ where $$k$$ denotes the cluster number, $$t$$ denotes the iteration number and $$\tau$$ is some user defined threshold. To understand more about the mathematical derivation which is fairly involved go to [this link](https://alliance.seas.upenn.edu/~cis520/dynamic/2017/wiki/index.php?n=Lectures.EM).

Now that we have estimated/learnt all the parameters in our model, i.e., $$\Theta = \{ \mu_1, \mu_2, \cdots, \mu_k, \Sigma_1, \Sigma_2, \cdots, \Sigma_k, \pi_1, \pi_2, \cdots, \pi_k\}$$ we can estimate the posterior probability of the $$k$$th cluster using the following equation:

$$
p(C_k \vert x) = \frac{\pi_k \mathcal{N}(x, \mu_k, \Sigma_k)}{\sum_{k=1}^K \pi_k \mathcal{N}(x, \mu_k, \Sigma_k)}
$$

<!-- When git doesn't push do this: git config --global core.askpass "git-gui--askpass" -->
