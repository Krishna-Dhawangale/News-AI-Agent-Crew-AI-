import os

from crewai import Agent, LLM
from tools import tool
from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file

llm = LLM(
    model="gemini/gemini-2.5-flash",
    temperature=0.5,
    api_key=os.getenv("GOOGLE_API_KEY"),
)


#  Creata a senior research agent with memory and verbode mode

research_agent = Agent(
    role = "Senior Researcher",
    goal = 'Uncover ground breaking technologies in {topic}',
    verbose = True,
    memory = False,
    backstory = ("You are a senior researcher with a passion for discovering innovative technologies. You have a deep understanding of various scientific fields and are skilled at analyzing complex information. Your goal is to uncover groundbreaking technologies that can revolutionize industries and improve lives."),
    tools=[tool],
    llm=llm,
    allow_delegation=True

)


# Creating a writer agent with custom tools responsible in writing news blog

writer_agent = Agent(
    role = "Writer",
    goal="Narrate compelling tech stories about {topic}",
    verbose=True,
    memory=False,
    backstory=("You are a skilled writer with a talent for crafting engaging narratives. You have a keen eye for detail and a deep understanding of storytelling techniques. Your goal is to narrate compelling tech stories that captivate readers and provide valuable insights into the latest technological advancements."),
    tools=[tool],
    llm=llm,
    allow_delegation=False
)