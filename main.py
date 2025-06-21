import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    client = genai.Client(api_key=api_key)
    
    args = sys.argv[1:]

    user_prompt = " ".join(args)
    verbosity = False
    for i,arg in enumerate(args):
        if arg == "--verbose":
            verbosity = True
            args.pop(i)
            print(f"User prompt: {user_prompt}\n")
            break

    if not args:
       print("AI Code Assistant")
       print('\nUsage: python main.py "your prompt here"[ --verbose]')
       print('Example: python main.py "How do I build a calculator app?"')
       sys.exit(1)

    

    messages = [
        types.Content(
            role="user",
            parts=[types.Part(text=user_prompt)]
        ),
    ]
    generate_response(client, messages,verbosity)


def generate_response(client, messages, verbosity):

    system_prompt = """
    You are a helpful AI coding agent.
    
    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:
    
    - List files and directories
    
    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """


    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],system_instruction=system_prompt)
    )

    # if response.function_calls != None:
    #     # print(response.function_calls[0])
    #     print(f"Calling function: {response.function_calls[0].name}({response.function_calls[0].args})")
   

    if verbosity == True:
         print("Prompt tokens:", response.usage_metadata.prompt_token_count)
         print("Response tokens:", response.usage_metadata.candidates_token_count)

    # print("Response:")
    # print(response.text)

    if not response.function_calls:
        return response.text

    for function_call_part in response.function_calls:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")



if __name__ == "__main__":
    main()
