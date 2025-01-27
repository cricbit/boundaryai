import os
import tempfile

from dotenv import load_dotenv

from autogen import ConversableAgent
from autogen.coding import LocalCommandLineCodeExecutor

from sql import *
from utils import register_tools

load_dotenv()

# Create a temporary directory to store the code files.
temp_dir = tempfile.TemporaryDirectory()

# Create a local command line code executor.
executor = LocalCommandLineCodeExecutor(
    timeout=10,  # Timeout for each code execution in seconds.
    work_dir=temp_dir.name,  # Use the temporary directory to store the code files.
)

assistant = ConversableAgent(
    "Cricket Analyst Agent",
    system_message="""
        You are a cricket analyst agent. 
        Remember that First Class, List A, and T20 are base formats, while T20I, ODI, and Test are the international formats. 
        When returning a result regarding a player, return the name of the player, the format, and the team(s) they played for.
        If the user request contains a query regarding a series, player or team, first search for the same in the database as the series name might differ from the name in the database.
        Remember that batter_id or bowler_id are NOT the batter or bowler name. Do not use batter_id="name" or bowler_id="name" in the query.
        DO NOT USE the raw_matches and raw_data tables present in the database.
        Try to get the result with a single query using JOINs.
    """,
    llm_config={"config_list": [{"model": "gpt-4o", "api_key": os.environ.get("OPENAI_API_KEY")}]},
    code_execution_config=False,  # Turn off code execution, by default it is off.
    function_map=None,  # No registered functions, by default it is None.
    human_input_mode="NEVER",  # Never ask for human input.
)

user_proxy = ConversableAgent(
    name="User",
    llm_config=False,
    # is_termination_msg=lambda msg: msg.get("content") is not None and "TERMINATE" in msg["content"],
    human_input_mode="ALWAYS",
)

register_tools(
    assistant,
    user_proxy,
    [
        {
            "name": "list_tables",
            "description": "List all tables in the database",
            "func": list_tables
        },
        {
            "name": "list_columns",
            "description": "List all columns in a table",
            "func": list_columns
        },
        {
            "name": "execute_query",
            "description": "Execute a query and return the result",
            "func": execute_query
        }
    ]
)

chat_result = user_proxy.initiate_chat(assistant, message="How many runs has DA Warner scored in each Big Bash season?")

print(chat_result)