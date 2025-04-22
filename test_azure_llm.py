from azure_llm import get_azure_llm
from langchain.schema import HumanMessage

def test_azure_llm():
    # Get the Azure LLM instance
    llm = get_azure_llm()
    
    # Create a test message
    message = HumanMessage(content="Hello! Can you tell me a short joke?")
    
    # Get the response
    response = llm([message])
    
    # Print the response
    print("\nResponse from Azure OpenAI:")
    print(response.content)

if __name__ == "__main__":
    test_azure_llm() 