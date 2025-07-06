import sqlite3
import pandas as pd

def load_csvs_to_sqlite(db_path):
    conn = sqlite3.connect(db_path)
    # Load each CSV
    bo_df = pd.read_csv('../data/sample_bo_tbl_large.csv')
    bo_df.to_sql('sample_bo_tbl_large', conn, if_exists='replace', index=False)

    sub_df = pd.read_csv('../data/sample_sub_details_large.csv')
    sub_df.to_sql('sample_sub_details_large', conn, if_exists='replace', index=False)

    rev_df = pd.read_csv('../data/sample_revenue_large.csv')
    rev_df.to_sql('sample_revenue_large', conn, if_exists='replace', index=False)

    conn.close()

