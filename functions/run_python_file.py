import os
import subprocess

def run_python_file(working_directory : str, file_path : str, args : str =None) -> str:
    """Runs the file referenced in file_path in the working_directory.
    
    Args:
        working_directory (str): The directory the agent is granted access to. The agent is not allowed
        to access or modify anything outside this directory.

        file_path (str): The file's path.

    Returns:
        
        If the provided `file_path` is outside the permitted `working_directory`, returns an error
        message: 'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        If the provided `file_path` does not exist, returns an error message:
            'Error: File "{file_path}" not found.'
            
        If the provided `file_path` does not end with ".py", return an error message:
            'Error: "{file_path}" is not a python file.'
    """
    # Before trying to read the file, let's check if we have:
    # 
    # A valid working directory
    abs_working_directory = os.path.abspath(working_directory)
    
    if  not os.path.isdir(working_directory):
        return f'Error: "{working_directory}" is not a directory'

    file_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    # The file is within the working directory
    if not file_full_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    # The file is an actual file
    if not os.path.isfile(file_full_path):
        return f'Error: File "{file_path}" not found.'
    
    # And the file is an actual python file.
    if not file_full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'
    
    # If we made it here, we can run the file


    try:
        # Command to run (as a list)
        command = ["python", file_full_path]

        if args:
            command.extend(args)

        # Run the command
        result = subprocess.run(
            command,
            capture_output=True,        # captures both stdout and stderr
            text=True,                  # decodes bytes to string
            cwd=abs_working_directory  # working directory
        )
        
        output = []
        
        if result.stdout:
            output.append(f"STDOUT:\n{result.stdout}")

        if result.stderr:
            output.append(f"STDERR:\n{result.stderr}")
        
        if result.returncode != 0:
            output.append(f"Process exited with code {result.returncode}")
            
        return "\n".join(output) if output else "No output produced."
    except Exception as error:
        return f"Error: executing Python file: {error}"