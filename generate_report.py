import pandas as pd
import os # Import the os module to check for file existence

def generate_income_statement(input_file_path='transactions.xlsx', output_file_name='income_statement_report.xlsx'):
    """
    Generates a simple Income Statement from transactional data.

    Args:
        input_file_path (str): Path to the Excel file containing transactional data.
        output_file_name (str): Name of the Excel file to save the income statement.
    """
    print(f"--- Starting Financial Report Generation ---")
    print(f"Attempting to read data from: {input_file_path}")

    # Check if the input file exists
    if not os.path.exists(input_file_path):
        print(f"Error: The input file '{input_file_path}' was not found. Please ensure it's in the same directory as the script or provide the full path.")
        return

    try:
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(input_file_path)
        print("Data loaded successfully.")
        print("\nFirst 5 rows of raw transaction data:")
        print(df.head())
        print("-" * 50)

    except Exception as e:
        print(f"An error occurred while reading the Excel file: {e}")
        print("Please ensure the Excel file is closed and has the correct format/headers.")
        return

    # --- Data Cleaning/Preparation ---
    # Ensure 'Amount' column is numeric. 'coerce' will turn non-numeric into NaN.
    df['Amount'] = pd.to_numeric(df['Amount'], errors='coerce')
    # Drop rows where 'Amount' couldn't be converted (e.g., empty or text in Amount column)
    df.dropna(subset=['Amount'], inplace=True)

    # Ensure 'Category' column is string type for string operations
    df['Category'] = df['Category'].astype(str)

    # --- Calculate Income Statement Components ---

    # Revenues: Look for categories containing 'Revenue' (case-insensitive)
    revenue_df = df[df['Category'].str.contains('revenue', case=False, na=False)]
    total_revenue = revenue_df['Amount'].sum()

    # Expenses: Look for categories containing 'Expense', 'Cost', or 'Supplies' (case-insensitive)
    # Assuming expenses are recorded as negative amounts in the source data
    expense_df = df[df['Category'].str.contains('expense|cost|supplies', case=False, na=False)]
    total_expenses_negative = expense_df['Amount'].sum() # This sum will be negative

    # Group expenses by category for detailed breakdown, display as positive
    expenses_by_category = expense_df.groupby('Category')['Amount'].sum().abs().sort_values(ascending=False)

    # Calculate Net Income (Revenue + Negative Expenses = Revenue - Positive Expenses)
    net_income = total_revenue + total_expenses_negative

    # --- Create the Income Statement DataFrame for Output ---
    income_statement_data = []

    # Revenues Section
    income_statement_data.append({'Line Item': 'Revenues:', 'Amount': ''})
    income_statement_data.append({'Line Item': '  Sales Revenue', 'Amount': total_revenue})
    # You could add other specific revenue lines here if your categories vary

    # Spacer
    income_statement_data.append({'Line Item': '', 'Amount': ''})

    # Expenses Section
    income_statement_data.append({'Line Item': 'Expenses:', 'Amount': ''})
    for category, amount in expenses_by_category.items():
        income_statement_data.append({'Line Item': f'  {category}', 'Amount': amount})

    # Spacer
    income_statement_data.append({'Line Item': '', 'Amount': ''})

    # Total Expenses
    income_statement_data.append({'Line Item': 'Total Expenses', 'Amount': total_expenses_negative * -1}) # Display as positive

    # Spacer
    income_statement_data.append({'Line Item': '', 'Amount': ''})

    # Net Income
    income_statement_data.append({'Line Item': 'NET INCOME (LOSS)', 'Amount': net_income})

    # Convert list of dictionaries to DataFrame
    income_statement_df = pd.DataFrame(income_statement_data)

    print("\n--- Generated Income Statement Preview ---")
    print(income_statement_df.to_string(index=False)) # Use to_string to see full DataFrame in console
    print("-" * 50)


    # --- Write the Income Statement to a New Excel File ---
    try:
        income_statement_df.to_excel(output_file_name, index=False)
        print(f"\nSUCCESS: Income Statement saved to '{output_file_name}'")
    except Exception as e:
        print(f"ERROR: An error occurred while saving the Income Statement to Excel: {e}")
        print("Please ensure the output file is not open and you have write permissions.")

# --- Main execution block ---
if __name__ == "__main__":
    # Call the function to generate the report
    generate_income_statement()