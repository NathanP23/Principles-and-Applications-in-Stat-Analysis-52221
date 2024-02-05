# data_config.py

data_operations = [
    {
        "input_csv_path": "/Users/nathan/Documents/HUJI/Principles and Applications in Stat Analysis/Ex1/Data/BTC.csv",
        "date_column_name": 'Date',
        "column_to_rename": 'Close',
        "new_column_name": 'BTC Close Price',
        "calculate_percentage_change": True,
        "output_csv_path": 'output.csv'
    },
    {
        "input_csv_path": "/Users/nathan/Documents/HUJI/Principles and Applications in Stat Analysis/Ex1/Data/INFLATION.csv",
        "date_column_name": 'DATE',
        "column_to_rename": 'T10YIE',
        "new_column_name": 'Inflation Rate',
        "calculate_percentage_change": False,
        "output_csv_path": 'output.csv'
    },
    {
        "input_csv_path": "/Users/nathan/Documents/HUJI/Principles and Applications in Stat Analysis/Ex1/Data/SP500.csv",
        "date_column_name": 'DATE',
        "column_to_rename": 'SP500',
        "new_column_name": 's&p_500',
        "calculate_percentage_change": True,
        "output_csv_path": 'output.csv'
    },
    {
        "input_csv_path": "/Users/nathan/Documents/HUJI/Principles and Applications in Stat Analysis/Ex1/Data/NASDAQ.csv",
        "date_column_name": 'DATE',
        "column_to_rename": 'NASDAQCOM',
        "new_column_name": 'NASDAQ',
        "calculate_percentage_change": True,
        "output_csv_path": 'output.csv'
    },
    {
        "input_csv_path": "/Users/nathan/Documents/HUJI/Principles and Applications in Stat Analysis/Ex1/Data/DOWJONES.csv",
        "date_column_name": 'DATE',
        "column_to_rename": 'DJIA',
        "new_column_name": 'DOWJONES',
        "calculate_percentage_change": True,
        "output_csv_path": 'output.csv'
    }
]
