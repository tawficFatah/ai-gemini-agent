import os

def write_file(working_directory : str, file_path : str, content: str) -> str:
    """Writes content to the given file.

    Args:
        working_directory (str): The directory the agent is granted access to. The agent is not allowed
        to access or modify anything outside this directory.

        file_path (str): The file's path.

    Returns:
        str: Successfully wrote to "{file_path}" (content's size) characters written)
            If we were able to write the file.

            If the provided `file_path` is outside the permitted `working_directory`,
            returns an error message:
            'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'

    """
    # Before trying to read the file, let's check if we have:
    # 
    # A valid working directory
    abs_working_directory = os.path.abspath(working_directory)
    
    if  not os.path.isdir(working_directory):
        return f'Error: "{working_directory}" is not a directory'

    file_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    # The file is within the working directory
    if  not file_full_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    try:
        # If the file_path doesn't exist, create it
        file_directory = os.path.dirname(file_full_path)
        if not os.path.exists(file_directory):
            os.makedirs(file_directory, exist_ok=True)
    except Exception as error:
        return f"Error: creating directory: {error}"
    
    if os.path.exists(file_full_path) and os.path.isdir(file_full_path):
        return f'Error: "{file_path}" is a directory, not a file'
    
    try:
        with open(file_full_path, "w") as file:
            file.write(content)
            
        return (
            f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
        )
    except Exception as error:
        return f"Error: writing to file: {file_path} {error}"