import os
from crewai import Agent, Task, Crew, Process
import openai
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.chat_models import openai


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


# Define agents with roles and goals
master_sourcer = Agent(
  role='Master Sourcer',
  goal='Gather critical evidence and information about the potato robbery',
  backstory="""An expert in sourcing information and evidence, known for solving peculiar cases.
  Has a vast network and uses unconventional methods to uncover truths.""",
  verbose=True,
  allow_delegation=False,
  tools=[search_tool],
  llm=openai.ChatOpenAI(model_name="gpt-3.5", temperature=0.7,max_tokens=250)
  
)

tsunami_survivor = Agent(
  role='Instigated Survivor',
  goal='Use personal insights and experiences to aid in the investigation',
  backstory="""A survivor of a devastating tsunami with a unique perspective.
  Has become deeply involved in community affairs and is determined to uncover the truth behind the potato robbery.""",
  verbose=True,
  allow_delegation=True,
  llm=openai.ChatOpenAI(model_name="gpt-3.5", temperature=0.7,max_tokens=250),
)

# Create tasks for your agents
task1 = Task(
  description="""Investigate the scene of the potato robbery. Gather as much evidence as possible,
  including witness statements, security footage, and any unusual clues. Your final answer MUST be a detailed
  evidence report""",
  agent=master_sourcer
)

task2 = Task(
  description="""Based on the evidence collected, use your personal experiences and community connections
  to hypothesize who might be behind the potato robbery and why. Consider motives, opportunities,
  and any relevant past incidents. Your final answer MUST be a hypothesis report with potential suspects and motives.""",
  agent=tsunami_survivor
)
# Instantiate your crew with a sequential process
crew = Crew(
  agents=[master_sourcer, tsunami_survivor],
  tasks=[task1, task2],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)