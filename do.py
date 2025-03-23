import asyncio
import os
import sys

from browser_use import Agent, Browser, BrowserConfig
from dotenv import load_dotenv

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


def get_llm():
    if "OPENAI_API_KEY" in os.environ:
        from langchain_openai import ChatOpenAI

        return ChatOpenAI(model="gpt-4o")
    elif "AWS_ACCESS_KEY_ID" in os.environ and "AWS_SECRET_ACCESS_KEY" in os.environ:
        from langchain_aws import ChatBedrock

        return ChatBedrock(model_id="us.anthropic.claude-3-5-sonnet-20241022-v2:0")
    else:
        raise EnvironmentError("No valid API keys found for LLM.")


async def main():
    agent = Agent(
        browser=browser,
        task=TASK_PROMPT,
        llm=get_llm(),
    )
    await agent.run()


asyncio.run(main())
