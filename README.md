# Automated Financial Reporting with Python & Excel

## Project Overview

This project demonstrates how to automate the generation of basic financial statements (specifically, an Income Statement) from raw transactional data stored in an Excel file using Python's powerful `pandas` library. This automation can significantly reduce manual effort in financial reporting processes.

## Features

* Reads transactional data from a specified Excel file (`transactions.xlsx`).
* Parses and categorizes financial transactions (revenues, various expenses).
* Calculates total revenues, total expenses, and net income.
* Generates a structured Income Statement.
* Outputs the complete Income Statement to a new Excel file (`income_statement_report.xlsx`).

## How It Works

The Python script (`generate_report.py`) utilizes the `pandas` library to perform data manipulation:
1.  It reads the input `transactions.xlsx` file into a DataFrame.
2.  It filters and groups transactions based on their 'Category' to identify revenues and different types of expenses.
3.  It sums up the amounts for each category to derive the key figures for the Income Statement.
4.  Finally, it constructs a new DataFrame representing the Income Statement and exports it to a new Excel file.

## Getting Started

### Prerequisites

* Python 3.x installed (ensure it's added to your PATH).
* `pip` (Python package installer) is typically included with Python.

### Installation

1.  **Clone this repository** (or download the ZIP file) to your local machine:
    ```bash
    git clone [https://github.com/YourGitHubUsername/Financial_Reporting_Project.git](https://github.com/YourGitHubUsername/Financial_Reporting_Project.git)
    cd Financial_Reporting_Project
    ```
    (If you're not using Git yet, you can just work directly in your local folder for now.)

2.  **Install the required Python libraries:**
    ```bash
    pip install pandas openpyxl
    ```

### Usage

1.  **Prepare your input data:**
    * Create an Excel file named `transactions.xlsx` in the same directory as `generate_report.py`.
    * Ensure it has the following columns (case-sensitive): `Date`, `Description`, `Category`, `Amount`.
    * Enter your financial transactions. **Revenues should be positive amounts, and Expenses should be negative amounts.**

    Example `transactions.xlsx` structure:
    | Date       | Description          | Category          | Amount |
    |------------|----------------------|-------------------|--------|
    | 2024-01-05 | Sale of Widgets      | Sales Revenue     | 1500   |
    | 2024-01-10 | Office Rent          | Rent Expense      | -800   |
    | ...        | ...                  | ...               | ...    |

2.  **Run the Python script:**
    Open your terminal or command prompt, navigate to the `Financial_Reporting_Project` directory, and run:
    ```bash
    python generate_report.py
    ```

3.  **View the output:**
    A new Excel file named `income_statement_report.xlsx` will be created in the same directory, containing your generated Income Statement.

## Future Enhancements (Ideas for your own development)

* **Balance Sheet & Cash Flow Statement:** Extend the script to generate other primary financial statements.
* **User Interface (GUI/CLI):** Develop a simple command-line interface (using `argparse`) or a graphical user interface (using `Tkinter` or `Streamlit`) for easier interaction.
* **Visualization:** Integrate `matplotlib` or `seaborn` to create charts (e.g., expense breakdown pie chart, revenue trends).
* **Database Integration:** Store transaction data in a simple SQLite database instead of Excel.
* **More Robust Error Handling:** Implement more specific checks for data integrity and file issues.
* **Dynamic Category Mapping:** Allow users to define how their transaction categories map to Income Statement line items.

## License

This project is open-source and available under the [MIT License](LICENSE) (You can add a LICENSE file later).

---
**Author:** Matthew Lubin