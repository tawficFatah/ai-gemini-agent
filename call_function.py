from google.genai import types

from functions.schema_files import schema_get_files_info
from functions.schema_files import schema_get_file_content
from functions.schema_files import schema_run_python_file
from functions.schema_files import schema_write_file

# ------------------------------------------------------------------------------
# Tool: available_functions
# Documentation: https://googleapis.github.io/python-genai/genai.html#genai.types.Tool
# ------------------------------------------------------------------------------
available_functions = types.Tool(
    function_declarations = [
        schema_get_files_info,
        schema_get_file_content,
        schema_run_python_file,
        schema_write_file,
    ]
)
"""
Tool containing function declarations for use with GenAI function calling.

This tool currently includes:

- `get_files_info`: Lists files and their sizes in a given directory, optionally specified.

- `get_file_content`: Gets the contents of a file up to MAX_CHARS to avoid files that are too long.

- `run_python_file`: Runs the file referenced in file_path in the working_directory.

- `write_file`: Writes content to the given file.
  
Can be used as part of the `tools` argument in a `model.generate_content(...)` call.

Tool docs:
https://googleapis.github.io/python-genai/genai.html#genai.types.Tool

Also see:
GenerateContentResponse.function_calls:
https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.function_calls
"""