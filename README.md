# Browser Use

An easy way to create browser automations using AI agents.

## Setup

1. Run `pip install -r requirements.txt`.
2. Create the following `.env` file:

```bash
# If you're using OpenAI.
OPENAI_API_KEY=...

# If you're using AWS Bedrock.
AWS_ACCESS_KEY_ID=...
AWS_SECRET_ACCESS_KEY=...

# Required for using cookies such as post-login automations.
CHROME_INSTANCE_PATH=...
```

## Usage

1. Choose a task from `tasks`.
2. Run: `python do.py <task>`
3. Enjoy!
