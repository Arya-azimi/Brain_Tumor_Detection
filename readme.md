# 🧠 Brain Tumor MRI Classification & Diagnosis System

A complete Deep Learning project for automatic brain tumor classification using MRI scans. This project combines Computer Vision, Transfer Learning, and an interactive diagnostic dashboard to assist in the identification of different brain tumor types from medical images.

The system is designed not only as a machine learning model but also as a deployable AI-powered diagnostic interface where users can upload MRI images and receive real-time predictions.

---

## Overview

Brain tumors are among the most critical neurological conditions and early diagnosis plays a vital role in treatment planning.

This project utilizes YOLO and Transfer Learning techniques to classify MRI images into multiple tumor categories.

The final solution includes:

* Data Exploration & Analysis
* Image Preprocessing Pipeline
* Deep Learning Model Training
* Performance Evaluation
* Interactive Streamlit Dashboard
* Single Image Prediction System

---

## Dataset

This project is based on the publicly available Kaggle dataset:

**Brain Tumor MRI Dataset for Deep Learning**

[Kaggle Dataset Source](https://www.kaggle.com/datasets/masoudnickparvar/brain-tumor-mri-dataset?utm_source=chatgpt.com)

Dataset contains MRI scans categorized into:

* Glioma Tumor
* Meningioma Tumor
* Pituitary Tumor
* No Tumor

The images are organized into training and testing folders which makes them suitable for supervised image classification tasks.

---

## Project Structure

```text
Brain_Tumor_Detection/

│
├── data
│   ├── train
│   │   ├── Glioma
│   │   │   └── images
│   │   ├── Meningioma
│   │   │   └── images
│   │   ├── No Tumor
│   │   │   └── images
│   │   └── Pituitary
│   │       ├── images
│   │       └── labels
│   └── val
│       ├── Glioma
│       │   └── images
│       ├── Meningioma
│       │   └── images
│       ├── No Tumor
│       │   └── images
│       └── Pituitary
│           └── images
└── training
|    └── train.py
|    └── yolov8s-cls.pt
|    └── runs
|        └── weights *
|
├── api/
│   └── main.py
├── dashboard/
│   └── app.py
│
├── requirements.txt
│
└── README.md
```

---

## Technologies Used

### Computer Vision

* YOLO

### Visualization

* plotly

### Deployment

* Streamlit

---

## Deep Learning Pipeline

### Data Preparation

MRI images are:

* Loaded automatically
* Resized to a fixed resolution
* Normalized
* Converted into numerical tensors

### Model Architecture

Transfer Learning is utilized through:

* YOLO8s-cls
* and can be others like openCV or ...

Depending on the available hardware and pretrained weights.

The network learns visual patterns associated with different tumor categories and produces probability scores for each class.

---

## Dashboard Features

The project includes a complete Streamlit-based diagnostic dashboard.

### Upload MRI Scan

Users can upload MRI images directly from their local machine.

### Real-Time Prediction

The trained model immediately predicts the tumor category.

### Confidence Score

Prediction confidence is displayed alongside the diagnosis.

### User-Friendly Interface

Designed for demonstration, education, and portfolio presentation purposes.

---

## Example Workflow

```text
Upload MRI Image
        ↓
Preprocessing
        ↓
Deep Learning Model
        ↓
Prediction
        ↓
Diagnostic Dashboard
```

---

## Evaluation Metrics

The model is evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

These metrics provide insight into how well the model distinguishes between different tumor classes.

---

## Industrial Applications

Although this project is intended for educational and research purposes, similar systems are used in:

* Medical Imaging Centers
* Hospitals
* Radiology Departments
* AI-Assisted Diagnostic Platforms
* Healthcare Research Labs

---

## Important Note

This project is **not a medical diagnostic tool** and should not be used for clinical decision-making.

The primary purpose of this implementation is:

* Learning Deep Learning workflows
* Demonstrating Transfer Learning techniques
* Understanding medical image classification
* Building deployable AI applications

---

## Future Improvements

Possible future enhancements include:

* Vision Transformers (ViT)
* EfficientNetV2
* Grad-CAM Explainability
* Multi-label Diagnosis
* FastAPI Backend
* Docker Deployment
* Cloud Inference
* Medical Report Generation
* Integration with Hospital Information Systems

---

## Results

The project demonstrates how MRI images can be processed and classified automatically using modern Deep Learning techniques while providing an intuitive dashboard for interactive single-image predictions.

It serves as a complete end-to-end Computer Vision project combining:

* Medical Imaging
* Deep Learning
* Model Deployment
* Interactive Visualization

into a single practical application.
