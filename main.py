import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from functions.call_function import call_function
from functions.get_files_info import get_files_info_schema
from functions.get_file_content import get_file_content_schema
from functions.write_file_content import write_file_content_schema
from functions.run_python_file import run_python_file_schema


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(api_key=api_key)

available_functions = types.Tool(
    function_declarations=[
        get_files_info_schema,
        get_file_content_schema,
        write_file_content_schema,
        run_python_file_schema,
    ]
)
system_prompt = """
You are a helpful AI coding agent.

When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

- List files and directories
- Read file contents
- Execute Python files with optional arguments
- Write or overwrite files

All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
"""


def main():
    if len(sys.argv) < 2:
        print("Usage: uv run main.py <prompt> [--verbose]")
        exit(1)

    verbose = "--verbose" in sys.argv[2:]
    prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=prompt)])
    ]
    response = client.models.generate_content(
        model="gemini-2.0-flash-001",
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions], system_instruction=system_prompt)
    )
    if not response.function_calls:
        print(response.text)
    else:
        for function_call_part in response.function_calls:
            result = call_function(
                function_call_part, verbose).parts[0].function_response.response
            if not result:
                raise Exception("Function returned no result!")

            if verbose:
                print(f"-> {result}")

    if verbose:
        print("Verbose Info:")
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {
              response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()
