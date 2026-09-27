# CrewAI Gemini News Agent

A CrewAI project that uses Google Gemini to research and write a technology article. The current workflow generates an article about artificial intelligence in healthcare.

## Project Structure

```text
crewgooglegemini/
  agents.py       # Gemini-powered research and writer agents
  crew.py         # Crew entry point
  tasks.py        # Research and writing tasks
  tools.py        # Serper web search tool
requirements.txt
```

## Requirements

- Python 3.10 or newer
- A Google Gemini API key
- A Serper API key for web search

## Setup

Create and activate a virtual environment:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

Install the dependencies:

```powershell
pip install -r requirements.txt
```

Create a `.env` file in the project root:

```env
GOOGLE_API_KEY=your_google_api_key
SERPER_API_KEY=your_serper_api_key
```

Never commit `.env` or expose your API keys. The repository `.gitignore` excludes it.

## Run

From the repository root:

```powershell
python crewgooglegemini\crew.py
```

The generated article is saved to:

```text
crewgooglegemini/new-blog-post.md
```

## Notes

The workflow uses the Gemini model configured in `agents.py`. Gemini API quota and rate limits apply when running the crew.
