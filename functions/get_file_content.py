import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
     #Validation of working and target directories
    try:
        working_directory_path = os.path.abspath(working_directory)
        target_directory_path = os.path.normpath(os.path.join(working_directory_path, file_path))

        valid_target_directory_path = os.path.commonpath([working_directory_path, target_directory_path]) == working_directory_path
        if not valid_target_directory_path:
            return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        if not os.path.isfile(target_directory_path):
            return f'Error: File not found or is not a regular file: "{file_path}"'
        print(f'Success: "{file_path}" is within the working directory')
    except Exception as e:
        return f"Error: {e}"

    try:
        with open(target_directory_path, 'r') as f:
            file_content = f.read(MAX_CHARS)
            if f.read(1):
                file_content += f'[...File "{file_path}" truncated at {MAX_CHARS} characters]'
            return file_content
    except Exception as e:
        return f"Error: {e}"