import os

def get_files_info(working_directory: str, directory: str = None) -> str:
    """Builds and returns a string representing the contents of a directory.

    Args:
        working_directory (str): The directory the agent is granted access to. The agent is not allowed
        to access or modify anything outside this directory.

        directory (str): The target directory to retrieve metadata from. If None, defaults to the working_directory.

    Returns:
        str: A formatted string representing the contents of the directory, where each line includes
        the file or directory name, its size, and whether it is a directory. Format:
            - README.md: file_size=1032 bytes, is_dir=False
            - src: file_size=128 bytes, is_dir=True
            - package.json: file_size=1234 bytes, is_dir=False

        If the provided `directory` is outside the permitted `working_directory`, returns an error message:
            'Error: Cannot list "{directory}" as it is outside the permitted working directory'

        If the provided `directory` path is not a directory, returns an error message:
            'Error: "{directory}" is not a directory'
    """

    # First, let's check if the working direcotry is valid
    # if working_directory is invalid, return an error string
    target_directory = working_directory if not directory or directory == "." else os.path.join(working_directory, directory)
    try:
        if  not os.path.isdir(os.path.abspath(working_directory)):
            return f'Error: "{working_directory}" is not a directory'

        # Next, let's check if the provided directotry is a directory
        if  not os.path.isdir(os.path.abspath(target_directory)):
            return f'Error: "{directory}" is not a directory'
    except Exception as error:
        return f"Error: {error}"

    # If both directories are valid, we need to verify that the target directory is within
    # the working directory.
    target_dir_abspath  = os.path.abspath(target_directory)
    working_dir_abspath = os.path.abspath(working_directory)

    if not target_dir_abspath.startswith(working_dir_abspath):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'

    files = get_list_of_dirs(target_directory)
 
    files_info = []
    
    for file in files:
        file_full_path = os.path.join(target_directory, file)

        files_info.append(get_file_info(file, file_full_path))

    files_info_str = "\n".join(files_info)
    
    return files_info_str

def get_list_of_dirs(working_directory: str) -> [str]:
    """Returns a list of strings representing the directories and/or files under the
    working_directory.

    Args:
        working_directory (str): The directory the agent is granted access to.

    Returns:
        [str]: A list of directories / files under the working_directory.

    """
    try:
        dir_abs_path = os.path.abspath(working_directory)
        return os.listdir(path=dir_abs_path)
    except Exception as error:
        return f"Error: {error}"
    
def get_file_info(file_name: str, file_path: str) -> str:
    """Returns a string representing file/directory information.
    Args:
        file_name (str): name of the file/directory
        working_directory (str): The initial directory.

    Returns:
        str: file/dir information in the following format:
            - file_name: file_size={file_size} bytes, is_dir={True / False}
    """

    # We're assuming the path is valid, i.e. it's been verified by the calling
    # function.
    file_size = os.path.getsize(file_path)
    
    is_dir = os.path.isdir(file_path)
    file_info_str = f"- {file_name}: file_size={file_size} bytes, is_dir={is_dir}"
    
    return file_info_str