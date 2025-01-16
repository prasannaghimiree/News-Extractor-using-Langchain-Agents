import os
from dotenv import load_dotenv
from langchain_aws import ChatBedrock
from langchain_ollama import OllamaLLM
# Loading environments
load_dotenv()
aws_access_key_id = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_access_key= os.getenv("AWS_SECRET_ACCESS_KEY")
aws_default_region = os.getenv("AWS_DEFAULT_REGION")
ollama_naxa_llm = os.getenv("OLLAMA_MISTRAL_LLM_NAXA")

model_id = "anthropic.claude-3-5-sonnet-20240620-v1:0"
def get_llm():
    return ChatBedrock(
        region_name=aws_default_region,
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key,
        model_id=model_id,
        model_kwargs=dict(temperature=0),
    )

def get_naxa_llm():
    return OllamaLLM(model_id="mistral", model_url=ollama_naxa_llm)

