# 🚀 Python Data Representation & Analysis Projects

A comprehensive collection of advanced Python projects showcasing signal processing, time series analysis, graph algorithms, and machine learning techniques for real-world data challenges.

## 📋 Project Overview

This repository contains cutting-edge implementations of data representation and analysis techniques across multiple domains, demonstrating proficiency in Python programming, mathematical modeling, and data science methodologies.

---

## 🎵 A6 Audio Signal Processing & Compression

**Exploring the frequency domain of audio signals through advanced DSP techniques**

### 🔧 Key Features:
- **Audio File Processing** 🎧 - Load and playback WAV files using Python libraries
- **Fast Fourier Transform (FFT)** 📊 - Convert time-domain signals to frequency representations
- **Signal Combination** 🔀 - Merge frequency domain representations of multiple audio sources
- **Inverse FFT (IFFT)** ↩️ - Reconstruct time-domain signals from frequency data
- **Short-Time Fourier Transform (STFT)** ⏱️ - Analyze time-frequency characteristics
- **Spectrogram Visualization** 🌈 - Create compelling visual representations of audio data

### 💡 Technical Highlights:
- Real-time audio processing and playback
- Advanced frequency domain analysis and manipulation
- Time-frequency decomposition for complex audio signals
- Interactive spectrogram interpretation

---

## 📈 A7: Time Series & Graph Analytics

**Advanced temporal data analysis and graph theory implementations**

### 📊 Time Series Analysis Features:
- **Data Preprocessing** 🔄 - Pandas-based datetime parsing and indexing
- **Temporal Visualization** 📉 - Multi-variable time series plotting with correlation analysis
- **Decomposition Analysis** 🧩 - Trend and seasonal component extraction
- **Signal Smoothing** 🌊 - Simple Moving Average (SMA) and Exponential Moving Average (EMA)
- **Stationarity Testing** 📏 - Augmented Dickey-Fuller (ADF) statistical tests
- **Differencing Techniques** 🔄 - First-order differencing for stationarity achievement

### 🌐 Graph Algorithm Implementations:
- **Dijkstra's Algorithm** 🗺️ - Shortest path computation from Chicago O'Hare (ORD)
- **Minimum Spanning Tree** 🌳 - Both Prim's and Kruskal's algorithm implementations
- **Weighted Graph Processing** ⚖️ - Real-world airport network analysis

### 💻 Technical Stack:
- **Libraries**: Pandas, NumPy, Matplotlib, NetworkX, Statsmodels
- **Algorithms**: Advanced graph traversal and optimization techniques
- **Statistical Methods**: Time series stationarity testing and decomposition

---

## 🤖 A8: Machine Learning for Text & Images

**Dual-domain ML applications: NLP sentiment analysis and computer vision**

### 📝 Part 1: Sentiment Classification Engine
- **Text Preprocessing Pipeline** 🔧 - Tokenization, stopword removal, stemming/lemmatization
- **Feature Engineering** 📊 - Advanced text vectorization techniques
- **Data Visualization** 📈 - Word frequency plots, word clouds, distribution analysis
- **Binary Classification** 🎯 - Logistic Regression vs Support Vector Machine comparison
- **Performance Metrics** 📏 - Comprehensive accuracy reporting and confusion matrices

### 🖼️ Part 2: Facial Image Reconstruction
- **Computer Vision Processing** 👁️ - Olivetti Faces dataset manipulation
- **Image Preprocessing** 🎨 - Vertical splitting and data preparation
- **Support Vector Regression** 🧠 - Left-to-right face completion model
- **Visual Results** 🖥️ - Side-by-side reconstruction comparisons
- **Bonus Challenge** ⭐ - Random Forest Regression implementation and comparison

---

## 🛠️ Technologies & Libraries Used

```python
# Core Data Science Stack
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Signal Processing
from scipy.fft import fft, ifft
from scipy.signal import stft
import librosa
import soundfile as sf

# Machine Learning
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, SVR
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import accuracy_score, confusion_matrix

# Time Series Analysis
from statsmodels.tsa.seasonal import seasonal_decompose
from statsmodels.tsa.stattools import adfuller

# Graph Algorithms
import networkx as nx
import heapq
```

## 🎯 Skills Demonstrated

- **Signal Processing** 🔊 - FFT/IFFT, STFT, spectrogram analysis
- **Time Series Analysis** ⏰ - Decomposition, stationarity, smoothing techniques
- **Graph Theory** 🕸️ - Shortest path algorithms, MST implementations
- **Machine Learning** 🤖 - Classification, regression, model comparison
- **Data Visualization** 📊 - Advanced plotting and interpretation
- **Statistical Analysis** 📐 - Hypothesis testing, performance evaluation

## 🚦 Getting Started

1. **Clone the repository**:
   ```bash
   git clone [repository-url]
   cd python-data-representation-projects
   ```

2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run individual assignments**:
   ```bash
   python assignment_6_audio_processing.py
   python assignment_7_timeseries_graphs.py
   python assignment_8_ml_classification.py
   ```

## 🏆 Project Outcomes

This repository demonstrates advanced proficiency in:
- **Data Science Methodologies** - End-to-end analysis pipelines
- **Algorithm Implementation** - From mathematical concepts to working code
- **Real-World Applications** - Audio processing, financial time series, NLP, computer vision
- **Performance Optimization** - Efficient data structures and processing techniques

---

## 📊 Future Enhancements

- [ ] Real-time audio processing dashboard
- [ ] Interactive time series forecasting models  
- [ ] Deep learning implementations for image reconstruction
- [ ] Graph neural network applications
- [ ] Deployment-ready ML model APIs

---
