from google.genai import types

# ------------------------------------------------------------------------------
# FunctionDeclaration: get_files_info
# Documentation: https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration
# ------------------------------------------------------------------------------
schema_get_files_info = types.FunctionDeclaration(
    name="get_files_info",
    description="""
    Lists files in the specified directory along with their sizes, constrained to
    the working directory.

    This function is designed for use with the Google GenAI SDK function calling system.
    It returns file metadata such as file name and size for a given directory.

    - **Parameter:**
        - `directory` (string, optional): Relative path to the target directory. 
          If not provided, lists files from the current working directory.

    Link to FunctionDeclaration docs:
    https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration
    """,
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "directory": types.Schema(
                type = types.Type.STRING,
                description="""
                The directory to list files from, relative to the working directory.

                If not provided, the function will default to listing the contents
                of the working directory.

                This parameter enhances safety by not allowing traversal outside
                the predefined scope.

                """,            ),
        },
    ),
)

# ------------------------------------------------------------------------------
# Tool: available_functions
# Documentation: https://googleapis.github.io/python-genai/genai.html#genai.types.Tool
# ------------------------------------------------------------------------------
available_functions = types.Tool(
    function_declarations = [
        schema_get_files_info,
    ]
)
"""
Tool containing function declarations for use with GenAI function calling.

This tool currently includes:

- `get_files_info`: Lists files and their sizes in a given directory, optionally specified.

Can be used as part of the `tools` argument in a `model.generate_content(...)` call.

Tool docs:
https://googleapis.github.io/python-genai/genai.html#genai.types.Tool

Also see:
GenerateContentResponse.function_calls:
https://googleapis.github.io/python-genai/genai.html#genai.types.GenerateContentResponse.function_calls
"""