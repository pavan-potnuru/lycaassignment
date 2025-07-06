import os

from src.dataloader.dataloader import load_csvs_to_sqlite
from src.query_engine.query_executor import run_sql
from src.llm.llm import generate_sql_query, extract_sql_query,generate_final_response


def main():
    db_path = os.path.abspath("../lycaassignment/db/data.db")
    load_csvs_to_sqlite(db_path=db_path)

    print("""Hi!!! I am your AI powered Data Assistant. Have query on your data? I am ready to assist you. \n
          Feel free to ask your question or type 'quit' to exit\n""")
    
    while True:
        question = input("Your Question: ")
        if question.lower() == 'quit':
            print("Goodbye !!!")
            break
        else:
            print("Analysing your question...\n")
            response = generate_sql_query(question=question)
            print("Extracting SQL query from the response ...\n")
            sql = extract_sql_query(response=response)
            answer =[]
            if sql == 0:
                print("No query generated...")
            else:
                print("Executing the SQL query in the Database ...\n")
                answer = run_sql(db_path=db_path,sql=sql)
                print("Query Executed successfully... Processing the response...\n")
            print(generate_final_response(question=question,answer=answer))
            print("""If you have any question, type it, or type "quit" to stop""")



if __name__ == "__main__":
    main()