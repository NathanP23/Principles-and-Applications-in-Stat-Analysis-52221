import pandas as pd
import numpy as np
import os

def read_csv(file_path):
    # Read a CSV file from the given file path and return a Pandas DataFrame.
    # This DataFrame will be used for further processing.
    return pd.read_csv(file_path)

def rename_column(df, old_name, new_name):
    # Rename a specified column in the DataFrame.
    # This is useful for standardizing column names across different datasets.
    if old_name and new_name:
        df.rename(columns={old_name: new_name}, inplace=True)
    return df

def parse_date_column(df, date_column_name):
    # Convert the specified column to a datetime format.
    # Ensures consistency in date representation, which is critical for time series analysis.
    # The 'errors='coerce'' argument turns unparseable values into NaT (Not-a-Time).
    if date_column_name in df.columns:
        df[date_column_name] = pd.to_datetime(df[date_column_name], errors='coerce')
        df.rename(columns={date_column_name: 'Date'}, inplace=True)
    return df

def convert_to_numeric(df):
    # Convert columns with numerical values to Pandas numeric types for mathematical operations.
    # The 'errors='coerce'' argument turns unparseable values into NaN.
    for col in df.columns:
        if col != 'Date':
            df[col] = pd.to_numeric(df[col], errors='coerce')
    return df

def clean_data(df):
    # Remove any rows containing '.', ' ', or NaN values.
    # This step is crucial to ensure the quality of data for analysis.
    df.replace(['.', ' '], np.nan, inplace=True)
    df.dropna(inplace=True)
    return df

def add_percentage_change_columns(df):
    # For each numeric column, calculate the percentage change and create a new column.
    # This is useful for analyzing trends over time.
    numeric_cols = df.select_dtypes(include=[np.number]).columns
    for col in numeric_cols:
        if col != 'Date':  # Avoid computing percentage change for 'Date'
            # Calculate percentage change
            df[col + ' % Change'] = df[col].pct_change() * 100
    return df

def read_existing_output(output_csv_path):
    # Read an existing output CSV file if it exists; if not, return None.
    # This function is used to check for and read any previously processed data.
    if os.path.exists(output_csv_path):
        return pd.read_csv(output_csv_path)
    else:
        return None

def combine_data(new_df, existing_df):
    # Combine new data with existing data, giving priority to new data.
    # This is done by setting 'Date' as the index and using combine_first method.
    existing_df.set_index('Date', inplace=True)
    new_df.set_index('Date', inplace=True)
    return new_df.combine_first(existing_df).reset_index()

def reorder_columns(df, original_columns):
    # Ensure the 'Date' column is the first column, followed by the original and new columns.
    # This step is important for maintaining a consistent data structure.
    new_columns = [col for col in df.columns if col not in original_columns and col != 'Date']
    column_order = ['Date'] + [col for col in original_columns if col != 'Date'] + new_columns
    return df[column_order]

def sort_and_clean_combined_df(df):
    # Sort the DataFrame by the 'Date' column and remove any rows with NaN values.
    # Sorting is essential for time series data and NaN removal ensures data integrity.
    df.sort_values(by='Date', inplace=True)
    df.dropna(inplace=True)
    return df

def save_to_csv(df, output_csv_path):
    # Save the processed DataFrame to a CSV file at the specified path.
    # This creates a persistent record of the processed data for future use.
    df.to_csv(output_csv_path, index=False)

def process_csv(input_csv_path, date_column_name, column_to_rename, new_column_name, calculate_percentage_change):
    # Core processing function for the input CSV.
    # Includes renaming columns, parsing dates, converting data types, and optionally adding percentage change columns.
    df = read_csv(input_csv_path)
    df = rename_column(df, column_to_rename, new_column_name)
    
    df = parse_date_column(df, date_column_name or 'Date')
    df = convert_to_numeric(df)
    df = clean_data(df)
    if calculate_percentage_change:
        df = add_percentage_change_columns(df)
    return df

def process_and_append_csv(input_csv_path, date_column_name=None, column_to_rename=None, new_column_name=None, calculate_percentage_change=False, output_csv_path='output.csv'):
    # Main function to process and append CSV data.
    # Orchestrates the reading, processing, combining, and saving of data.
    # Handles both new data and existing data, merging them appropriately.
    new_df = process_csv(input_csv_path, date_column_name, column_to_rename, new_column_name, calculate_percentage_change)
    existing_df = read_existing_output(output_csv_path)

    if existing_df is not None:
        existing_df = parse_date_column(existing_df, 'Date')
        combined_df = combine_data(new_df, existing_df)
        combined_df = reorder_columns(combined_df, list(existing_df.columns) if 'Date' in existing_df.columns else ['Date'] + list(existing_df.columns))
    else:
        combined_df = new_df

    combined_df = sort_and_clean_combined_df(combined_df)
    save_to_csv(combined_df, output_csv_path)