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
# FunctionDeclaration: get_file_content
# Documentation: https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration
# ------------------------------------------------------------------------------
schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="""
    Gets the contents of a file up to MAX_CHARS to avoid files that are too long, i.e. expensive.
    - **Parameter:**
        - `directory` (string): Relative path to the target directory. 
          If not provided, lists files from the current working directory.
          
        - `file_path` (string): The file's path.

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

                """),
            "file_path": types.Schema(
                type = types.Type.STRING,
                description="""
                The file's path
                """),
        },
        required = ["file_path"],
    ),
)

# ------------------------------------------------------------------------------
# FunctionDeclaration: run_python_file
# Documentation: https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration
# ------------------------------------------------------------------------------
schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="""
    Runs the file referenced in file_path in the working_directory.
    - **Parameter:**
        - `working_directory` (string): Relative path to the target directory. 
          
        - `file_path` (string): The file's path.
        
        - `args` (string, optional): any arguments used to run the file.

    Link to FunctionDeclaration docs:
    https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration
    """,
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "working_directory": types.Schema(
                type = types.Type.STRING,
                description="""
                The directory the agent is granted access to.
                """),
            "file_path": types.Schema(
                type = types.Type.STRING,
                description="""
                The file's path.
                """),
            "args": types.Schema(
                type = types.Type.STRING,
                description="""
                Any arguments required to run the file.
                """),
        },
        required = ["file_path"],
    ),
)

# ------------------------------------------------------------------------------
# FunctionDeclaration: write_file
# Documentation: https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration
# ------------------------------------------------------------------------------
schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="""
    Writes content to the given file.
    - **Parameter:**
        - working_directory (str): The directory the agent is granted access to. The agent is not allowed
        to access or modify anything outside this directory.

        - file_path (str): The file's path.
        
        - content (str): The content of the file.

    Link to FunctionDeclaration docs:
    https://googleapis.github.io/python-genai/genai.html#genai.types.FunctionDeclaration
    """,
    parameters = types.Schema(
        type = types.Type.OBJECT,
        properties = {
            "working_directory": types.Schema(
                type = types.Type.STRING,
                description="""
                The directory the agent is granted access to.
                """),
            "file_path": types.Schema(
                type = types.Type.STRING,
                description="""
                The file's path.
                """),
            "content": types.Schema(
                type = types.Type.STRING,
                description="""
                The content of the file.
                """),
        },
        required = ["file_path", "content"],
    ),
)
