from functions.get_file_content import schema_get_file_content
from functions.get_files_info import schema_get_files_info
from functions.write_file import schema_write_files
from functions.run_python import schema_run_python


available_functions = [
    schema_get_files_info,
    schema_get_file_content,
    schema_run_python,
    schema_write_files
]