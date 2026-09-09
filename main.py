import os
import argparse
from dotenv import load_dotenv
from openai import OpenAI
from system_promt import system_prompt

#type hint
from argparse import Namespace
from openai.types.chat import ChatCompletion



def main():
    #Load environment variables from the local .env file
    load_dotenv()
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if api_key == None:
        raise RuntimeError("Environment variable wasn´t found")

    #Initialize the OpenAI client configured to route requests through OpenRouter
    client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key
    )

    #Uses the argparse python module for the option to add an argument to the command line
    arg_parser = argparse.ArgumentParser(description="Chatbot")
    arg_parser.add_argument("user_prompt", type=str, help = "User prompt")
    arg_parser. add_argument("--verbose", action="store_true", help="Enables verbose output")
    args = arg_parser.parse_args()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": args.user_prompt},
        ]
    #Send a chat completion request to the OpenRouter API
    response = client.chat.completions.create(
        model="openrouter/free",
        messages=messages,
        temperature=0,
    )

    print_to_console(response, args)



def print_to_console(response: ChatCompletion, args: Namespace) -> None:
    if args.verbose:
        print(f"User prompt: {args.user_prompt}")
        if response.usage != None:
            print(f"Prompt tokens: {response.usage.prompt_tokens}")
            print(f"Response tokens: {response.usage.completion_tokens}")
        else:
            raise RuntimeError("Failed api request!")
    print(f"Response:\n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
