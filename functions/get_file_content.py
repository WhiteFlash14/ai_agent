import os 

def get_file_content(working_directory,file_path):
    base_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(base_path,file_path))
    if not abs_file_path.startswith(base_path):
        f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    if not os.path.isfile(file_path):
        f'Error: File not found or is not a regular file: "{file_path}"'
    MAX_CHAR = 10000

    try:
        
        with open(abs_file_path,"r") as f:
             file_content_string = f.read(MAX_CHAR)
             file_content_string = file_content_string.strip()
             if len(file_content_string) == MAX_CHAR:
                content += (
                    f'[...File "{file_path}" truncated at {MAX_CHAR} characters]'
                )
        return content
        

    except Exception as e :
           return f"Error listing files: {e}"