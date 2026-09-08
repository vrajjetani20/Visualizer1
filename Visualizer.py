import pandas as pd
import seaborn as sns
import numpy as np
import os
import matplotlib.pyplot as plt


class SalesDataAnalyzer:

    def __init__(self, file_path=None):
        self.data = pd.DataFrame()
        self.last_figure = None

        if file_path:
            self.load_data(file_path)

    def __del__(self):
        pass

    # ---------------------------------------------------------
    # 1. LOAD DATA
    # ---------------------------------------------------------
    def load_data(self, file_path):
        try:
            self.data = pd.read_csv(file_path)

            if "Date" in self.data.columns:
                self.data["Date"] = pd.to_datetime(
                    self.data["Date"], errors="coerce"
                )

            numeric_columns = ["Sales", "Profit", "Quantity", "Year"]

            for column in numeric_columns:
                if column in self.data.columns:
                    self.data[column] = pd.to_numeric(
                        self.data[column], errors="coerce"
                    )

            print("\nDataset loaded successfully!")
            print("Rows:", len(self.data))
            print("Columns:", len(self.data.columns))

        except FileNotFoundError:
            print("\nFile not found. Please check the CSV file path.")
        except Exception as e:
            print("\nError while loading data:", e)

    # ---------------------------------------------------------
    # 2. EXPLORE DATA
    # ---------------------------------------------------------
    def explore_data(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:
            print("\n========== EXPLORE DATA ==========")
            print("1. Display first 5 rows")
            print("2. Display last 5 rows")
            print("3. Display column names")
            print("4. Display data types")
            print("5. Display basic information")
            print("6. Display shape")
            print("7. Display unique values")
            print("8. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                print("\n", self.data.head())

            elif choice == "2":
                print("\n", self.data.tail())

            elif choice == "3":
                print("\nColumn Names:")
                print(list(self.data.columns))

            elif choice == "4":
                print("\nData Types:")
                print(self.data.dtypes)

            elif choice == "5":
                print("\nBasic Information:")
                self.data.info()

            elif choice == "6":
                print("\nShape (Rows, Columns):", self.data.shape)

            elif choice == "7":
                column = input("Enter column name: ")

                if column in self.data.columns:
                    print("\nUnique values:")
                    print(self.data[column].unique())
                else:
                    print("Column not found.")

            elif choice == "8":
                break

            else:
                print("Invalid choice.")

    # ---------------------------------------------------------
    # 3. CLEAN DATA / MISSING VALUES
    # ---------------------------------------------------------
    def clean_data(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:
            print("\n========== HANDLE MISSING DATA ==========")
            print("1. Display missing values")
            print("2. Fill numeric missing values with mean")
            print("3. Drop rows with missing values")
            print("4. Replace missing values with a specific value")
            print("5. Convert data types")
            print("6. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                missing = self.data.isnull().sum()

                if missing.sum() == 0:
                    print("\nNo missing values found!")
                else:
                    print("\nMissing values:")
                    print(missing)

            elif choice == "2":
                numeric_columns = self.data.select_dtypes(
                    include=np.number
                ).columns

                for column in numeric_columns:
                    self.data[column] = self.data[column].fillna(
                        self.data[column].mean()
                    )

                print("\nNumeric missing values filled with mean.")

            elif choice == "3":
                old_rows = len(self.data)
                self.data = self.data.dropna()
                new_rows = len(self.data)

                print(
                    f"\nDeleted {old_rows - new_rows} rows with missing values."
                )

            elif choice == "4":
                value = input("Enter value to replace missing values: ")

                try:
                    value = float(value)
                except ValueError:
                    pass

                self.data = self.data.fillna(value)
                print("\nMissing values replaced successfully.")

            elif choice == "5":
                if "Date" in self.data.columns:
                    self.data["Date"] = pd.to_datetime(
                        self.data["Date"], errors="coerce"
                    )

                for column in ["Sales", "Profit", "Quantity", "Year"]:
                    if column in self.data.columns:
                        self.data[column] = pd.to_numeric(
                            self.data[column], errors="coerce"
                        )

                print("\nData type conversion completed.")

            elif choice == "6":
                break

            else:
                print("Invalid choice.")

    # ---------------------------------------------------------
    # 4. NUMPY ARRAY OPERATIONS
    # ---------------------------------------------------------
    def numpy_operations(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        if "Sales" not in self.data.columns:
            print("\nSales column is required for NumPy operations.")
            return

        sales_array = self.data["Sales"].dropna().to_numpy()

        if len(sales_array) == 0:
            print("\nNo Sales values available.")
            return

        print("\n========== NUMPY OPERATIONS ==========")

        print("\nSales NumPy Array:")
        print(sales_array)

        print("\n1. Indexing")
        print("First value:", sales_array[0])

        if len(sales_array) > 1:
            print("Second value:", sales_array[1])

        print("\n2. Slicing")
        print("First 3 values:", sales_array[:3])
        print("Last 3 values:", sales_array[-3:])

        print("\n3. Element-wise Mathematical Operations")
        print("Sales + 100:")
        print(sales_array + 100)

        print("\nSales - 50:")
        print(sales_array - 50)

        print("\nSales * 2:")
        print(sales_array * 2)

        print("\nSales / 2:")
        print(sales_array / 2)

        print("\n4. Search")
        search_value = float(input("Enter Sales value to search: "))

        positions = np.where(sales_array == search_value)[0]

        if len(positions) > 0:
            print("Value found at index:", positions)
        else:
            print("Value not found.")

        print("\n5. Split Array")
        number_of_parts = int(input("Enter number of parts: "))

        if 1 <= number_of_parts <= len(sales_array):
            parts = np.array_split(sales_array, number_of_parts)

            for i, part in enumerate(parts, start=1):
                print(f"Part {i}:", part)
        else:
            print("Number of parts must be between 1 and array length.")

        print("\n6. Combine Array")
        extra_array = np.array([1000, 2000])
        combined = np.concatenate((sales_array, extra_array))
        print("Extra Array:", extra_array)
        print("Combined Array:", combined)

    # ---------------------------------------------------------
    # 5. DATAFRAME MATHEMATICAL OPERATIONS
    # ---------------------------------------------------------
    def mathematical_operations(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        print("\n========== MATHEMATICAL OPERATIONS ==========")

        if "Sales" in self.data.columns:
            self.data["Sales_After_10_Percent_Increase"] = (
                self.data["Sales"] * 1.10
            )
            print("\nSales after 10% increase:")
            print(
                self.data[
                    ["Sales", "Sales_After_10_Percent_Increase"]
                ].head()
            )

        if "Sales" in self.data.columns and "Profit" in self.data.columns:
            self.data["Sales_Profit_Total"] = (
                self.data["Sales"] + self.data["Profit"]
            )
            print("\nSales + Profit:")
            print(self.data[["Sales", "Profit", "Sales_Profit_Total"]].head())

        if "Sales" in self.data.columns:
            print("\nTotal Sales:", self.data["Sales"].sum())
            print("Average Sales:", self.data["Sales"].mean())
            print("Maximum Sales:", self.data["Sales"].max())
            print("Minimum Sales:", self.data["Sales"].min())

    # ---------------------------------------------------------
    # 6. COMBINE DATA
    # ---------------------------------------------------------
    def combine_data(self):
        if self.data.empty:
            print("\nPlease load the main dataset first.")
            return

        print("\n========== COMBINE DATA ==========")
        print("1. Concatenate another CSV")
        print("2. Merge with another CSV")
        print("3. Back")

        choice = input("Enter your choice: ")

        if choice == "3":
            return

        file_path = input("Enter second CSV file path: ")

        try:
            other_data = pd.read_csv(file_path)

            if choice == "1":
                self.data = pd.concat(
                    [self.data, other_data],
                    ignore_index=True
                )
                print("\nDataFrames combined using concat().")

            elif choice == "2":
                column = input("Enter common column for merge: ")

                if column in self.data.columns and column in other_data.columns:
                    self.data = pd.merge(
                        self.data,
                        other_data,
                        on=column,
                        how="inner"
                    )
                    print("\nDataFrames combined using merge().")
                else:
                    print("Common column not found.")

            else:
                print("Invalid choice.")
                return

            print("\nUpdated data:")
            print(self.data.head())

        except FileNotFoundError:
            print("Second CSV file not found.")
        except Exception as e:
            print("Error:", e)

    # ---------------------------------------------------------
    # 7. SPLIT DATA
    # ---------------------------------------------------------
    def split_data(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        print("\n========== SPLIT DATA ==========")

        print("Available columns:")
        print(list(self.data.columns))

        column = input("Enter column to split by: ")

        if column not in self.data.columns:
            print("Column not found.")
            return

        values = self.data[column].dropna().unique()

        if len(values) == 0:
            print("No values available.")
            return

        print("\nAvailable values:")
        for value in values:
            print("-", value)

        selected_value = input("Enter value: ")

        matching_value = None

        for value in values:
            if str(value).lower() == selected_value.lower():
                matching_value = value
                break

        if matching_value is None:
            print("Value not found.")
            return

        split_data = self.data[
            self.data[column] == matching_value
        ].copy()

        print(f"\nData for {matching_value}:")
        print(split_data)

        save_choice = input("Save this split data? (y/n): ").lower()

        if save_choice == "y":
            file_name = input("Enter file name (example: north_data.csv): ")

            if not file_name.lower().endswith(".csv"):
                file_name += ".csv"

            split_data.to_csv(file_name, index=False)
            print(f"Data saved as {file_name}")

    # ---------------------------------------------------------
    # 8. SEARCH, SORT AND FILTER
    # ---------------------------------------------------------
    def search_sort_filter(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:
            print("\n========== SEARCH / SORT / FILTER ==========")
            print("1. Search")
            print("2. Sort")
            print("3. Filter")
            print("4. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                column = input("Enter column name: ")
                value = input("Enter value to search: ")

                if column not in self.data.columns:
                    print("Column not found.")
                    continue

                result = self.data[
                    self.data[column].astype(str).str.contains(
                        value,
                        case=False,
                        na=False
                    )
                ]

                print("\nSearch Result:")
                print(result)

            elif choice == "2":
                column = input("Enter column name to sort: ")

                if column not in self.data.columns:
                    print("Column not found.")
                    continue

                order = input("Ascending? (y/n): ").lower()
                ascending = order == "y"

                result = self.data.sort_values(
                    by=column,
                    ascending=ascending
                )

                print("\nSorted Data:")
                print(result.head(10))

            elif choice == "3":
                column = input("Enter column name: ")
                value = input("Enter value to filter: ")

                if column not in self.data.columns:
                    print("Column not found.")
                    continue

                result = self.data[
                    self.data[column].astype(str).str.lower()
                    == value.lower()
                ]

                print("\nFiltered Data:")
                print(result)

            elif choice == "4":
                break

            else:
                print("Invalid choice.")

    # ---------------------------------------------------------
    # 9. AGGREGATE FUNCTIONS
    # ---------------------------------------------------------
    def aggregate_functions(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        print("\n========== AGGREGATE FUNCTIONS ==========")

        numeric_columns = self.data.select_dtypes(
            include=np.number
        ).columns

        print("\nNumeric Columns:")
        print(list(numeric_columns))

        if len(numeric_columns) == 0:
            print("No numeric columns found.")
            return

        column = input("Enter numeric column: ")

        if column not in numeric_columns:
            print("Please enter a valid numeric column.")
            return

        print("\nSum:", self.data[column].sum())
        print("Mean:", self.data[column].mean())
        print("Count:", self.data[column].count())
        print("Minimum:", self.data[column].min())
        print("Maximum:", self.data[column].max())

        if "Region" in self.data.columns:
            print("\nSales/Selected column by Region:")
            print(
                self.data.groupby("Region")[column]
                .agg(["sum", "mean", "count"])
            )

    # ---------------------------------------------------------
    # 10. STATISTICAL ANALYSIS
    # ---------------------------------------------------------
    def statistical_analysis(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        print("\n========== STATISTICAL ANALYSIS ==========")

        numeric_data = self.data.select_dtypes(include=np.number)

        if numeric_data.empty:
            print("No numeric columns available.")
            return

        print("\nDescriptive Statistics:")
        print(numeric_data.describe())

        print("\nStandard Deviation:")
        print(numeric_data.std())

        print("\nVariance:")
        print(numeric_data.var())

        print("\n25% Quantile:")
        print(numeric_data.quantile(0.25))

        print("\n50% Quantile / Median:")
        print(numeric_data.quantile(0.50))

        print("\n75% Quantile:")
        print(numeric_data.quantile(0.75))

    # ---------------------------------------------------------
    # 11. PIVOT TABLE
    # ---------------------------------------------------------
    def create_pivot_table(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        if "Region" not in self.data.columns or "Sales" not in self.data.columns:
            print("\nRegion and Sales columns are required.")
            return

        index_column = "Region"

        if "Product" in self.data.columns:
            pivot = pd.pivot_table(
                self.data,
                index="Region",
                columns="Product",
                values="Sales",
                aggfunc="sum",
                fill_value=0
            )
        else:
            pivot = pd.pivot_table(
                self.data,
                index="Region",
                values="Sales",
                aggfunc="sum"
            )

        print("\n========== PIVOT TABLE ==========")
        print(pivot)

    # ---------------------------------------------------------
    # 12. VISUALIZATION
    # ---------------------------------------------------------
    def visualize_data(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:
            print("\n========== DATA VISUALIZATION ==========")
            print("1. Bar Plot")
            print("2. Line Plot")
            print("3. Scatter Plot")
            print("4. Pie Chart")
            print("5. Histogram")
            print("6. Stack Plot")
            print("7. Seaborn Heatmap")
            print("8. Seaborn Box Plot")
            print("9. Subplots")
            print("10. Back")

            choice = input("Enter your choice: ")

            try:
                if choice == "1":
                    if "Product" not in self.data.columns or "Sales" not in self.data.columns:
                        print("Product and Sales columns are required.")
                        continue

                    grouped = self.data.groupby("Product")["Sales"].sum()

                    fig, ax = plt.subplots(figsize=(8, 5))
                    grouped.plot(kind="bar", ax=ax)

                    ax.set_title("Total Sales by Product")
                    ax.set_xlabel("Product")
                    ax.set_ylabel("Sales")
                    plt.xticks(rotation=45)
                    plt.tight_layout()

                    self.last_figure = fig
                    plt.show()
                    
                elif choice == "2":
                    if "Year" not in self.data.columns or "Sales" not in self.data.columns:
                        print("Year and Sales columns are required.")
                        continue

                    grouped = self.data.groupby("Year")["Sales"].sum()

                    fig, ax = plt.subplots(figsize=(8, 5))
                    ax.plot(
                        grouped.index,
                        grouped.values,
                        marker="o",
                        label="Sales"
                    )

                    ax.set_title("Sales Trend by Year")
                    ax.set_xlabel("Year")
                    ax.set_ylabel("Sales")
                    ax.legend()
                    ax.grid(True)

                    plt.tight_layout()

                    self.last_figure = fig
                    plt.show()

                elif choice == "3":
                    x_column = input("Enter X-axis column: ")
                    y_column = input("Enter Y-axis column: ")

                    if x_column not in self.data.columns or y_column not in self.data.columns:
                        print("Column not found.")
                        continue

                    fig, ax = plt.subplots(figsize=(8, 5))
                    ax.scatter(
                        self.data[x_column],
                        self.data[y_column]
                    )

                    ax.set_title(f"{x_column} vs {y_column}")
                    ax.set_xlabel(x_column)
                    ax.set_ylabel(y_column)

                    plt.tight_layout()

                    self.last_figure = fig
                    plt.show()

                elif choice == "4":
                    if "Region" not in self.data.columns or "Sales" not in self.data.columns:
                        print("Region and Sales columns are required.")
                        continue

                    grouped = self.data.groupby("Region")["Sales"].sum()

                    fig, ax = plt.subplots(figsize=(7, 7))
                    ax.pie(
                        grouped.values,
                        labels=grouped.index,
                        autopct="%1.1f%%"
                    )

                    ax.set_title("Sales by Region")

                    self.last_figure = fig
                    plt.show()

                elif choice == "5":
                    if "Sales" not in self.data.columns:
                        print("Sales column is required.")
                        continue

                    fig, ax = plt.subplots(figsize=(8, 5))
                    ax.hist(
                        self.data["Sales"].dropna(),
                        bins=5,
                        edgecolor="black"
                    )

                    ax.set_title("Sales Distribution")
                    ax.set_xlabel("Sales")
                    ax.set_ylabel("Frequency")

                    plt.tight_layout()

                    self.last_figure = fig
                    plt.show()

                elif choice == "6":
                    if (
                        "Year" not in self.data.columns
                        or "Region" not in self.data.columns
                        or "Sales" not in self.data.columns
                    ):
                        print("Year, Region and Sales columns are required.")
                        continue

                    pivot = self.data.pivot_table(
                        index="Year",
                        columns="Region",
                        values="Sales",
                        aggfunc="sum",
                        fill_value=0
                    )

                    fig, ax = plt.subplots(figsize=(9, 5))

                    ax.stackplot(
                        pivot.index,
                        *[
                            pivot[region].values
                            for region in pivot.columns
                        ],
                        labels=pivot.columns
                    )

                    ax.set_title("Sales by Region and Year")
                    ax.set_xlabel("Year")
                    ax.set_ylabel("Sales")
                    ax.legend(loc="upper left")

                    plt.tight_layout()

                    self.last_figure = fig
                    plt.show()

                elif choice == "7":
                    numeric_data = self.data.select_dtypes(
                        include=np.number
                    )

                    if numeric_data.shape[1] < 2:
                        print("At least two numeric columns are required.")
                        continue

                    fig, ax = plt.subplots(figsize=(8, 6))

                    sns.heatmap(
                        numeric_data.corr(),
                        annot=True,
                        ax=ax
                    )

                    ax.set_title("Correlation Heatmap")

                    plt.tight_layout()

                    self.last_figure = fig
                    plt.show()

                elif choice == "8":
                    if "Region" not in self.data.columns or "Sales" not in self.data.columns:
                        print("Region and Sales columns are required.")
                        continue

                    fig, ax = plt.subplots(figsize=(8, 5))

                    sns.boxplot(
                        data=self.data,
                        x="Region",
                        y="Sales",
                        ax=ax
                    )

                    ax.set_title("Sales Distribution by Region")

                    plt.xticks(rotation=45)
                    plt.tight_layout()

                    self.last_figure = fig
                    plt.show()

                elif choice == "9":
                    if (
                        "Product" not in self.data.columns
                        or "Sales" not in self.data.columns
                    ):
                        print("Product and Sales columns are required.")
                        continue

                    product_sales = self.data.groupby(
                        "Product"
                    )["Sales"].sum()

                    fig, axes = plt.subplots(2, 2, figsize=(12, 8))

                    axes[0, 0].bar(
                        product_sales.index,
                        product_sales.values
                    )
                    axes[0, 0].set_title("Bar Plot")
                    axes[0, 0].tick_params(axis="x", rotation=45)
                    
                    if "Year" in self.data.columns:
                        year_sales = self.data.groupby(
                            "Year"
                        )["Sales"].sum()

                        axes[0, 1].plot(
                            year_sales.index,
                            year_sales.values,
                            marker="o"
                        )
                        axes[0, 1].set_title("Line Plot")

                    axes[1, 0].hist(
                        self.data["Sales"].dropna(),
                        bins=5,
                        edgecolor="black"
                    )
                    axes[1, 0].set_title("Histogram")

                    if "Region" in self.data.columns:
                        region_sales = self.data.groupby(
                            "Region"
                        )["Sales"].sum()

                        axes[1, 1].pie(
                            region_sales.values,
                            labels=region_sales.index,
                            autopct="%1.1f%%"
                        )
                        axes[1, 1].set_title("Pie Chart")

                    fig.suptitle("Sales Data Visualization")
                    plt.tight_layout()

                    self.last_figure = fig
                    plt.show()

                elif choice == "10":
                    break

                else:
                    print("Invalid choice.")

            except Exception as e:
                print("Visualization error:", e)

    # ---------------------------------------------------------
    # 13. SAVE VISUALIZATION
    # ---------------------------------------------------------
    def save_visualization(self):
        if self.last_figure is None:
            print("\nFirst create a visualization from option 6.")
            return

        print("\n========== SAVE VISUALIZATION ==========")

        file_name = input(
            "Enter file name (example: sales_chart.png): "
        )

        if not file_name.lower().endswith(
            (".png", ".jpg", ".jpeg", ".pdf")
        ):
            file_name += ".png"

        try:
            self.last_figure.savefig(
                file_name,
                dpi=300,
                bbox_inches="tight"
            )

            print(f"\nVisualization saved successfully as {file_name}")

        except Exception as e:
            print("Error while saving:", e)

    # ---------------------------------------------------------
    # 14. DATAFRAME OPERATIONS MENU
    # ---------------------------------------------------------
    def dataframe_operations(self):
        if self.data.empty:
            print("\nPlease load a dataset first.")
            return

        while True:
            print("\n========== DATAFRAME OPERATIONS ==========")
            print("1. Mathematical Operations")
            print("2. NumPy Array Operations")
            print("3. Combine Data")
            print("4. Split Data")
            print("5. Search / Sort / Filter")
            print("6. Aggregate Functions")
            print("7. Create Pivot Table")
            print("8. Back")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.mathematical_operations()

            elif choice == "2":
                self.numpy_operations()

            elif choice == "3":
                self.combine_data()

            elif choice == "4":
                self.split_data()

            elif choice == "5":
                self.search_sort_filter()

            elif choice == "6":
                self.aggregate_functions()

            elif choice == "7":
                self.create_pivot_table()

            elif choice == "8":
                break

            else:
                print("Invalid choice.")


def main():
    print("        SALES DATA ANALYSIS & VISUALIZATION")

    analyzer = SalesDataAnalyzer()

    while True:
        print("\n========== MAIN MENU ==========")
        print("1. Load Dataset")
        print("2. Explore Data")
        print("3. Perform DataFrame Operations")
        print("4. Handle Missing Data")
        print("5. Generate Descriptive Statistics")
        print("6. Data Visualization")
        print("7. Save Visualization")
        print("8. Exit")
        print("=" * 32)

        choice = input("Enter your choice: ")

        if choice == "1":
            file_path = input(
                "Enter CSV file path (example: sales_data.csv): "
            )
            analyzer.load_data(file_path)

        elif choice == "2":
            analyzer.explore_data()

        elif choice == "3":
            analyzer.dataframe_operations()

        elif choice == "4":
            analyzer.clean_data()

        elif choice == "5":
            analyzer.statistical_analysis()

        elif choice == "6":
            analyzer.visualize_data()

        elif choice == "7":
            analyzer.save_visualization()

        elif choice == "8":
            print("\nExiting the program. Goodbye!")
            break

        else:
            print("\nInvalid choice. Please enter 1 to 8.")

if __name__ == "__main__":
    main()
