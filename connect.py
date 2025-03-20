import asyncio
import os

from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

TASK_PROMPT = """
Goal: Use my LinkedIn to connect with DevSecOps Engineers from the US.

Technical details:
1. Browse to the following URL: https://www.linkedin.com/search/results/people/?geoUrn=%5B%22103644278%22%5D&keywords=DevSecOps%20Engineer
2. For each person that shows and has a "Connect" button, click it, a prompt will show, and then click "Send without a note".
3. Do this continuously for the entire page.
4. If you've reached the end of the page, click "Next" to move to the next page.
"""

config = BrowserConfig(
    chrome_instance_path=os.getenv("CHROME_INSTANCE_PATH"),
)
browser = Browser(config=config)


async def main():
    agent = Agent(
        browser=browser,
        task=TASK_PROMPT,
        llm=ChatOpenAI(model="gpt-4o"),
    )
    await agent.run()


asyncio.run(main())
