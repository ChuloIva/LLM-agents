

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



# Define new agents with roles and goals
relaxed_businessman = Agent(
    role='The Yacht-Enthusiast Businessman',
    goal='Share insights about his lifestyle and business strategies. Be very short and concise with your answers and pass them on to another agent',
    backstory="""A successful businessman known for his love of yachting and a relaxed approach to life.
    Balances business acumen with leisure, offering a unique perspective on work-life balance.""",
    verbose=True,
    allow_delegation=True,
    # tools=[communication_tool]
)

napoleon_like_guy = Agent(
    role='The Napoleon-Esque Strategist',
    goal='Discuss his unique past and strategic thinking. Be very short and concise with your answers and pass them on to another agent',
    backstory="""A mysterious individual with a past that mirrors that of Napoleon.
    Known for his strategic thinking and love for frisbee, offering a blend of historical insight and modern tactics.""",
    verbose=True,
    allow_delegation=True,
    # tools=[strategy_tool, communication_tool]
)

interviewer = Agent(
    role='The Conversational Facilitator',
    goal='Guide a productive and insightful conversation between the two unique individuals. Be very short and concise with your questions and pass them on to another agent',
    backstory="""An experienced interviewer adept at facilitating engaging and insightful dialogues.
    Known for drawing out concise and meaningful responses.""",
    verbose=True,
    allow_delegation=True,
    # tools=[interview_tool, communication_tool]
)

# Create a task for the agents
shared_insights_dialogue = Task(
    description="""Engage in a structured dialogue where each participant shares insights about their unique
    lifestyles, perspectives, and experiences. The conversation should be concise, to the point, and revealing
    of each individual's character and philosophy. The interviewer will facilitate this discussion, ensuring
    that the conversation remains focused and that each participant has equal opportunity to speak. Last output should be passed to the next agent so that they can respond to it""",
    agent=relaxed_businessman
)

shared_insights_dialogue2 = Task(
    description="""Engage in a structured dialogue where each participant shares insights about their unique
    lifestyles, perspectives, and experiences. The conversation should be concise, to the point, and revealing
    of each individual's character and philosophy. The interviewer will facilitate this discussion, ensuring
    that the conversation remains focused and that each participant has equal opportunity to speak. Last output should be passed to the next agent so that they can respond to it""",
    agent=napoleon_like_guy
)

shared_insights_dialogue3 = Task(
    description="""Engage in a structured dialogue where each participant shares insights about their unique
    lifestyles, perspectives, and experiences. The conversation should be concise, to the point, and revealing
    of each individual's character and philosophy. The interviewer will facilitate this discussion, ensuring
    that the conversation remains focused and that each participant has equal opportunity to speak. Last output should be passed to the next agent so that they can respond to it""",
    agent=interviewer
)

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[relaxed_businessman, napoleon_like_guy, interviewer],
  tasks=[shared_insights_dialogue, shared_insights_dialogue2, shared_insights_dialogue3],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)