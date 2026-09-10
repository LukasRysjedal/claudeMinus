

# AI Coding Agent

A simple AI agent that can inspect project files, run Python code, and make code changes to fix bugs.

## How It Works

The agent sends your request to an AI model along with a system prompt. The model can choose from tools such as:

- Reading file contents
- Listing files in a directory
- Running Python files
- Writing changes to files

The agent repeats this process until the model finishes its task.

## Setup

1. Install project dependencies:

```bash
uv sync

    Add your API key to your environment or configuration file.

Run the Agent

Start the agent with:

uv run main.py

Then describe what you want it to do, for example:

Fix the calculator bug where multiplication is evaluated incorrectly.

Example Use Cases

    Find and fix a bug
    Explain a piece of code
    Update a function
    Run a program and diagnose an error

Important Note
    The models working directory range is manually set to the calculator directory for security reasons