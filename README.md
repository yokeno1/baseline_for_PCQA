# Baseline_for_PCQA
# Point Cloud Quality Assessment (PCQA) Learning Repository

Welcome to the Point Cloud Quality Assessment (PCQA) Learning Repository! This repository is dedicated to learning, exploring, and implementing various techniques for evaluating the quality of point clouds.

## Table of Contents

- [Baseline\_for\_PCQA](#baseline_for_pcqa)
- [Point Cloud Quality Assessment (PCQA) Learning Repository](#point-cloud-quality-assessment-pcqa-learning-repository)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Repository Structure](#repository-structure)
  - [Learning-materials](#learning-materials)
  - [EXPERIMENT](#experiment)

## Introduction

Point Cloud Quality Assessment (PCQA) is an essential task in computer vision, especially for applications involving 3D data, such as virtual reality, autonomous driving, and 3D reconstruction. The goal of this repository is to provide resources and tools to help you learn about PCQA, from basic concepts to advanced algorithms.

## Repository Structure

The repository is organized as follows:

## Learning-materials
Here, we mainly conduct experiments using three PCQA methods: FR, RR, and NR.
The main reference comes from this link：[Point-cloud-quality-assessment](https://github.com/zzc-1998/Point-cloud-quality-assessment.git)

FR:
    1. P2point: [matlab](./matlab/point_to_point.m),[python](./point2point.py)  
    2. P2plane: [matlab](./matlab/point_to_plane.m),[python](./point2plane.py)  
    3. PointSSIM: The source code offers four selectable modes: geometry, normal, curvature, and color. In most PCQA articles, the specific mode used is not explicitly mentioned.  
    4. PCQM:  
    5.   
Note: For geometric only methods, due to color distortion in the SJTU dataset, we excluded this part for PLCC calculation

RR:

NR: 
    1. PQA-net:  
    2. IT-PCQA:  
    3. ResSCNN  
    4. MM-PCQA:  
    5. GMS-3DQA:  
    6. 3DTA:  


## EXPERIMENT
All experiments were implemented on a server with INTEL I9-14900K CPU, 64 GB RAM and NVIDIA RTX4090D-24G GPU.

|  metrics   | |SJTU | | | |WPC  | | |
|------------|-|-|-|-|-|-----|-|-|
|            |PLCC|SRCC|KRCC|RMSE|PLCC|SRCC|KRCC|RMSE|
|P2point_MSE | 0.775843 | 0.715329 | 0.536786 | 1.531142 | 0.457139 | 0.451657 | 0.312855 | 20.387780| 
|P2point_HD | 0.700806 | 0.671430 | 0.495518 | 1.731176 |0.358211 | 0.281550 | 0.191817 | 21.402017
|P2plane_MSE | 0.670508 | 0.605116 | 0.450819 | 1.800461 | 0.251108 | 0.326213 | 0.223586 | 22.923189 |
|P2plane_HD | 0.664976 | 0.627832 | 0.454506 | 1.812505 | 0.348689 | 0.291444 | 0.201330 | 21.484496 |
|PointSSIM |
|
|GMS-3DQA | 0.93189367 | 0.92208374 | 0.77271558 | 0.84681154 | 0.82700251 | 0.82313567 |  0.64041184 | 12.61126236 |
|MM-PCQA |
|

