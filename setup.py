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
    
    available_functions = types.Tool(
        function_declarations=[
            schema_get_files_info,
        ]
    )
    
    system_prompt = """
    You are a helpful AI coding agent.

    When a user asks a question or makes a request, make a function call plan. You can perform the following operations:

    - List files and directories

    All paths you provide should be relative to the working directory. You do not need to specify the working directory in your function calls as it is automatically injected for security reasons.
    """
    
    config=types.GenerateContentConfig(
        tools=[available_functions], system_instruction=system_prompt
    )
    
    return config