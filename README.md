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

---

## Usage Instructions

1. Load the Data: Start by loading the protein interaction data from either `brca.tsv` (breast cancer) or `leuk.tsv` (leukemia).
2. Run the Node2Vec Algorithm: The script trains a Node2Vec model on the graph and learns vector representations for the nodes.
3. t-SNE Dimensionality Reduction: Apply t-SNE to the node embeddings to reduce their dimensionality for visualization.
4. Visualization: Plot the reduced embeddings using a scatter plot to analyze the structural patterns in the protein network.

---

## Results Visualization

The results are visualized as 2D scatter plots showing the protein-protein interaction networks:

* Breast Cancer (BRCA): The visualization highlights structural and functional relationships between proteins associated with breast cancer.

![brca](https://github.com/user-attachments/assets/bb32b190-d6c2-4b87-af57-4223dae07ad5)

* Leukemia (LEUK): The visualization shows the relationships and interactions of proteins involved in leukemia, helping identify patterns in the network structure.

![leuk](https://github.com/user-attachments/assets/6db77e07-08de-4267-8da1-c2d1b648aba7)


---

## Conclusion
This project demonstrates the use of Node2Vec for generating graph embeddings from protein networks and visualizing them using t-SNE. The resulting visualizations provide insights into the structural and functional relationships within the protein networks, potentially revealing biological pathways and interactions.
