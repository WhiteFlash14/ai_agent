import os 
from google.genai import types

def get_file_content(working_directory,file_path):
    base_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(base_path,file_path))
    if not abs_file_path.startswith(base_path):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    MAX_CHAR = 10000

    try:
        
        with open(abs_file_path,"r") as f:
             file_content_string = f.read(MAX_CHAR)
             file_content_string = file_content_string.strip()
             if len(file_content_string) == MAX_CHAR:
                file_content_string += (
                    f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
                )
        return file_content_string
        

    except Exception as e :
           return f"Error listing files: {e}"
    

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Reads the content of a specified file (up to 10,000 characters) within the permitted working directory. Returns an error if the file is outside the working directory, does not exist, or is not a regular file. If the file is longer than 10,000 characters, the output is truncated and a note is appended.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to read, relative to the working directory.",
            ),
        },
    ),
)