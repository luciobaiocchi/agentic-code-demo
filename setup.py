import sys
import os
from google.genai import types
from google import genai

def setup():
    # 
    # 
    # We won't allow the LLM to specify the working_directory parameter. 
    # We're going to hard code that.
    #
    #
    schema_get_files_info = types.FunctionDeclaration(
        name="get_files_info",
        description="Lists files in the specified directory along with their sizes, constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "directory": types.Schema(
                    type=types.Type.STRING,
                    description="The directory to list files from, relative to the working directory. If not provided, lists files in the working directory itself.",
                ),
            },
        ),
    )
    schema_get_file_content = types.FunctionDeclaration(
        name="get_file_content",
        description="Lists the content of a file in the specified directory, constrained to the working directory, with a maximum of character (default = 10000).",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path of the file to read, relative to the working directory (e.g., 'main.py').",
                ),
            },
            required=["file_path"]
        ),
    )
    schema_run_python_file = types.FunctionDeclaration(
        name="run_python_file",
        description="Runs a Python file (and only that type of file) with optional arguments. All paths are constrained to the working directory.",
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema(
                    type=types.Type.STRING,
                    description="The path to the Python file to execute, relative to the working directory (e.g., 'main.py' or 'scripts/my_script.py')."
                ),
                "args": types.Schema(
                    type=types.Type.ARRAY,
                    items=types.Schema(type=types.Type.STRING),
                    description="Optional. A list of command-line arguments to pass to the script (e.g., ['--verbose', 'input.txt'])."
                )
            },
            # This tells the model it MUST provide a file_path
            required=["file_path"] 
        ),
    )

    schema_write_file = types.FunctionDeclaration(
        name="write_file",  # <-- FIX 1: Name must match your Python function
        description="Writes new content to a specified file, overwriting the file if it already exists. All paths are constrained to the working directory.", # <-- FIX 2: Correct description
        parameters=types.Schema(
            type=types.Type.OBJECT,
            properties={
                "file_path": types.Schema( # <-- FIX 3: Must ask for file_path
                    type=types.Type.STRING,
                    description="The path of the file to write, relative to the working directory (e.g., 'new_script.py' or 'data/output.txt')."
                ),
                "content": types.Schema( # <-- FIX 4: Must ask for content
                    type=types.Type.STRING,
                    description="The new content to be written to the file."
                )
            },
            required=["file_path", "content"] # Ensure the AI provides both
        ),
    )

    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
            schema_get_file_content,
            schema_run_python_file,
            schema_write_file
        ]
    )
    
    #we insert the functions that the model can use
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories
    - Read file contents
    - Execute Python files with optional arguments
    - Write or overwrite files

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
    
    return config