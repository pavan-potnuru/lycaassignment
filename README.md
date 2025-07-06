# Lyca Assignment
🧠 AI-powered structured data question answering assistant over your CSV data, powered by OpenAI + SQLite

## ✨ Overview
This project is an AI-powered assistant that can answer natural language questions over structured data stored in three CSV datasets.
It:

  -Understands your question
  
  -Generates an SQLite-compatible SQL query using an LLM (OpenAI GPT-4o)

  -Executes it on a local database

  -Returns a friendly, conversational answer

  -Ideal for analytics teams, quick exploratory analysis, and data dashboards.

## ⚙ Setup instructions
✅ 1. Clone the repo

    git clone https://github.com/pavan-potnuru/lycaassignment.git
    cd lycaassignment

✅ 2. Create a virtual environment (recommended)

    python -m venv venv
    source venv/bin/activate          # Linux/Mac
    venv\Scripts\activate             # Windows

✅ 3. Install dependencies

    pip install -r requirements.txt

✅ 4. Add your OpenAI API key

  Create a .env file in the project root:
  
      OPENAI_API_KEY=sk-xxxxx...
  (Replace sk-xxxxx... with your real key)

## ▶ How to run

  Execute the following command in terminal or command prompt from the root directory of the repo

    python main.py
    
  You’ll see:

    Hi!!! I am your AI powered Data Assistant. Have query on your data? I am ready to assist you.

    Feel free to ask your question or type 'quit' to exit
Now you can type your questions in natural language!

## 🧪 Example queries & outputs
### 📌 Example 1
  Question: Which country had the highest churn-to-subscriber ratio in Q1?

  Reasoning:

    To find the country with the highest churn-to-subscriber ratio in Q1, we need to compute the churn-to-subscriber ratio for each country during the first quarter of the year (January, February, March). We will first filter the data from 'sample_sub_details_large' table for Q1. Then, we will calculate the churn-to-subscriber ratio by summing the churn and subs for each country within Q1, and finding the maximum ratio.

  Generated SQL:

    SELECT country, SUM(churn) * 1.0 / SUM(subs) AS churn_to_sub_ratio
    FROM sample_sub_details_large
    WHERE strftime('%m', date) IN ('01', '02', '03')
    GROUP BY country
    ORDER BY churn_to_sub_ratio DESC
    LIMIT 1;

  Final Answer:

    "In Q1, country BBB had the highest churn-to-subscriber ratio at approximately 0.29."

### 📌 Example 2
  Question: List countries with highest data usage in Q2.

  Reasoning:

    To determine the countries with the highest data usage in Q2, we need to focus on the 'sample_bo_tbl_large' table, as it contains information about 'total_data_usage'. Q2 consists of the months April, May, and June. Hence, we will filter rows where the date falls in these months. We will group the results by country and summarize the total data usage for each country. Finally, we sort this summarized data in descending order of total data usage and select the top records to identify the countries with the highest data usage.
    
  Generated SQL:

    SELECT country, SUM(total_data_usage) AS total_usage 
    FROM sample_bo_tbl_large 
    WHERE strftime('%m', date) IN ('04', '05', '06') 
    GROUP BY country ORDER BY total_usage DESC;

  Final Answer:

    Certainly! In the second quarter, the countries with the highest data usage are BBB, with 37,459 units, followed by DDD with 30,956 units, CCC with 27,030 units, and AAA with 20,812 units.

## 🧠 Prompting strategy
  The prompt sent to the LLM guides it to:

  -Think step by step (chain-of-thought)

  -Generate a simple, SQLite-compatible SQL query

  -Avoid non-SQLite functions like EXTRACT or TO_DATE

  -Answer only based on data available in the three tables

  -If data is missing → reply "Question out of available data range."

After query execution, another prompt rephrases the raw numbers into a friendly, human-readable response.

## 🧑‍💻 Author

  Pavan Potnuru
