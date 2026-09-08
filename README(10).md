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

![Load Dataset](screenshots/screen1.png)

### 2️⃣ Explore Data

![Explore Data](screenshots/screen2.png)

### 3️⃣ DataFrame Mathematical & Search Operations

![DataFrame Operations](screenshots/screen3.png)

### 4️⃣ Split Data

![Split Data](screenshots/screen4.png)

### 5️⃣ Descriptive Statistics

![Descriptive Statistics](screenshots/screen5.png)

### 6️⃣ Data Visualization

![Data Visualization](screenshots/screen6.png)

---

## 📁 Suggested Project Structure

```text
Sales-Data-Analysis/
│
├── Visualizer.py
├── sales_data.csv
├── README.md
│
└── screenshots/
    ├── screen1.png
    ├── screen2.png
    ├── screen3.png
    ├── screen4.png
    ├── screen5.png
    └── screen6.png
```

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
