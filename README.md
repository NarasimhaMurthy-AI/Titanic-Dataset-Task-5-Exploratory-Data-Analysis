# 🚢 Titanic Dataset – Task 5 Exploratory Data Analysis (EDA)

This repository contains the complete Exploratory Data Analysis (Task 5) performed on the **Titanic Dataset** as part of my Data Analyst Internship practice.  
The project covers statistical exploration, data understanding, visualization, and key insights following the Task-5 instructions.

---

## 📂 Project Structure


---

## 🎯 Project Objective

The objective of **Task 5** is to:
- Load and inspect the Titanic dataset  
- Generate descriptive statistics  
- Handle missing values  
- Visualize dataset using multiple chart types  
- Identify relationships and trends  
- Produce an EDA PDF report  
- Summarize key findings & insights  

This follows the exact requirements from **Task 5 instructions**.

---

## 🧠 Steps Performed in EDA

### 1️⃣ Data Loading
- Loaded `Titanic-Dataset.xlsx` using Pandas
- Inspected shape, columns, and data types

### 2️⃣ Data Summary
- `df.info()`
- `df.describe(include='all')`
- Missing values count

### 3️⃣ Value Counts
- Survived distribution
- Gender distribution
- Passenger Class distribution

### 4️⃣ Visual Explorations
Generated visualizations using `matplotlib` and `seaborn`:

#### 📊 Histograms
- Numerical column distributions  
- Age, Fare, SibSp, Parch

#### 📦 Boxplots
- To identify outliers in numerical features

#### 🔵 Scatter Plots
- Age vs Fare  
- Colored by survival

#### 🔁 Pairplot
- Relationship between all numeric variables  
- Patterns and correlations

#### 🔥 Correlation Heatmap
- Checking linear relationships between:
  - Age  
  - Fare  
  - SibSp  
  - Parch  
  - Survived  

---

## 📝 Key Insights

### ✔ Survival Rate  
- Overall survival rate = **~38%**

### ✔ Gender Effect  
- **Females had a significantly higher survival rate** than males.

### ✔ Class Effect  
- Passengers in **1st Class** survived more compared to 2nd and 3rd class.

### ✔ Age Trends  
- Majority of passengers were 20–40 years old.

### ✔ Fare Distribution  
- Fare distribution is right-skewed (few high outliers).

### ✔ Missing Values  
- Age has missing values  
- Cabin has many missing values (+70%)  
- Embarked has only 2 missing values  

### ✔ Correlations  
- Survival is **positively correlated** with Passenger Class (higher class → more survival).
- Fare and Pclass show strong relationship.

---

## 📄 PDF Report

A full **multi-page EDA PDF report** was auto-generated using:

```python
from matplotlib.backends.backend_pdf import PdfPages
