import pandas as pd

def load_data():
    df = pd.read_csv("data/student_dataset_v2.csv")
    
    print("=" * 50)
    print("MODULE 1: DATA LOADING")
    print("=" * 50)
    
    print("\nFIRST 5 ROWS:")
    print(df.head())
    
    print("\nLAST 5 ROWS:")
    print(df.tail())
    
    print("\nSHAPE OF DATASET:")
    print(df.shape)
    
    print("\nCOLUMN NAMES:")
    print(df.columns)
    
    print("\nDATA TYPES:")
    print(df.dtypes)
    
    return df