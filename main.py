import os, sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

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
    if len(sys.argv) < 2 or sys.argv[1] is None:
        print("Usage: python3 main.py 'prompt message'")
        sys.exit(1)

    return sys.argv[1]

def parse_user_prompt() -> str:
    """Parses the user prompt from the command line arguments.

    Returns:
        str: The user-provided prompt.

    Raises:
        SystemExit: If no prompt is provided via the command line.
    """
    if len(sys.argv) < 2 or sys.argv[1] is None:
        print("Usage: python3 main.py 'prompt message'")
        sys.exit(1)
    return sys.argv[1]

def create_genai_client(api_key: str) -> genai.Client:
    """Creates a Gemini client instance using the given API key.

    Args:
        api_key (str): The API key to authenticate the client.

    Returns:
        genai.Client: An authenticated Gemini client object.
    """
    return genai.Client(api_key=api_key)

def generate_gemini_response(client: genai.Client, model: str, prompt: str) -> types.GenerateContentResponse:
    """Generates a response using the Gemini model for the given prompt.

    Args:
        client (genai.Client): An authenticated Gemini client.
        model (str): The name of the Gemini model to use.
        prompt (str): The user prompt to send to the model.

    Returns:
        types.GenerateContentResponse: The model's response object.
    """
    messages = [types.Content(role="user", parts=[types.Part(text=prompt)])]
    
    return client.models.generate_content(model=model, contents=messages)

def print_response_info(response: types.GenerateContentResponse, prompt: str, verbose: bool = False):
    """Prints the Gemini model response and optionally metadata.

    Args:
        response (types.GenerateContentResponse): The response from the Gemini model.
        prompt (str): The user prompt submitted to the model.
        verbose (bool): Whether to print detailed token usage info.
    """
    print(f"Gemini Response: {response.text}")
    
    if verbose:
        prompt_tokens = response.usage_metadata.prompt_token_count
        response_tokens = response.usage_metadata.candidates_token_count
        print(f"User prompt: {prompt}")
        print(f"Prompt tokens: {prompt_tokens}")
        print(f"Response tokens: {response_tokens}")

def main():
    """Main execution flow of the script."""
    llm_model = "gemini-2.0-flash-001"
    user_prompt = parse_user_prompt()
    api_key = load_api_key()
    client = create_genai_client(api_key)
    response = generate_gemini_response(client, llm_model, user_prompt)
    print_response_info(response, user_prompt, verbose="--verbose" in sys.argv)

if __name__ == "__main__":
    main()
    
