import os
from functions.config import MAX_CHARS

# Implementation of a safe directory listing
#
# ================= PARAMS ===========================================
# working_directory = the root folder you allow the function to access, the "sandbox"
# file_path = file_path inside working dir
#
# ================= RETURNS ==========================================
#
def get_file_content(working_directory, file_path):
    abs_workdir = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target.startswith(abs_workdir):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        
    
    # Try to list file content
    try:
        if (os.path.isfile(abs_target)):
            with open(abs_target, "r") as f:
                file_content_string = f.read(MAX_CHARS)
                total_chars = len(f.read()) + len(file_content_string)  # total chars in file
        if (total_chars > MAX_CHARS):
                file_content_string += f"\n[...File '{file_path}' truncated at {MAX_CHARS} characters]"
        return file_content_string


    except Exception as e:
        return f'Error: File not found or is not a regular file: "{file_path}"'


