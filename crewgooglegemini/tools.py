from dotenv import load_dotenv
load_dotenv()  # Load environment variables from .env file
import os

os.environ["SERPER_API_KEY"] = os.getenv("SERPER_API_KEY")

from crewai_tools import SerperDevTool

# Initialize the tool for internet searching capabilities
tool = SerperDevTool()