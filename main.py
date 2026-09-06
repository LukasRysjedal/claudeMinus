import os
from dotenv import load_dotenv
from openai import OpenAI


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

    #Send a chat completion request to the OpenRouter API
    promt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    response= client.chat.completions.create(
        model="openrouter/free",
        messages=[
            {
                "role": "user",
                "content": f"{promt}",
            }
        ],
    )

    #Print logic
    print(f"User promt: {promt}")
    if response.usage != None:
        print(f"Prompt tokens: {response.usage.prompt_tokens}")
        print(f"Response tokens: {response.usage.completion_tokens}")
    else:
        raise RuntimeError("Failed api request!")
    #Extract and print the text content from the first completion choice
    print(f"Response:\n{response.choices[0].message.content}")


if __name__ == "__main__":
    main()
