from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.write_file import schema_write_files
from functions.run_python import schema_run_python
from collections.abc import Callable
import json

from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.run_python import run_python_file
from functions.write_file import write_file


available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python,
    schema_write_files
]

function_map: dict["string": Callable[..., str]] = {
    "get_files_info": get_files_info,
    "get_file_content": get_file_content,
    "run_python_file": run_python_file,
    "write_file": write_file,
}

def call_function(tool_call, verbose: bool = False) -> dict:
    function_name = tool_call.function.name
    function_args = json.loads(tool_call.function.arguments or "{}")
    if verbose:
        print(f" - Calling function: {function_name}({function_args})")
    print(f" - Calling function: {function_name}")
    tool_msg = {
        "role": "tool",
        "tool_call_id": tool_call.id,
    }
    if function_name not in function_map:
        tool_msg["content"] = f"Error: Unknown function: {function_name}"
        return tool_msg

    function_args["working_directory"] = "calculator"
    result = function_map[function_name](**function_args)
    tool_msg["content"] = result
    return tool_msg
