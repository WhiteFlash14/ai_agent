import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    base_path = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(base_path,file_path))
    if not abs_file_path.startswith(base_path):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_file_path):
        return f'Error: File "{file_path}" not found.'
    if not abs_file_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    try:
        result = subprocess.run(["python3",abs_file_path],capture_output=True,cwd = base_path,timeout=30,check=True,text=True)
        # print(f"STDOUT:{result.stdout}")
        # print(f"STDERR:{result.stderr}")
    #     if result.stdout == None:
    #        return "No output produced"
    # except subprocess.CalledProcessError as e:
    #     print(f"Process exited with code {e.returncode}")
        output = []
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")
        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")

        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")

        return "\n".join(output) if output else "No output produced."

        
    except Exception as e:
        return f"Error: executing Python file: {e}"
    





schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Executes a specified Python file within the permitted working directory. Returns the standard output and error produced by the script, as well as the process exit code if it is nonzero. Returns an error if the file is outside the working directory, does not exist, or is not a Python file.",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path to the Python file to execute, relative to the working directory.",
            ),
        },
    ),
)