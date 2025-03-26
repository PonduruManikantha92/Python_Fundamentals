import pandas as pd     # Need to import both Pandas and Openpyxl libraries to execute this program

def read_pandas():
    df= pd.read_excel("C:\\Users\\10013887\\OneDrive - AIG Hospitals\\Desktop\\Testing.xlsx")

    test_values = df['ReceiptNo']
    for options in test_values:
        print(options)

read_pandas()

