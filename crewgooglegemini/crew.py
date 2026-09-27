from crewai import Crew, Process
from tasks import research_task, writer_task  
from agents import research_agent, writer_agent  

# Forming the tech-focused crew with some enhannced capabilities

crew = Crew(
    agents=[research_agent, writer_agent],
    tasks=[research_task, writer_task],
    process=Process.sequential,
)

# Start the crew's operations
result = crew.kickoff(inputs={"topic": "Artificial Intelligence in Healthcare"})
print(result)