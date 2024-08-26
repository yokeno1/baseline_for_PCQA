# baseline_for_PCQA
# Point Cloud Quality Assessment (PCQA) Learning Repository

Welcome to the Point Cloud Quality Assessment (PCQA) Learning Repository! This repository is dedicated to learning, exploring, and implementing various techniques for evaluating the quality of point clouds.

## Table of Contents

- [baseline\_for\_PCQA](#baseline_for_pcqa)
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
    3. PointSSIM:  
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
