from crewai import Agent, Task, Crew
from azure_llm import get_azure_llm

azure_llm = get_azure_llm()

# Define two agents
research_agent = Agent(
    role='Researcher',
    goal='Find the most relevant and up-to-date information about Microsoft Azure AI products',
    backstory='Expert in AI tools and Microsoft ecosystem',
    verbose=True,
    llm=azure_llm
)

writer_agent = Agent(
    role='Technical Writer',
    goal='Summarize technical content for executive presentation',
    backstory='Skilled at converting technical info into executive-friendly language',
    verbose=True,
    llm=azure_llm
)

# Define task
research_task = Task(
    description='Search and gather the latest updates on Azure AI Foundry and its integration with LLMs.',
    agent=research_agent
)

write_task = Task(
    description='Summarize findings into a 5-paragraph executive briefing.',
    agent=writer_agent
)

# Build and run crew
crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, write_task],
    verbose=True
)

result = crew.run()
print(result)
