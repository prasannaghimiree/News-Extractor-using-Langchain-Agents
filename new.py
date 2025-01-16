import os
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
from tools import search_tool, formatter
from langchain.agents import initialize_agent, Tool, AgentExecutor
import json

# Loading environment variables
load_dotenv()
api_key = os.getenv("LANGCHAIN_API_KEY")
model_url = os.getenv("OLLAMA_MISTRAL_LLM_NAXA")

# Initializing tools for search and formatting
tools = [
    Tool(
        name="search_tool",
        func=search_tool,
        description="Use this tool to search for information on the web."
    ),
    Tool(
        name="formatter",
        func=formatter,
        description="Use this tool to format raw information into JSON."
    )
]

# Initializing the Ollama model
llm = OllamaLLM(
    model="mistral",
    config={
        "max_new_tokens": 1000,
        "temperature": 0.8
    },
)

# Defining prompt template
prompt = PromptTemplate(
    input_variables=["raw_text", "query"],
    template="""
        You are a helpful assistant. Perform the following steps:
        1. Use the 'search_tool' to get raw information based on the user's query.
        2. Analyze the raw information and filter out irrelevant details from keywords in the user's query.
        3. Summarize the filtered content, focusing on the key points, important features, and dates (if any).
        4. Use the 'formatter' tool to convert the summarized content into a structured JSON format.
        5. Ensure the final output is JSON formatted, concise, and relevant to the query.
        Query:
        {query}



        Provide the summary in JSON format after processing all of the above steps.
    """
)

# Initializing the agent with the necessary tools and LLM
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent_type="zero-shot-react-description",  # Using zero-shot-react-description agent
    verbose=True
)

# Main function to process user input
if __name__ == "__main__":
    while True:
        user_query = input("Enter your query (or 'exit' to quit): ")
        if user_query.lower() == 'exit':
            print("Exiting the system.")
            break

        try:
            # Format the prompt with the user's query
            formatted_prompt = prompt.format(query=user_query)
            
            # Run the agent with the formatted prompt and handle parsing errors
            response = agent.invoke(formatted_prompt, handle_parsing_errors=True)
            print("JSON Response:\n", response)

            # Save the response in a human-readable format with proper indentation
            with open("response.json", "w") as json_file:
                json.dump(response, json_file, indent=4)  # Write JSON to file with indentation for readability

        except Exception as e:
            print(f"An error occurred: {str(e)}")
