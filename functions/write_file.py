import os

def write_file(working_directory: str, file_path: str, content: str) -> str:
    #Validation of working and target directories
    try:
        working_directory_path = os.path.abspath(working_directory)
        target_directory_path = os.path.normpath(os.path.join(working_directory_path, file_path))

        valid_target_directory_path = os.path.commonpath([working_directory_path, target_directory_path]) == working_directory_path
        if not valid_target_directory_path:
            return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
        if os.path.isdir(target_directory_path):
            return f'Error: Cannot write to "{file_path}" as it is a directory'
        print(f'Success: "{file_path}" is within the working directory')
    except Exception as e:
        return f"Error: {e}"

    try:
        os.makedirs(os.path.dirname(target_directory_path), exist_ok=True)
        with open(target_directory_path, 'w') as f:
            f.write(content)
            return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
    except Exception as e:
        return f"Error: {e}"



schema_get_files_info = {
    "type": "function",
    "function": {
        "name": "get_files_info",
        "description": "Lists files in a specified directory relative to the working directory, providing file size and directory status",
        "parameters": {
            "type": "object",
            "properties": {
                "directory": {
                    "type": "string",
                    "description": "Directory path to list files from, relative to the working directory (default is the working directory itself)",
                },
            },
        },
    },
}