import os

def get_files_info(working_directory: str, directory: str = ".") -> str:
    #Validation of working and target directories
    try:
        working_directory_path = os.path.abspath(working_directory)
        target_directory_path = os.path.normpath(os.path.join(working_directory_path, directory))

        valid_target_directory_path = os.path.commonpath([working_directory_path, target_directory_path]) == working_directory_path
        if not valid_target_directory_path:
            return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
        if not os.path.isdir(target_directory_path):
            return f'Error: "{directory}" is not a directory'
        #print(f'Success: "{directory}" is within the working directory')
    except Exception as e:
        return f"Error: {e}"

    #Getting files info
    try:
        file_info_list = []

        for file in os.listdir(target_directory_path):
            file_path = os.path.join(target_directory_path, file)
            file_info_list.append(f"- {file}: file_size={os.path.getsize(file_path)} bytes, is_dir={os.path.isdir(file_path)}")
        return "\n".join(file_info_list)
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
