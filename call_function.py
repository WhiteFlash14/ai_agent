from google.genai import types

from functions.get_files_info import schema_get_files_info,get_files_info
from functions.get_file_content import schema_get_file_content,get_file_content
from functions.run_python import schema_run_python_file,run_python_file
from functions.write_file import schema_write_file,write_file


available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_write_file,
            schema_get_file_content,
            schema_run_python_file
        ]
)


def call_function(function_call_part, verbosity=False):
    if verbosity == True:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f" - Calling function: {function_call_part.name}")
    
    function_dict = {
        "get_files_info" : get_files_info,
        "get_file_content" : get_file_content,
        "write_file" : write_file,
        "run_python_file": run_python_file
    }

    function_name = function_call_part.name

    if function_name not in function_dict:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_name,
                    response={"error": f"Unknown function: {function_name}"},
                )
            ],
        )
    args = dict(function_call_part.args)
    function_result = function_dict[function_name](**args,working_directory = "./calculator")
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_name,
                response={"result": function_result},
            )
        ],
    )