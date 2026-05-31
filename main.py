# Task 1: Iris Dataset Analysis
# Author: AI/ML Intern
# Date: 2026

# ========== 1. IMPORTS ==========
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.datasets import load_iris

# Set style for better visualizations
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# ========== 2. LOAD DATASET ==========
print("="*50)
print("TASK 1: IRIS DATASET EXPLORATION")
print("="*50)

# Load iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].map({0: 'setosa', 1: 'versicolor', 2: 'virginica'})

# ========== 3. DATA INSPECTION ==========
print("\n📊 DATASET SHAPE:", df.shape)
print("\n📋 COLUMN NAMES:")
print(df.columns.tolist())

print("\n🔍 FIRST 5 ROWS:")
print(df.head())

print("\nℹ️ DATA INFO:")
print(df.info())

print("\n📈 DESCRIPTIVE STATISTICS:")
print(df.describe())

print("\n🎯 SPECIES DISTRIBUTION:")
print(df['species_name'].value_counts())

# ========== 4. VISUALIZATIONS ==========

# Create figure with subplots
fig = plt.figure(figsize=(16, 12))

# 4.1 Scatter Plot Matrix (relationships between features)
ax1 = fig.add_subplot(2, 2, 1)
sns.scatterplot(data=df, x='sepal length (cm)', y='petal length (cm)', 
                hue='species_name', size='species_name', sizes=(50, 200), ax=ax1)
ax1.set_title('Sepal Length vs Petal Length', fontsize=12, fontweight='bold')
ax1.legend(loc='upper left')

# 4.2 Pairplot (all feature relationships)
ax2 = fig.add_subplot(2, 2, 2)
# Using seaborn pairplot - but for subplot, create separate figure
# Instead, let's create a correlation heatmap
corr_matrix = df[iris.feature_names].corr()
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', center=0, 
            square=True, ax=ax2, fmt='.2f')
ax2.set_title('Feature Correlation Matrix', fontsize=12, fontweight='bold')

# 4.3 Histograms (value distributions)
ax3 = fig.add_subplot(2, 2, 3)
df[iris.feature_names].hist(bins=20, ax=ax3, alpha=0.7)
ax3.set_title('Distribution of Features', fontsize=12, fontweight='bold')
plt.setp(ax3.get_xticklabels(), rotation=45)

# 4.4 Box Plots (outlier detection)
ax4 = fig.add_subplot(2, 2, 4)
df_melted = pd.melt(df, id_vars=['species_name'], 
                     value_vars=iris.feature_names,
                     var_name='Feature', value_name='Value')
sns.boxplot(data=df_melted, x='Feature', y='Value', hue='species_name', ax=ax4)
ax4.set_title('Box Plots by Species (Outlier Detection)', fontsize=12, fontweight='bold')
ax4.tick_params(axis='x', rotation=45)

plt.tight_layout()
plt.savefig('iris_analysis.png', dpi=150, bbox_inches='tight')
plt.show()

# ========== 5. ADDITIONAL INSIGHTS ==========
print("\n" + "="*50)
print("📊 KEY INSIGHTS")
print("="*50)

# Check for missing values
print(f"\n✅ Missing values: {df.isnull().sum().sum()}")

# Check for outliers using IQR
print("\n📌 OUTLIER DETECTION (IQR Method):")
for col in iris.feature_names:
    Q1 = df[col].quantile(0.25)
    Q3 = df[col].quantile(0.75)
    IQR = Q3 - Q1
    outliers = df[(df[col] < Q1 - 1.5*IQR) | (df[col] > Q3 + 1.5*IQR)]
    print(f"  {col}: {len(outliers)} outliers detected")

# Species analysis
print("\n🌸 SPECIES ANALYSIS:")
species_means = df.groupby('species_name')[iris.feature_names].mean()
print(species_means.round(2))

# Key observations
print("\n💡 OBSERVATIONS:")
print("1. Setosa has significantly smaller petal lengths/widths than other species")
print("2. Virginica has the largest sepal dimensions overall")
print("3. No missing values detected - dataset is clean")
print("4. Strong positive correlation between petal length and petal width")
print("5. Versicolor shows intermediate measurements between Setosa and Virginica")