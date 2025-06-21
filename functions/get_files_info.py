import os
from google.genai import types

# def get_files_info(working_directory, directory=None):
#     if directory not in os.listdir(working_directory):
#         return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    

#     if (not os.path.isdir(os.path.join(working_directory, directory))):
#         return (f'Error: "{directory}" is not a directory')
    

#     for item in os.listdir(os.path.join(working_directory, directory)):

#         item_path = os.path.join(working_directory, directory, item)

#         if os.path.isfile(item_path):
#             print(f"{item}: file_size: {os.path.getsize(item_path)} bytes is_dir: False")

#         elif os.path.isdir(item_path):
            
#             total_size = 0
#             for file in os.listdir(item_path):
#                 filepath = os.path.join(item_path, file)
#             # Skip broken symlinks or inaccessible files
#                 if os.path.isfile(filepath):
#                     total_size += os.path.getsize(filepath)
#             print(f"{item}: file_size: {total_size} bytes is_dir: True")


def get_files_info(working_directory, directory=None):
    base_path = os.path.abspath(working_directory)
    dir_path = os.path.abspath(os.path.join(base_path,directory))
    if not dir_path.startswith(base_path):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    if not os.path.isdir(dir_path):
        return f'Error: "{directory}" is not a directory'
    try:
        files_info = []
        for item in os.listdir(dir_path):
             item_path = os.path.abspath(os.path.join(dir_path,item))
             file_size = 0
             is_dir = os.path.isdir(item_path)
             file_size = os.path.getsize(item_path)
             files_info.append(
                f"- {item}: file_size={file_size} bytes, is_dir={is_dir}"
            )
        return "\n".join(files_info)

             
    except Exception as e :
           return f"Error listing files: {e}"
   


schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
    parameters=types.Schema(
        type = types.Type.OBJECT,
        properties={
            "directory": types.Schema(
                type = types.Type.STRING,
                description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
            ),
        },
    ),
)