import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI

def get_azure_llm():
    # Load environment variables
    load_dotenv()
    
    # Get Azure OpenAI configuration from environment variables
    azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
    api_key = os.getenv("AZURE_OPENAI_API_KEY")
    deployment_name = os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME", "gpt-4o-2")  # Default to a common deployment name
    
    if not azure_endpoint or not api_key:
        raise ValueError("Azure OpenAI endpoint and API key must be set in environment variables")
    
    return AzureChatOpenAI(
        azure_endpoint=azure_endpoint,
        deployment_name=deployment_name,
        openai_api_key=api_key,
        openai_api_version="2024-02-01",
        temperature=0.7,
        max_tokens=1000
    )
