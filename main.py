import os
from google.genai import types
from google import genai
from dotenv import load_dotenv
import sys
import get_files_info from functions

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
verbose = False

def main():
    global verbose
    pop = sys.argv.pop() 
    if (pop == "--verbose"):
        verbose = True
        user_prompt = sys.argv.pop()
        print(user_prompt)
    else:
        user_prompt = pop

    #print("Digitare -q per uscire")
    #print("user:", end="")
    #user_prompt = input()
    #print("\n")
    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', contents=messages
    )
        
    printResponse(response, user_prompt)
        
    '''while user_prompt!= '-q':
        messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
        response = client.models.generate_content(
            model='gemini-2.0-flash-001', contents=messages
        )
        
        printResponse(response, user_prompt)
        user_prompt = input()
    '''
    #print("\nSOME STATS:\n")
    #print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
    #print("Response tokens: " + str(response.usage_metadata.candidates_token_count))

def printResponse(response, user_prompt):
    if (verbose):
        print("User prompt: " + user_prompt)
        print("Prompt tokens: " + str(response.usage_metadata.prompt_token_count))
        print("Response tokens: " + str(response.usage_metadata.candidates_token_count))
        print("Model Response:" + response.text)
        #print("user:", end="")
    else:
        print("model:" + response.text, end="")
        #print("user:", end="")
    

    
    
    

if __name__ == "__main__":
    main()
