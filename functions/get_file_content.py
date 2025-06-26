import os
from config import MAX_CHARS

def get_file_content(working_directory: str, file_path: str) -> str:
    """Gets the contents of a file up to MAX_CHARS to avoid files that are too long, i.e. expensive.
    
    Args:
        working_directory (str): The directory the agent is granted access to. The agent is not allowed
        to access or modify anything outside this directory.

        file_path (str): The file's path.

    Returns:
        str: The contents of the file up to a predetermined MAX chracters length.
        
        If the provided `file_path` is outside the permitted `working_directory`, returns an error
        message: 'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

        If the provided `file_path` is not a file, returns an error message:
            'Error: File not found or is not a regular file: "{file_apth}"'
    """
    TRUNCATION_NOTICE = f'[...File "{file_path}" truncated at 10000 characters]'

    # Before trying to read the file, let's check if we have:
    # 
    # A valid working directory
    abs_working_directory = os.path.abspath(working_directory)
    
    if  not os.path.isdir(working_directory):
        return f'Error: "{working_directory}" is not a directory'

    file_full_path = os.path.abspath(os.path.join(working_directory, file_path))
    
    # The file is within the working directory
    if  not file_full_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'

    # And the file is an actual file
    if not os.path.isfile(file_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(file_full_path, "r", encoding="utf-8") as file:
            file_contents = file.read(MAX_CHARS)
            
            # Check if the file has been truncated by trying to read one more character
            if file.read(1):
                file_contents += TRUNCATION_NOTICE

        return file_contents
    except Exception as error:
        return f'Error: Cant read file: "{file_path}: {error}"'