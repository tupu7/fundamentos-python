import pandas as pd

# Load the Excel file
file_path = '/mnt/data/Progra.xlsx'
excel_data = pd.ExcelFile(file_path)

# Get the sheet names
sheet_names = excel_data.sheet_names

# Dictionary to hold counts of tables per sheet
tables_count = {}

# Read each sheet and count the number of tables (assuming "table" means data blocks)
for sheet in sheet_names:
    df = pd.read_excel(file_path, sheet_name=sheet, header=None)
    # Count non-empty regions as "tables" by looking for separated blocks of data
    non_empty_cells = df.notnull().astype(int)
    # Mark transitions from empty to non-empty as table starts
    table_starts = (non_empty_cells.diff(axis=0) == 1).sum().sum() + (non_empty_cells.diff(axis=1) == 1).sum().sum()
    tables_count[sheet] = table_starts

tables_count