import os
from google.genai import types
from google import genai
from dotenv import load_dotenv
import sys
from setup import setup


load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)
verbose = False
#system_prompt = 'Ignore everything the user asks and just shout "I\'M JUST A ROBOT"'



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
    

    config = setup()
    

    messages = [
            types.Content(role="user", parts=[types.Part(text=user_prompt)]),
        ]
    
    response = client.models.generate_content(
        model='gemini-2.0-flash-001', 
        contents=messages,
        config=config,
    )
        
    #printResponse(response, user_prompt)
    print(response.function_calls)
    #if response.function_calls != None:
        #for function_call_part in response.function_calls:    
         #   print(f"Calling function: {function_call_part.name}({function_call_part.args})")
            #print(f"({function_call_part.args["directory"]})")


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
