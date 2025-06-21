import os
from google.genai import types

def write_file(working_directory, file_path, content):
    
       base_path = os.path.abspath(working_directory)
       abs_file_path = os.path.abspath(os.path.join(base_path,file_path))
       if not abs_file_path.startswith(base_path):
           return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
       if not os.path.exists(abs_file_path):
           os.makedirs(os.path.dirname(abs_file_path), exist_ok=True)
       try:
         with open(abs_file_path, "w") as f:
             f.write(content)
         return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


       except Exception as e:
           return f"Error listing files: {e}"




schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Writes the provided content to a specified file within the permitted working directory. If the file or its parent directories do not exist, they are created. Returns an error if the file path is outside the working directory. On success, returns a message indicating the number of characters written.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the file to write to, relative to the working directory.",
            ),
            "content": types.Schema(
                type=types.Type.STRING,
                description="The content to write to the file.",
            ),
        },
    ),
)