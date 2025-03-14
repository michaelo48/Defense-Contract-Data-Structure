import pandas as pd
import os
import ContractLinkedList
from ContractLinkedList import ContractNode
import Clin
import math
import numpy as np
def read_excel_first_10_rows(file_path):
    """
    Read an Excel file and print the first 10 rows.
    
    Parameters:
    file_path (str): Path to the Excel file
    """
    try:
        # Check if file exists and is accessible
        if not os.path.exists(file_path):
            print(f"Error: File '{file_path}' does not exist.")
            return None
        
        # Check if we have read permission
        if not os.access(file_path, os.R_OK):
            print(f"Error: No read permission for '{file_path}'.")
            return None
            
        # Read the Excel file into a pandas DataFrame
        df = pd.read_excel(file_path, usecols=[0])
        
        # Print information about the DataFrame
        print(f"Excel file has {df.shape[0]} rows and {df.shape[1]} columns.")
        print(f"Column names: {list(df.columns)}")
        
        # Print the first 10 rows
        num_rows = len(df)
        print(df.head(num_rows))
        
        return df
    except PermissionError:
        print(f"Error: Permission denied for '{file_path}'. The file might be open in another program.")
    except Exception as e:
        print(f"Error reading Excel file: {e}")
def read_Clins(filepath, start: int, end: int):
    df = pd.read_excel(filepath, usecols=[1])
    rows_subset = df.iloc[start: end]
    
    
def create_LinkedList(file_path):
    df = pd.read_excel(file_path, usecols=[0])
    totalcount = 0
    current_row = 0
    for i in range(len(df)):
        value = df.iloc[i, 0]
        if not math.isnan(value):
            
            
            print(df.iloc[i, 0])
           
            
            
        
    
    

    
        

# Example usage
if __name__ == "__main__":
    file_path = "book1.xlsx"  # Using the file name from your error message
    
    create_LinkedList(file_path)
    
