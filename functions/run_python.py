import os
import subprocess

def run_python_file(
    working_directory: str, file_path: str, args: list[str] | None = None
) -> str:
        #Validation of working and target directories
    try:
        working_directory_path = os.path.abspath(working_directory)
        target_directory_path = os.path.normpath(os.path.join(working_directory_path, file_path))

        valid_target_directory_path = os.path.commonpath([working_directory_path, target_directory_path]) == working_directory_path
        if not valid_target_directory_path:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_directory_path):
            return f'Error: "{file_path}" does not exist or is not a regular file'
        if ".py" not in file_path:
            return f'Error: "{file_path}" is not a Python file'
        #print(f'Success: "{file_path}" is within the working directory')
    except Exception as e:
        return f"Error: {e}"

    command = ["python", target_directory_path]
    if args:
        command.extend(args)
    process = subprocess.run(command, cwd=working_directory, capture_output=True, text=True, timeout=30)
    return print_result_of_run_python(process)




def print_result_of_run_python(process: subprocess) -> str:
    try:
        result = ""
        if process.returncode != 0:
            result += f"Process exited with code {process.returncode}\n"
        if not process.stdout and not process.stderr:
            result += "No output produced"
            return result
        result += f"STDOUT:\n{process.stdout}\nSTDERR:\n{process.stderr}"
        return result
    except Exception as e:
        return f"Error: executing Python file: {e}"


schema_run_python = {
    "type": "function",
    "function": {
        "name": "run_python_file",
        "description": "Run or excecute a python file",
        "parameters": {
            "type": "object",
            "properties": {
                "file_path": {
                    "type": "string",
                    "description": "The name of the file to be excecuted, relative to the working directory (default is the working directory itself)",
                },
                "args": {
                    "type": "list[str]",
                    "description": "A list of arguments to be parameters in the given python file, the list can be empty"
                }
            },
        },
    },
}

