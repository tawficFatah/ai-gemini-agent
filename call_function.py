from google.genai import types

from functions.schema_files import schema_get_files_info
from functions.schema_files import schema_get_file_content
from functions.schema_files import schema_run_python_file
from functions.schema_files import schema_write_file

from functions.get_file_content import get_file_content
from functions.get_files_info   import get_files_info
from functions.run_python_file  import run_python_file
from functions.write_file       import write_file

from config import WORKING_DIR
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

def call_function(function_call_part: types.FunctionCall, verbose: bool = False): 
    """Used by the AI agent to call a function.

    Args:
        function_call_part (types.FunctionCall): The function to call. It has
            A .name property (the name of the function, a string)
            A .args property (a dictionary of named arguments to the function)
            
        If verbose is specified, it prints the function name and args like:
            print(f"Calling function: {function_call_part.name}({function_call_part.args})")
        otherwise
            print(f" - Calling function: {function_call_part.name}")

    Returns:
        The output of the called funtion if it's valid.
        Otherwise:
            types.Content indicating an error when calling the function.

    """
    name = function_call_part.name
    args = function_call_part.args

    if verbose:
        print(f" - Calling function: {name}({args})")
    else:
        print(f" - Calling function: {name}")

    # Map from function name string to actual implementation
    functions = {
        "get_files_info": get_files_info,
        "get_file_content": get_file_content,
        "run_python_file": run_python_file,
        "write_file": write_file,
    }

    if name not in functions:
        return types.Content(
            role = "tool",
            parts= [
                types.Part.from_function_response(
                    name = name,
                    response = {"error": f"Unknown function: {name}"},
                )
            ],
        )

    # Adding the working directory to args. Let's do it in a safe way, just in case
    args = dict(args)  # Make a shallow copy before mutating
    args["working_directory"] = WORKING_DIR

    function_to_call = functions.get(name)
    
   # Call the function with unpacked arguments and capture the response
    function_result = function_to_call(**args)

    # Return the result wrapped in a types.Content
    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name = name,
                response={"result": function_result},
            )
        ],
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