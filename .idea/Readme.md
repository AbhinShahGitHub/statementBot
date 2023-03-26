**StatementBot**

StatementBot is a Python program that uses OpenAI APIs to interact with your bank statement in natural language. The project assumes you have categorized all your transactions into meaningful categories. These transactions are stored in the transactions table in a MySQL database.

**Installation**

To install StatementBot, simply clone the repository on your local machine and configure a MySQL instance. Then, install the database plugin in PyCharm and ensure that you specify the credentials for your MySQL database.
You will also need to obtain a new API key from your OpenAI account to use the program. This key should be added to the testOpenAiApi.py and statementBot.py file where indicated.

**Usage**

Before using StatementBot, make sure that you have categorized your transactions and stored them in the transactions table in the MySQL database.

To run the program, simply execute the main.py file in your Python environment. This will prompt you to enter a natural language query related to your bank statement. The program will then use OpenAI's GPT-3 model to parse your query and return the relevant information from your statement.

Creating the Transactions Table
To create the necessary table for the StatementBot project, you can execute the following SQL command in your MySQL instance:

**sql**

CREATE TABLE transactions (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    date DATE NOT NULL,
    narration VARCHAR(255) NOT NULL,
    value_date DATE NOT NULL,
    debit_amount DECIMAL(10,2) DEFAULT 0,
    credit_amount DECIMAL(10,2) DEFAULT 0,
    chq_ref_number VARCHAR(50),
    closing_balance DECIMAL(10,2) NOT NULL,
    category VARCHAR(50)
);

This will create a table named transactions with the necessary columns id, date, narration, value_date, debit_amount, credit_amount, chq_ref_number, closing_balance, and category.

Remember to properly configure the credentials for your MySQL database in the project's code.
