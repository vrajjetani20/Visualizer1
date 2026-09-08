# 📊 Sales Data Analysis & Visualization

A **menu-driven Python project** for loading, exploring, cleaning, analyzing, and visualizing sales data using **Pandas, NumPy, Matplotlib, and Seaborn**.

This project works with CSV datasets and provides an easy-to-use command-line menu for common data-analysis tasks.

---

## ✨ Features

### 📥 1. Load Dataset
- Load sales data from a CSV file.
- Automatically convert the `Date` column to datetime.
- Convert numeric columns such as `Sales`, `Profit`, `Quantity`, and `Year`.
- Display the number of rows and columns after loading.

### 🔎 2. Explore Data
- Display the first 5 rows.
- Display the last 5 rows.
- Display column names.
- Display data types.
- Display basic DataFrame information.
- Display DataFrame shape.
- Display unique values from a selected column.

### 🧮 3. DataFrame Operations
Includes:
- Mathematical operations.
- NumPy array operations.
- Concatenating and merging CSV data.
- Splitting data by a selected column.
- Searching, sorting, and filtering.
- Aggregate functions.
- Pivot table creation.

### 🧹 4. Handle Missing Data
- Check missing values.
- Fill numeric missing values with the mean.
- Drop rows containing missing values.
- Replace missing values with a specific value.
- Convert data types.

### 📈 5. Descriptive Statistics
Generates:
- Count
- Mean
- Standard deviation
- Variance
- Minimum and maximum
- 25% quantile
- Median / 50% quantile
- 75% quantile

### 📊 6. Data Visualization
The project supports:
- Bar Plot
- Line Plot
- Scatter Plot
- Pie Chart
- Histogram
- Stack Plot
- Seaborn Correlation Heatmap
- Seaborn Box Plot
- Multiple subplots

### 💾 7. Save Visualization
The last generated chart can be saved as:
- `.png`
- `.jpg`
- `.jpeg`
- `.pdf`

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| 🐍 Python | Main programming language |
| 🐼 Pandas | Data loading and DataFrame analysis |
| 🔢 NumPy | Array operations and numerical processing |
| 📉 Matplotlib | Data visualization |
| 🌈 Seaborn | Heatmaps and box plots |
| 📄 CSV | Dataset input format |

---

## 📦 Installation

Make sure Python is installed, then install the required libraries:

```bash
pip install pandas numpy matplotlib seaborn
```

---

## ▶️ How to Run

1. Place `Visualizer.py` and `sales_data.csv` in the same project folder.
2. Open the folder in VS Code or a terminal.
3. Run:

```bash
python Visualizer.py
```

4. Select an option from the **MAIN MENU**.
5. When asked for the CSV path, enter:

```text
sales_data.csv
```

---

## 🗂️ Main Menu

```text
========== MAIN MENU ==========
1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
```

---

## 📸 Screenshots

### 1️⃣ Load Dataset

<img width="877" height="400" alt="1" src="https://github.com/user-attachments/assets/bed8207a-c294-4ce3-babf-774eded5fcaa" />


### 2️⃣ Explore Data

<img width="736" height="935" alt="2" src="https://github.com/user-attachments/assets/7e18e2a5-c39d-462d-8768-cf4fa04eb772" />


### 3️⃣ DataFrame Mathematical & Search Operations

<img width="880" height="912" alt="3" src="https://github.com/user-attachments/assets/2358fe28-bb8a-4e51-9883-b1f23faa8f80" />


### 4️⃣ Split Data

<img width="1431" height="837" alt="4" src="https://github.com/user-attachments/assets/ad6cc88b-9df4-45e8-8fa1-5509f22a45ee" />


### 5️⃣ Descriptive Statistics

<img width="1082" height="927" alt="5" src="https://github.com/user-attachments/assets/afe8fdcf-94a5-434d-8a3c-f5a1d114a2ba" />


### 6️⃣ Data Visualization

<img width="1795" height="582" alt="6" src="https://github.com/user-attachments/assets/6013aa40-08a4-4d41-9693-68863e8f6e6a" />


---


## 💡 Example Analysis

The program can calculate values such as:

```text
Total Sales
Average Sales
Maximum Sales
Minimum Sales
```

It can also create a new column for a **10% sales increase** and calculate a **Sales + Profit total**.

---

## 🎯 Learning Objectives

This project demonstrates practical use of:

- Python classes and methods
- Pandas DataFrames
- NumPy arrays
- CSV data handling
- Data cleaning
- Searching, sorting, and filtering
- GroupBy and aggregation
- Pivot tables
- Descriptive statistics
- Matplotlib visualization
- Seaborn visualization
- File saving
- Menu-driven programming

---

## 👨‍💻 Project File

**Main Python file:** `Visualizer.py`

The application is organized around the `SalesDataAnalyzer` class, with separate methods for loading, exploring, cleaning, statistical analysis, DataFrame operations, visualization, and saving charts.

---

## ⭐ Project Highlights

> 📌 A complete beginner-friendly **Sales Data Analysis & Visualization** project combining data handling, statistics, NumPy operations, and visualization in one interactive Python application.

---

## 📄 License

This project is created for **learning and educational purposes**.
