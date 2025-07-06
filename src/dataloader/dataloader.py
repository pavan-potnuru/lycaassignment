import sqlite3
import pandas as pd
import os

def load_csvs_to_sqlite(db_path):
    try:
        print("Please wait while we load the data into database...\n")
        
        conn = sqlite3.connect(db_path)
        # Load each CSV
        bo_df = pd.read_csv(os.path.abspath('../lycaassignment/data/sample_bo_tbl_large.csv'))
        bo_df.to_sql('sample_bo_tbl_large', conn, if_exists='replace', index=False)

        sub_df = pd.read_csv(os.path.abspath('../lycaassignment/data/sample_sub_details_large.csv'))
        sub_df.to_sql('sample_sub_details_large', conn, if_exists='replace', index=False)

        rev_df = pd.read_csv(os.path.abspath('../lycaassignment/data/sample_revenue_large.csv'))
        rev_df.to_sql('sample_revenue_large', conn, if_exists='replace', index=False)

        print("Data loaded successfully to Database ...!\n")
    except FileNotFoundError as e:
        print(f"Error while loading data: {e}")
    except Exception as e:
        print(f"Some exception occured while loading data: {e}")
    finally:
        conn.close()

    

