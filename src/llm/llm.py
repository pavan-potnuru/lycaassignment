from openai import OpenAI

def generate_sql_query(question):
    client = OpenAI()

    prompt = f""" You are a specialist in generating queries for SQLite database.

    There are 3 tables in the database and user will ask questions based on data from these tables:
    - sample_bo_tbl_large: country (a 3 digit code like "AAA"), date, total_mins, international_mins, sms, total_data_usage, payg_amount
    - sample_sub_details_large: country, channel, date, subs, netadds, churn
    - sample_revenue_large: country, channel, date, revenue, net_revenue

    Your task is to generate an SQLite-compatible SQL query to answer the user question.
    If time related queries are asked, fetch todays date and then calculate accordingly.
    Think step by step and then formulate the query. Do not add any comments in the query.
    Generate queries using only builtin functions of SQLite.
    Maintain consistency in your query generation pattern and generate as simple query as possible for a given question.
    If the query cannot be answered from the available datasets, just respond with "Question out of available data range."
    Generate the response which contains reasoning step by step and a query in the following format:
    {{"Reasoning": ..., "Query": ...}}
    User Question: {question}
    """
    #print("Generating SQL query....\n")
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{"role":"user","content":prompt}],
    )
    return response.choices[0].message.content



def generate_final_response(question,answer):
    client = OpenAI()
    response_prompt =f"""Given the following question and answer, rephrase the answer as a proper meaningful response to the question in a friendly tone.
    Question: {question}
    Answer: {answer}""" 
    response = client.chat.completions.create(
        model = "gpt-4o",
        messages = [{"role":"user","content":response_prompt}],
    )
    return response.choices[0].message.content

