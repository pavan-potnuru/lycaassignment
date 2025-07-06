import os

from src.dataloader.dataloader import load_csvs_to_sqlite
from src.query_engine.query_executor import run_sql
from src.llm.llm import generate_sql_query, generate_final_response


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
            print("\nAnalysing your question...\n")
            response = generate_sql_query(question=question)
            print(f"Reasoning: {eval(response)["Reasoning"]}\n")
            answer =[]
            if eval(response)["Query"] == "Question out of available data range.":
                print("No SQL query generated... \n")
                answer=["No info in database, question is either not relavant or there is no enough data to answer the question."]
            else:
                sql = eval(response)["Query"]
                print(f"Generatede SQL: {sql} \n")
                print("Executing the SQL query in the Database ...\n")
                answer = run_sql(db_path=db_path,sql=sql)
                print("Query Executed successfully... Processing the response...\n")
            print(f"Final Answer: {generate_final_response(question=question,answer=answer)}\n")
            print("""If you have any other question, please type, or type "quit" to stop. \n""")



if __name__ == "__main__":
    main()