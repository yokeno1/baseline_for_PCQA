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

**FR:**  
    1. P2point: [matlab](./matlab/point_to_point.m),[python](./point2point.py)  
    2. P2plane: [matlab](./matlab/point_to_plane.m),[python](./point2plane.py)  
    3. PointSSIM: The source code offers four selectable modes: geometry, normal, curvature, and color. In most PCQA articles, the specific mode used is not explicitly mentioned.  
    4. PCQM:  
    5.   
Note: For geometric only methods, due to color distortion in the SJTU dataset, we excluded this part for PLCC calculation

RR:

**NR:**  
    1. PQA-net:  
    2. IT-PCQA:  
    3. ResSCNN  
    4. MM-PCQA:  
    5. GMS-3DQA:  
    6. 3DTA:  


## EXPERIMENT
All experiments were implemented on a server with INTEL I9-14900K CPU, 64 GB RAM and NVIDIA RTX4090D-24G GPU.
'P' and 'I' means point cloud and image modals respectively.
 
|  metrics   |Type |  Modal  | |SJTU | | | |WPC  | | |
|------------|-----|---------|-|-|-|-|-|-----|-|-|
|  |      |    |PLCC|SRCC|KRCC|RMSE|PLCC|SRCC|KRCC|RMSE|
|P2point_MSE |FR | P| 0.7758 | 0.7153 | 0.5367 | 1.5311 | 0.4571 | 0.4516 | 0.3128 | 20.3877| 
|P2point_HD|FR | P | 0.7008 | 0.6714 | 0.4955 | 1.7311 |0.3582 | 0.2815 | 0.1918 | 21.4020 |
|P2plane_MSE| FR| P | 0.6705 | 0.6051 | 0.4508 | 1.8004 | 0.2511 | 0.3262 | 0.2235 | 22.9231 |
|P2plane_HD|FR | P | 0.6649 | 0.6278 | 0.4545 | 1.8125 | 0.3486 | 0.2914 | 0.2013 | 21.4844 |
|PointSSIM|FR | P |  |   |   |   |  |  |   |  |
|GMS-3DQA|NR |I  | 0.9318 | 0.9220 | 0.7727 | 0.8468 | 0.8270 | 0.8231 |  0.6404 | 12.6112 |
|MM-PCQA|NR | P+I |
|IT-PCQA (train on SJTU)|NR|I |  0.7971 | 0.7034 | 0.5183 | 0.1471 | 0.4751 | 0.4549 | 0.3143 | 0.2105 |
|IT-PCQA(train on WPC) |NR|I |  0.7744 | 0.7566 | 0.5694 | 0.1542 | 0.6017 | 0.5981 | 0.4194 | 0.1911 |

