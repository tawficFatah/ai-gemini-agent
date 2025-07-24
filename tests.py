from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from call_function import call_function

from google.genai import types

def main():
    function_call_part = types.FunctionCall(
        name="run_python_file",
        args={"file_path": "main.py"}
    )
    result_content = call_function(function_call_part, verbose=True)
    print(result_content.parts[0].function_response.response)

    function_call_part = types.FunctionCall(
        name="run_python_file",
        args={"file_path": "tests.py"}
    )
    result_content = call_function(function_call_part, verbose=True)
    print(result_content.parts[0].function_response.response)
 
    
    #result = run_python_file(working_directory="./calculator", file_path="nonexistent.py")
    #print(result)

if __name__ == "__main__":
    main()