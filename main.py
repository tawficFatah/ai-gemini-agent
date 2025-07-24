import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from config import SYSTEM_PROMPT

from call_function import (call_function, available_functions)

def load_api_key() -> str:
    """Loads the Gemini API key from the environment variables.

    Returns:
        str: The API key string.

    Raises:
        SystemExit: If the API key is not found in the environment.
    """
    load_dotenv()
    
    api_key = os.environ.get("GEMINI_API_KEY")
    
    if not api_key:
        print("Error: GEMINI_API_KEY not found in environment variables.")
        sys.exit(1)
        
    return api_key

def parse_user_prompt() -> str:
    """Parses the user prompt from the command line arguments.

    Returns:
        str: The user-provided prompt.

    Raises:
        SystemExit: If no prompt is provided via the command line.
    """
    verbose = "--verbose" in sys.argv
    args = []
    
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)

    if not args:
        print("AI Code Assistant")
        print('\nUsage: python main.py "your prompt here" [--verbose]')
        print('Example: python main.py "How do add a function to the calculator?"')
        sys.exit(1)
    
    user_prompt = " ".join(args)
    
    if verbose:
        print(f"User prompt: {user_prompt}\n")

    return user_prompt

def create_genai_client(api_key: str) -> genai.Client:
    """Creates a Gemini client instance using the given API key.

    Args:
        api_key (str): The API key to authenticate the client.

    Returns:
        genai.Client: An authenticated Gemini client object.
    """
    return genai.Client(api_key=api_key)

def generate_gemini_response(client: genai.Client, user_prompt: str, verbose: bool):
    """Generates a response using the Gemini model for the given prompt.

    Args:
        client (genai.Client): An authenticated Gemini client.
        prompt (str): The user prompt to send to the model.
        verbose (boolean): Used tp print extra info
        
    Returns:
        types.GenerateContentResponse: The model's response object.
    """
    llm_model = "gemini-2.0-flash-001"

    messages = [types.Content(role="user", parts=[types.Part(text = user_prompt)])]

    response = client.models.generate_content(
        model       = llm_model,
        contents    = messages,
        config      = types.GenerateContentConfig(
            tools = [available_functions], system_instruction = SYSTEM_PROMPT
        ),
    )

    if verbose:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)

    if not response.function_calls:
        return response.text

    function_responses = []
    
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part, verbose)
        if (
            not function_call_result.parts
            or not function_call_result.parts[0].function_response
        ):
            raise Exception("empty function call result")
        if verbose:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result.parts[0])

    if not function_responses:
        raise Exception("no function responses generated, exiting.")

def main():
    """Main execution flow of the script."""
    user_prompt = parse_user_prompt()
    api_key = load_api_key()
    client = create_genai_client(api_key)

    is_verbose : bool = "--verbose" in sys.argv
    
    generate_gemini_response(client, user_prompt, is_verbose)

if __name__ == "__main__":
    main()
    
