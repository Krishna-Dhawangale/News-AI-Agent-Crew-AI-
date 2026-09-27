from crewai import Task
from tools import tool
from agents import research_agent, writer_agent

# Research task
research_task = Task(
    description=("Conduct in-depth research on emerging technologies and their potential impact on various industries {topic}."),
    expected_output=("A comprehensive report detailing the findings, including potential applications and implications of the researched technologies."),
    tools=[tool],
    agent=research_agent,
)

# Writer task
writer_task = Task(
    description=("Write an engaging and informative article on the latest technological advancements in {topic}."),
    expected_output=("A well-structured article that effectively communicates the significance of the technological advancements to a broad audience."),
    tools=[tool],
    agent=writer_agent,
    async_execution=False,  # Allow the writer task to run asynchronously
    output_file="new-blog-post.md"  # Specify the output file for the article   
)