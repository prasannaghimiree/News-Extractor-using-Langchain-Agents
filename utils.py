
import os
from dotenv import load_dotenv
from tools import  tools
from llm import get_llm
from langchain.chains import LLMChain

from langchain.agents import create_tool_calling_agent, AgentExecutor, Tool, initialize_agent
from langchain.prompts import ChatPromptTemplate
from langchain_ollama import ChatOllama, OllamaLLM

import json

# Load environment variables
load_dotenv()

#Load Api keys from environment variables
api_key = os.getenv("LANGCHAIN_API_KEY")
model_url = os.getenv("OLLAMA_MISTRAL_LLM_NAXA") 
os.getenv("GROQ_API_KEY")

#using langsmith for tracing
from langsmith import utils
utils.tracing_is_enabled()



from langchain.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            '''
            You are a helpful assistant. Perform the following steps in sequence:

            1. **Search Information:**
               Use the 'search_tool' to retrieve raw information relevant to the user's query.

            2. **Analyze and Filter:**
               Review the retrieved data and filter out irrelevant details. Focus on extracting key points, essential facts, statistics, important dates, and names that are directly related to the user's query.

            3. **Summarize:**
               Provide a concise summary of the filtered content. Focus on summarizing the important aspects, such as key events, facts, and relevant details. If there are dates, ensure to mention them. Make it structured.

            4. **Format the Data:**
               Pass the structured-summarized content to the 'formatter' tool. Ensure that the 'formatter' tool receives the data in the exact format it requires (e.g., structured JSON format).

            5. **Final Output:**
               Return the exact formatted output provided by the 'formatter' tool. If any errors occur during the process, provide the user with appropriate messages:
               - "No data found matching the query." (If the search yields no relevant results)
               - "Formatting failed due to invalid input data." (If formatting could not be completed)
            6. Donot modify result given by formatter. Give exact data given by formatter. 

            ### Error and Query Handling:
            - If there is an error or the query cannot be processed: Respond with an appropriate message indicating the failure.
            - If no data matches the query: Respond with "No data found matching the query."
            '''
        ),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}"),
    ]
)







# llm = ChatOllama(
#     model="mistral",
#     temperature = 0.9
    
# )
# llm=get_llm()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="mixtral-8x7b-32768",
    temperature=0,
  
)
agent = create_tool_calling_agent(tools=tools, llm=llm, prompt=prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)





def fetch_query_response(query: str) -> dict:
    try:
        input_data = {"query": query}
        response = agent_executor.invoke(input_data)
        return response
    except Exception as e:
        return {"error": str(e)}

