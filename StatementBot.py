import openai
import mysql.connector
from tabulate import tabulate
from mysql.connector import Error

secrets = {
    "secret_key": "<your key here>",
    "mysql": {
        "host": "localhost",
        "username": "root",
        "password": "admin123",
        "database": "mysql"
    }
}

openai.api_key = secrets["secret_key"]


def execute_sql_query(query):
    # Initialising variables for connection and cursor to None so avoiding uninitialised (unbound) errors
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host=secrets["mysql"]["host"],
            user=secrets["mysql"]["username"],
            password=secrets["mysql"]["password"],
            database=secrets["mysql"]["database"]
        )
        cursor = connection.cursor(buffered=True)  # Use a buffered cursor
        cursor.execute(query)

        if cursor.rowcount > 0:
            result = cursor.fetchall()
        else:
            result = None

        return result, cursor

    except Error as e:
        print(f"Error: {e}")
        return None
    finally:
        if connection.is_connected() and connection is not None:
            cursor.close()
            connection.close()


def ask_openai_api(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=512,
        n=1,
        top_p=1,
        temperature=0.7
    )

    return response.choices[0].text.strip()


def main():
    while True:
        user_question = input("Ask a question about the transactions data (type 'exit' to quit): ")

        if user_question.lower() == "exit":
            break

        prompt = (
            "There is a database table called 'transactions' with columns 'id', 'date', 'narration', 'value_date', "
            "'debit_amount', 'credit_amount', 'chq_ref_number', 'closing_balance', 'category'.\n\n"
            "The available categories are, Shopping, Wallet Add Money, Credit card payment, Utilities, Refunds, "
            "Entertainment, Salary, Transfer to Own Accounts, Healthcare, ATM, Education, Bank Transfer, "
            "Others, and Interest Earned.\n\n"
            "Write an SQL query to answer the following question:\n\n"
            f"{user_question}\n\n"
            "SQL Query:"
        )

        sql_query = ask_openai_api(prompt)
        # print(f"\nGenerated SQL Query: {sql_query}\n\n")

        query_result, cursor = execute_sql_query(sql_query)

        if query_result is not None:
            headers = [i[0] for i in cursor.description]  # Get column names from the cursor description
            print(tabulate(query_result, headers=headers, tablefmt="pretty"))
            table = tabulate(query_result, headers=headers, tablefmt="pipe")
            summary_prompt = f"Please provide a summary of the following transaction data:\n\n{table}\n\nSummary:"
            summary = ask_openai_api(summary_prompt)
            print(f"Summary: {summary}\n")
            print("\n")
        else:
            print("No results found.\n")


if __name__ == "__main__":
    main()
