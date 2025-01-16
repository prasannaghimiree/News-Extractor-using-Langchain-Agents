import os
# from langchain.agents import initialize_agent
from langchain.prompts import ChatPromptTemplate
# from langchain.tools import StructuredTool



# from langchain_ollama import OllamaLLM
from dotenv import load_dotenv
from tools import search_tool, formatter, tools
from langchain.agents import create_tool_calling_agent, AgentExecutor, Tool, initialize_agent
from langchain_ollama import OllamaLLM
# from langchain.chains import LLMChain
from llm import get_llm
import json

# Loading environments
load_dotenv()
api_key = os.getenv("LANGCHAIN_API_KEY")
model_url = os.getenv("OLLAMA_MISTRAL_LLM_NAXA")

#using langsmith for tracing
from langsmith import utils
utils.tracing_is_enabled()

# #initializing two tools one for search using searXNG and another for formatiing into jason format


# from langchain.agents import Tool

# searching_tool = Tool(
#     name="search_tool",
#     func=search_tool,  
#     description="Searches for information on the web."
# )

# # formatting_tool = Tool(
# #     name="formatter",
# #     func=formatter,  
# #     description="Formats raw information into JSON."
# # )
# formatting_tool = Tool(
#     name="formatter",
#     func=formatter,
#     description="Formats raw information into structured JSON."
# )

# tools = [searching_tool, formatting_tool]

# importing anthropic llm from llm.py
# llm = get_llm()
# llm = OllamaLLM(model_id="mistral", model_url=model_url)
# llm = OllamaLLM(
#     model="mistral",
#     config={
#         "max_new_tokens": 1000,
#         "temperature": 0.8
#     },
# )

# Define tools as LangChain `Tool` objects
# search_tool = Tool(
#     name="search_tool",
#     func=search_tool,
#     description="Use this tool to search for information on the web."
# )

# formatter_tool = Tool(
#     name="formatter",
#     func=formatter,
#     description="Use this tool to format raw information into JSON."
# )

#Defining prompt so that agent can handle well.
from langchain.prompts import PromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            '''
            You are a helpful assistant. Perform the following steps:
            
            1. Use the 'searching_tool' to get raw information based on the user's query.
            
            2. Analyze the raw information and filter out irrelevant details from keywords in the user's query.
            3. Summarize the filtered content, focusing on the key points, important features, and dates (if any).
            4. Use the 'formatting_tool' tool to give the final output, `formatting_tool` expects the input format as given in its description .
            5. Ensure the final output is JSON formatted, concise, and relevant to the query.
            ### Error and Query Handling
            - If there is an error or the query cannot be processed: Respond with an appropriate message.
            - If no data matches the query: Respond with "No data found matching the query."
            '''
        ),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)
# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             '''
#             You are a helpful assistant. Perform the following steps:

#             1. Use the 'search_tool' to retrieve raw information based on the user's query. 
#                - The result from the search tool will be either a list or dictionary containing relevant data (e.g., news articles, headlines, URLs, etc.).
#                - Make sure the information retrieved is relevant to the user's query.

#             2. Analyze the retrieved information:
#                - If the result is in a list format (multiple items), iterate through each item.
#                - If the result is a dictionary (single item), process it directly.
#                - Filter out irrelevant details and focus on extracting key features such as:
#                  - Headline
#                  - Author
#                  - Publication Date
#                  - Event Date (if available)
#                  - Source URL
#                  - Content
#             3. Try to convert it into dictionary and pass it to formatter tool.

#             4. Summarize the filtered information in a clear, concise manner.
#                - Extract the relevant fields and ensure that the data corresponds to the format expected by the 'formatter' tool.

#             5. Pass the summarized and structured data to the 'formatter' tool in the following format:
#                - The tool expects a list of dictionaries, where each dictionary contains:
#                      "headline": "<extracted headline>",
#                      "author": "<extracted author>",
#                      "publication_date": "<extracted publication date>",
#                      "content": "<extracted content>",
#                      "event_date": "<extracted event date>",
#                      "source_url": "<extracted source URL>"
#                - If the raw data is a list of multiple items, return a list of such dictionaries.
#                - If there is only one item, return it as a single dictionary within a list.

#             6. If no relevant data is found, respond with:
    
#                    "error": "No data found matching the query."
    

#             7. If an error occurs during the process, provide a structured error message:
#                    "error": "<error message>"
            
#             '''
#         ),
#         ("human", "{query}"),
#         ("placeholder", "{agent_scratchpad}"),
#     ]
# )

# prompt = ChatPromptTemplate.from_messages(
#     [
#         (
#             "system",
#             '''
#             You are a helpful assistant that processes user queries in a structured sequence of steps:
            
#             1. **Search**: Use the `searching_tool` to gather raw information based on the user's query.
#             2. **Summarize**: Analyze the results using the LLM to filter out irrelevant details, focusing on the core keywords in the user's query.
#             3. **Format**: Use the `formatting_tool` to structure the summarized information into a concise and JSON-formatted output.
            
#             ### Error Handling
#             - If no data is found during the search, respond: "No data found matching the query."
#             - If there is an error, describe the issue clearly.
            
#             Always strictly follow this sequence of operations and ensure the final output is JSON formatted if relevant data is found.
#             '''
#         ),
#         (
#             "human",
#             '''
#             {query}
            
#             ### Instructions
#             - Start by using the `searching_tool` for information retrieval.
#             - Summarize the search results using LLM, extracting only relevant details.
#             - Format the summarized results into JSON using the `formatting_tool`.
#             '''
#         ),
#         ("placeholder", "{agent_scratchpad}"),
#     ]
# )




# Initialize create_tool_calling_agent with tools, llm and prompt
# agent = create_tool_calling_agent(
#     tools=tools,
#     llm=llm,
#     prompt=prompt,
# )
# agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

# agent = initialize_agent(
#     tools=tools,
#     llm=llm,
#     agent="zero-shot-react-description", 
#     verbose=True
# )

# from langchain_experimental.llms.ollama_functions import OllamaFunctions

# model = OllamaFunctions(model="mistral")
# llm = model.bind_tools(
#     tools=[search_tool, formatter])
from langchain_ollama import ChatOllama

# llm = ChatOllama(
#     model="mistral",
#     model_url=model_url
    
# )

# llm = ChatOllama(
#     model="mistral",
#     temperature=0.9
    
# )

llm = get_llm()

# Initialize create_tool_calling_agent with tools, llm and prompt
agent = create_tool_calling_agent(
    tools=tools,
    llm=llm,
    prompt=prompt,
)
from langchain.agents import AgentExecutor

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)


# Main function
import json

if __name__ == "__main__":
    while True:
        user_query = input("Enter your query (or 'exit' to quit): ")
        if user_query.lower() == 'exit':
            print("Exiting the system.")

            break

        try:
            print("a")
            # use agent to fetch from the web at first, then summarize it through LLM and make a formatted output in JSON format.
            # formatted_prompt = prompt.format(query=user_query)
            
            # Run the agent with the formatted prompt
            input_data = {
                "query": user_query,
                }

            # response = agent.invoke(input_data)
            response = agent_executor.invoke(input_data)
            print("b")

            

            with open("response.json", "w") as json_file:
                json.dump(response, json_file, indent=4)  

        except Exception as e:
            print('c')
            print(f"An error occurred: {str(e)}")


