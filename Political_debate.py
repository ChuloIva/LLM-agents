import os
from crewai import Agent, Task, Crew, Process

os.environ["OPENAI_API_KEY"] = "1234"
os.environ["OPENAI_API_BASE"]="http://localhost:1234/v1"
# You can choose to use a local model through Ollama for example.
#
# from langchain.llms import Ollama
# ollama_llm = Ollama(model="openhermes")

# Install duckduckgo-search for this example:
# !pip install -U duckduckgo-search

from langchain.tools import DuckDuckGoSearchRun
search_tool = DuckDuckGoSearchRun()


# Define agents with political leanings
right_wing_analyst = Agent(
  role='Right-Wing Political Analyst',
  goal='Argue in favor of conservative policies and viewpoints',
  backstory="""You are a well-known conservative thinker in Croatia.
  You advocate for traditional values, limited government intervention in the economy,
  and a strong national identity.""",
  verbose=True,
  allow_delegation=False,
  # tools=[search_tool],
  # llm configuration as needed
)

left_wing_analyst = Agent(
  role='Left-Wing Political Analyst',
  goal='Promote progressive policies and social equality',
  backstory="""As a prominent left-wing voice in Croatian politics,
  you focus on social justice, environmental sustainability, and reducing economic inequality.""",
  verbose=True,
  allow_delegation=False,
  # tools=[search_tool],
  # llm configuration as needed
)

# centerist_analyst = Agent(
#   role='Centrist Political Analyst',
#   goal='Find a balanced perspective between left and right viewpoints',
#   backstory="""You are known for your moderate and pragmatic approach to Croatian politics.
#   You often seek to bridge the gap between left and right, emphasizing compromise and unity.""",
#   verbose=True,
#   allow_delegation=True
#   # llm configuration as needed
# )

# Create a debate task
debate_initiation_task = Task(
    description="""Prepare a structured presentation of statements on Croatian politics.
    Focus on topics such as economic policy, social issues, and foreign relations.
    Lay out the statements in a clear, concise manner, providing a solid foundation for a subsequent debate.""",
    agent= right_wing_analyst
)



# Create a debate task
debate_response_task = Task(
    description="""Engage in a structured debate by responding to the statements presented by a previous political candidate on Croatian politics.
    Analyze and debate topics such as economic policy, social issues, and foreign relations, as outlined in the initial presentation.
    Each response should offer a critical analysis of the candidate's statements, providing counterpoints, alternative viewpoints, or supporting arguments.
    Aim to create a dynamic and comprehensive discussion that builds upon the initial presentation.""",
    agent=left_wing_analyst
)

# Create a debate task
# debate_task3 = Task(
#   description="""Engage in a structured debate about Croatian politics.
#   Discuss topics such as economic policy, social issues, and foreign relations.
#   Each agent must present their viewpoints clearly and respond to others' arguments.
#   The final output should be a comprehensive transcript of the debate.""",
#   agents=[centerist_analyst]
# )
# Instantiate your crew with a sequential process
crew = Crew(
  agents=[right_wing_analyst, left_wing_analyst],
  tasks=[debate_initiation_task, debate_response_task],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)