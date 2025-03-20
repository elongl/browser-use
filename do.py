import asyncio
import os
import sys

from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

if len(sys.argv) < 2:
    print("Error: Please provide a task file.")
    sys.exit(1)

load_dotenv()

with open(f"tasks/{sys.argv[1]}.txt") as task_prompt_file:
    TASK_PROMPT = task_prompt_file.read()

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
