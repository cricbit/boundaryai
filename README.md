# BoundaryAI

BoundaryAI is an AI-powered cricket analyst agent that processes user-input queries related to cricket statistics and provides answers by executing SQL queries on a cricket database. The agent is built using the `autogen` framework and leverages a ConversableAgent to interact with users.

## Features

- **Cricket Query Handling**: Understands and processes queries related to cricket statistics.
- **SQL Query Execution**: Executes SQL queries to fetch data from a cricket database.
- **ConversableAgent**: Utilizes a ConversableAgent to facilitate user interaction.
- **Tool Registration**: Supports tool registration for listing tables, columns, and executing queries.

## Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/cricbit/boundaryai.git
   cd boundaryai
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.9+ installed. Then, install the required packages:

   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**:
   Create a `.env` file in the root directory and add your database and API credentials:
   ```plaintext
   POSTGRES_URL=your_postgres_url
   OPENAI_API_KEY=your_openai_api_key
   ```

## Usage

1. **Run the Agent**:
   Execute the `agent.py` script to start the agent:

   ```bash
   python agent.py
   ```

2. **Interact with the Agent**:
   The agent will prompt you to enter cricket-related queries. For example:

   ```
   How many runs has DA Warner scored in each Big Bash season?
   ```

3. **Receive Results**:
   The agent will process your query and return the results based on the database information.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the GNU General Public License v3.0. See the [LICENSE](LICENSE) file for details.
