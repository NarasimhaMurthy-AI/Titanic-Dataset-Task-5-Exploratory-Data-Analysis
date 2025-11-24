import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

# ------------ 1. Load Data ----------------
file_path = r"D:\DataAnalyst internship\Titanic-Dataset.xlsx"
report_path = r"D:\DataAnalyst internship\eda_report_task5.pdf"

df = pd.read_excel(file_path)

# ------------ START PDF -------------------
pdf = PdfPages(report_path)

# ------------ 2. Basic Info ----------------
fig = plt.figure(figsize=(10, 5))
plt.title("Dataset Info")
plt.text(0.1, 0.9, str(df.info()), fontsize=10)
pdf.savefig(fig)
plt.close()

fig = plt.figure(figsize=(10, 7))
plt.title("Describe Statistics")
plt.text(0.01, 0.99, df.describe(include='all').to_string(), fontsize=9, va="top")
pdf.savefig(fig)
plt.close()

fig = plt.figure(figsize=(10, 6))
plt.title("Missing Values")
plt.text(0.01, 0.99, df.isnull().sum().to_string(), fontsize=10, va="top")
pdf.savefig(fig)
plt.close()

# ------------ 4. Histograms ----------------
fig = plt.figure(figsize=(12, 8))
df.hist(ax=fig.gca())
plt.suptitle("Histograms of Numerical Columns")
pdf.savefig(fig)
plt.close()

# ------------ 5. Boxplots -------------------
fig = plt.figure(figsize=(10, 5))
sns.boxplot(data=df.select_dtypes(include=np.number))
plt.title("Boxplot - Numerical Columns")
pdf.savefig(fig)
plt.close()

# ------------ 6. Scatterplots ---------------
if 'Age' in df.columns and 'Fare' in df.columns:
    fig = plt.figure(figsize=(6,4))
    sns.scatterplot(data=df, x='Age', y='Fare', hue='Survived')
    plt.title("Scatterplot: Age vs Fare")
    pdf.savefig(fig)
    plt.close()

# ------------ 7. Pairplot -------------------
fig = sns.pairplot(df.select_dtypes(include=np.number))
fig.fig.suptitle("Pairplot - Numerical Columns", y=1.02)
pdf.savefig(fig.fig)
plt.close()

# ------------ 8. Heatmap -------------------
fig = plt.figure(figsize=(10, 6))
sns.heatmap(df.select_dtypes(include=np.number).corr(), annot=True, fmt=".2f", cmap="Blues")
plt.title("Correlation Heatmap")
pdf.savefig(fig)
plt.close()

# ------------ 9. Observations Summary -------
summary = []

if 'Survived' in df.columns:
    summary.append(f"Overall Survival Rate: {df['Survived'].mean():.2f}")

miss = df.isnull().sum()
summary.append("\nMissing Values:")
summary.append(miss[miss > 0].to_string())

if 'Age' in df.columns:
    summary.append(f"\nMedian Age: {df['Age'].median():.2f}")

if 'Fare' in df.columns:
    summary.append(f"Median Fare: {df['Fare'].median():.2f}")

summary.append("\nTrend: Females and higher-class passengers have higher survival probabilities.")

fig = plt.figure(figsize=(10, 6))
plt.title("Summary of Key Observations")
plt.text(0.01, 0.99, "\n".join(summary), va="top", fontsize=10)
pdf.savefig(fig)
plt.close()

# ------------ END PDF -------------------
pdf.close()

print("PDF generated successfully at:", report_path)
