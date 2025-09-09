import os
import subprocess
from google.genai import types

def run_python_file(working_directory, file_path):
    abs_working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(abs_working_dir):
        return f'Error: "{file_path}" is not in the working directory'

    if not os.path.isfile(abs_file_path):
        return f"Error: {file_path} is not a file"

    if not file_path.endswith('.py'):
        return f"Error: {file_path} is not a python file"

    try:
        output = subprocess.run(["python3", file_path],
                              cwd=abs_working_dir,
                              timeout=30,
                              capture_output=True)
        return output
    except Exception as e:
        return f"Error executing {file_path}  {e}"

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Runs a python file with the python3 interpreter",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        properties={
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="The path of the file to run relative to the working directory",
            ),
        },
    ),
)



