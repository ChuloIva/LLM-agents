

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
    # allow_delegation=True,
    # tools=[communication_tool]
)

analyst = Agent(
    role='The Data Analyst',
    # expertise='Specializes in NLP and data processing',
    goal='Provide precise and insightful analysis of conversational data, ensuring high accuracy and relevance.',
    backstory="""A highly skilled analyst known for meticulous attention to detail and deep expertise in natural language processing and data analysis. 
    With a history of uncovering nuanced insights from complex datasets, this agent is adept at transforming raw data into meaningful information.""",
    verbose=False,
    # allow_delegation=True,
)

# interviewer = Agent(
#     role='The Conversational Facilitator',
#     goal='Guide a productive and insightful conversation between the two unique individuals. Be very short and concise with your questions and pass them on to another agent',
#     backstory="""An experienced interviewer adept at facilitating engaging and insightful dialogues.
#     Known for drawing out concise and meaningful responses.""",
#     verbose=True,
#     allow_delegation=True,
#     # tools=[interview_tool, communication_tool]
# )

# Create a task for the agents

Story = Task(
    description="""Tell a story rich with diverse places, people, and actions. The narrative should weave through various locations, 
    introducing a range of characters, each with their unique traits and backgrounds. The story should be dynamic, encompassing a variety 
    of actions and events that reveal the depth and complexity of the characters and settings. The task involves creating a cohesive and engaging 
    story that showcases creativity and attention to detail in character development, scene setting, and plot progression. Last output should be
    passed to the next agent so that they can continue and expand upon the story, adding their own elements and twists.""",
    agent=relaxed_businessman
)

extract_story_elements = Task(
    description="""Analyze the provided story and extract only the key elements: places, people, and actions. Your task is to meticulously identify each distinct\
    location, character, and action mentioned in the narrative. For places, list all specific locations described. For people, note down every character introduced,\
    focusing on names and key characteristics. For actions, enumerate the various events and activities that occur throughout the story. Additionally, assess the overall\
    sentiment or emotional tone of the story, and identify specific sentiments associated with each key element (places, people, and actions). This assessment should\
    reflect the mood and emotions conveyed in the narrative. Your output should be a clear, concise, and organized list of these elements, including their associated\
    sentiments, devoid of additional narrative or descriptive context. This list will then be passed to the next agent for further processing.""",
    agent=analyst
)


# shared_insights_dialogue3 = Task(
#     description="""Engage in a structured dialogue where each participant shares insights about their unique
#     lifestyles, perspectives, and experiences. The conversation should be concise, to the point, and revealing
#     of each individual's character and philosophy. The interviewer will facilitate this discussion, ensuring
#     that the conversation remains focused and that each participant has equal opportunity to speak. Last output should be passed to the next agent so that they can respond to it""",
#     agent=interviewer
# )

# Instantiate your crew with a sequential process
crew = Crew(
  agents=[relaxed_businessman, analyst],
  tasks=[Story, extract_story_elements],
  verbose=2, # You can set it to 1 or 2 to different logging levels
)

# Get your crew to work!
result = crew.kickoff()

print("######################")
print(result)