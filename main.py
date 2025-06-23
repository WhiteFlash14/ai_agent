import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from call_function import available_functions,call_function

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
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files
    
    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """


    response = client.models.generate_content(
        model='gemini-2.0-flash-001',
        contents=messages,
        config=types.GenerateContentConfig(
            tools=[available_functions],system_instruction=system_prompt)
    )
    

    
    
    for i in range(min(len(response.candidates), 20)):
        if response.candidates[i]:
            messages.append(response.candidates[i].content)
    




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
    
    function_call_result=[]

    for function_call_part in response.function_calls:
        #print(f"Calling function: {function_call_part.name}({function_call_part.args})")
      result = call_function(function_call_part,verbosity)
      if not result.parts[0].function_response:
          raise Exception("empty function call result")
      if verbosity == True:
          print(f"-> {result.parts[0].function_response.response}")
      messages.append(result)   


    

if __name__ == "__main__":
    main()
