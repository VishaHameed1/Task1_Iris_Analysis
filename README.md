
# 🌸 Task 1: Iris Dataset Exploration and Visualization

## 📋 Task Overview

**Objective**: Load, inspect, and visualize the Iris dataset to understand data trends, distributions, and relationships between flower species.

**Role**: AI/ML Engineering Intern  
**Company**: DevelopersHub Corporation  
**Due Date**: 5th June, 2026

---

## 📊 Dataset Information

### Iris Dataset (Fisher's Classic Dataset)

| Property | Details |
|----------|---------|
| **Source** | UCI Machine Learning Repository / Seaborn built-in |
| **Samples** | 150 flowers |
| **Features** | 4 numerical measurements |
| **Species** | 3 classes (Setosa, Versicolor, Virginica) |
| **Balance** | Perfectly balanced (50 samples each) |

### Feature Descriptions

| Feature | Description | Range (cm) |
|---------|-------------|------------|
| Sepal Length | Length of sepal | 4.3 - 7.9 |
| Sepal Width | Width of sepal | 2.0 - 4.4 |
| Petal Length | Length of petal | 1.0 - 6.9 |
| Petal Width | Width of petal | 0.1 - 2.5 |

### Target Classes

```
🌸 Setosa     - 50 samples (33.3%)
🌿 Versicolor - 50 samples (33.3%)
🌺 Virginica  - 50 samples (33.3%)
```

---

## 🔧 Tools & Technologies Used

```python
pandas==2.0.3      # Data loading and manipulation
numpy==1.24.3      # Numerical operations
matplotlib==3.7.1  # Base plotting
seaborn==0.12.2    # Advanced statistical visuals
scikit-learn==1.3.0 # Built-in dataset loading
```

---

## 📈 Visualizations Created

### 1. Scatter Plot: Sepal Length vs Petal Length
**Purpose**: Show relationship between two features across species

**Key Insights**:
- Setosa forms a distinct cluster (petal length < 2cm)
- Versicolor and Virginica show overlap but are separable
- Strong positive correlation visible

### 2. Correlation Heatmap
**Purpose**: Identify feature relationships

**Key Findings**:
```
Strongest Correlations:
- Petal length ↔ Petal width: 0.96
- Petal length ↔ Sepal length: 0.87
- Petal width ↔ Sepal length: 0.82

Weakest Correlation:
- Sepal width with all features (< 0.2)
```

### 3. Distribution Histograms
**Purpose**: Understand individual feature distributions

**Observations**:
- Sepal width: Near-normal distribution
- Petal features: Bimodal patterns (due to species differences)
- No extreme skewness in any feature

### 4. Box Plots by Species
**Purpose**: Compare distributions and detect outliers

**Findings**:
| Species | Outliers | Observations |
|---------|----------|--------------|
| Setosa | 0 | Tight, well-contained distribution |
| Versicolor | 1 | Minor outlier in sepal width |
| Virginica | 2 | Slight spread in sepal length |

---

## 📊 Analysis Results

### Descriptive Statistics (Overall)

| Feature | Mean | Std | Min | 25% | 50% | 75% | Max |
|---------|------|-----|-----|-----|-----|-----|-----|
| Sepal Length | 5.84 | 0.83 | 4.3 | 5.1 | 5.8 | 6.4 | 7.9 |
| Sepal Width | 3.05 | 0.43 | 2.0 | 2.8 | 3.0 | 3.3 | 4.4 |
| Petal Length | 3.76 | 1.76 | 1.0 | 1.6 | 4.3 | 5.1 | 6.9 |
| Petal Width | 1.20 | 0.76 | 0.1 | 0.3 | 1.3 | 1.8 | 2.5 |

### Species-wise Comparison

| Species | Sepal Length | Sepal Width | Petal Length | Petal Width |
|---------|--------------|-------------|--------------|--------------|
| **Setosa** | 5.01 cm | 3.43 cm | 1.46 cm | 0.25 cm |
| **Versicolor** | 5.94 cm | 2.77 cm | 4.26 cm | 1.33 cm |
| **Virginica** | 6.59 cm | 2.97 cm | 5.55 cm | 2.03 cm |

### Key Observations

**Species Separability**:
- ✅ Setosa is 100% separable using petal features alone
- ⚠️ Versicolor and Virginica have slight overlap (about 5-10%)
- 📍 Petal measurements > Sepal measurements for classification

**Data Quality**:
- ✅ No missing values detected
- ✅ Minimal outliers (only 3 total across 150 samples)
- ✅ Clean, well-documented dataset

---

## 💡 Learning Outcomes

### Skills Developed in This Task

| Skill Category | Specific Skills |
|----------------|-----------------|
| **Data Loading** | pandas read methods, built-in datasets |
| **Data Inspection** | .shape, .head(), .info(), .describe() |
| **Statistical Analysis** | Mean, median, quartiles, correlations |
| **Visualization** | Scatter plots, histograms, box plots, heatmaps |
| **Outlier Detection** | IQR method, box plot analysis |
| **Documentation** | Clear insights and observations |

### Key Takeaways

1. **Always start with EDA** - Visualize before modeling
2. **Multiple visualization types** tell different stories
3. **Correlation ≠ Causation** - Strong correlation doesn't imply cause
4. **Clean data** makes analysis easier and reliable
5. **Document findings** as you discover them

---

## 🚀 How to Run

### Installation

```bash
# Create virtual environment (optional)
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install requirements
pip install pandas numpy matplotlib seaborn scikit-learn
```

### Execution

```bash
# Navigate to task folder
cd Task1_Iris_Analysis

# Launch Jupyter Notebook
jupyter notebook task1_iris_analysis.ipynb

# Or run as Python script
python task1_iris_analysis.py
```

### Expected Output

1. **Console Output**:
   - Dataset shape and info
   - Statistical summaries
   - Missing value counts
   - Outlier detection results

2. **Generated Files**:
   - `iris_analysis.png` - Combined visualization (150 DPI)

---

## 📁 File Structure

```
Task1_Iris_Analysis/
│
├── task1_iris_analysis.ipynb   # Main Jupyter notebook
├── task1_iris_analysis.py       # Python script version
├── iris_analysis.png            # Output visualization
└── README.md                    # This file
```

---

## 🎯 Task Completion Checklist

- [x] Load dataset using pandas
- [x] Print shape, column names, and first rows
- [x] Use .info() and .describe() for statistics
- [x] Create scatter plot for feature relationships
- [x] Create histograms for value distributions
- [x] Create box plots for outlier detection
- [x] Use matplotlib AND seaborn for plotting
- [x] Document all findings and insights

---

## 🔄 Future Improvements

### Short-term Enhancements
- [ ] Add pairplot for all feature combinations
- [ ] Implement violin plots for density visualization
- [ ] Add statistical hypothesis testing (ANOVA between species)

### Long-term Enhancements
- [ ] Build classification models on this dataset
- [ ] Create interactive Plotly visualizations
- [ ] Deploy as a Streamlit dashboard
- [ ] Add PCA for dimensionality reduction visualization

---

## 📚 References

1. Fisher, R.A. (1936). "The use of multiple measurements in taxonomic problems"  
   *Annals of Eugenics*, 7(2): 179-188

2. UCI Machine Learning Repository - Iris Data Set  
   https://archive.ics.uci.edu/ml/datasets/iris

3. Seaborn Documentation  
   https://seaborn.pydata.org/

---

## 👤 Author

**Name**: [Visha Hameed]  
**Position**: AI/ML Engineering Intern  
**Company**: DevelopersHub Corporation  
**Date**: June 2026  
**Email**: [vishahameed111@gmail.com]

---

## 📝 License

This project is submitted as part of internship requirements.  
All rights reserved to DevelopersHub Corporation.

---

## ⭐ Key Results Summary

```
✅ Dataset Loaded: 150 rows, 5 columns (4 features + 1 target)
✅ Missing Values: 0
✅ Outliers Detected: 3 total
✅ Visualizations Created: 4
✅ Key Insight: Petal features perfectly separate Setosa species
✅ Data Quality: Excellent - ready for modeling
```

---

