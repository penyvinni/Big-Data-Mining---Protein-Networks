# Vector Representation of Graphs and Visualization: Application in Protein Networks

**Course**: Data Mining  
**Student**: Vinni Panagiota  
**Assignment**: Lab Exercise 2 - "Vector Representation of Graphs and Visualization: Application in Protein Networks"  
**Semester**: 2nd  
**Email**: penyvinni@gmail.com  

---

## Table of Contents

1. [Overview](#overview)
2. [Objective](#objective)
3. [Algorithm Description](#algorithm-description)
4. [Files](#files)
5. [Setup and Dependencies](#setup-and-dependencies)
6. [Usage Instructions](#usage-instructions)
7. [Results Visualization](#results-visualization)
8. [Conclusion](#conclusion)

---

## Overview

This project explores the application of the **Node2Vec** algorithm for analyzing protein networks and generating vector representations from these networks. **t-SNE** is employed to reduce the dimensionality of these embeddings, facilitating the visualization of structural and functional relationships between proteins. The biological datasets used include protein-protein interactions from the **Human Protein Reference Database (HPRD)** and structural information from the **Protein Data Bank (PDB)**.

---

## Objective

The main objectives of this project are:

- To understand the application of **Node2Vec** in producing feature representations from protein graph networks.
- To implement **t-SNE** for dimensionality reduction of the embeddings for visualization purposes.
- To analyze and interpret the visual patterns of protein interaction data to formulate hypotheses regarding biological functions and interactions.
- To explore real-world datasets involving protein interactions and structural information.

---

## Algorithm Description

### Node2Vec Algorithm

**Node2Vec** is a node embedding algorithm that learns low-dimensional representations for the nodes of a graph. It is an extension of the **Word2Vec** algorithm for word embeddings. The key steps include:

1. **Purpose**: Converting each graph node into a low-dimensional vector representing its relationships with other nodes.
2. **Graph Walks**: Biased random walks are performed to sample node neighborhoods for feature learning.
3. **Applications**: Node2Vec is widely used in social network analysis, biological network analysis, and recommendation systems.

### t-SNE

**t-SNE (t-distributed Stochastic Neighbor Embedding)** is a dimensionality reduction technique that converts high-dimensional data into a lower-dimensional space, maintaining the relationships between the points.

---

## Files

- **brca.tsv**: Protein interaction data for breast cancer.
- **leuk.tsv**: Protein interaction data for leukemia.
- **main_code.ipynb**: Jupyter notebook containing the code implementation.
  
---

## Setup and Dependencies

To run the project, the following Python libraries are required:

- `pandas`
- `networkx`
- `node2vec`
- `sklearn`
- `numpy`
- `matplotlib`
- Google Colab or local Jupyter notebook environment

You can install the necessary libraries by running:

```bash
pip install pandas networkx node2vec scikit-learn numpy matplotlib
