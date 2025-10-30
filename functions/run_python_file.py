import os

def run_python_file(working_directory, file_path, args=[]):
    abs_workdir = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_target.startswith(abs_workdir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

    
    # Try to list file content
    try:
        with open(abs_target, "w") as f:
            f.write(abs_target)
        return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'


    except Exception as e:
        return f'Error: File not found or is not a regular file: "{abs_target}"'