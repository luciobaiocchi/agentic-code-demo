import os

# Implementation of a safe directory listing
#
# ================= PARAMS ===========================================
# working_directory = the root folder you allow the function to access, the "sandbox"
# directory = subfolder inside working dir
#
# ================= RETURNS ==========================================
#

def get_files_info(working_directory, directory="."):
    abs_workdir = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, directory))

    if not abs_target.startswith(abs_workdir):
        print(f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
        return

    print(f"Listing files in: {abs_target}")

    # Try to list directory contents
    try:
        lines = []
        for entry in os.listdir(abs_target):
            full_path = os.path.join(abs_target, entry)
            is_dir = os.path.isdir(full_path)
            file_size = os.path.getsize(full_path)
            lines.append(f"- {entry}: file_size={file_size} bytes, is_dir={is_dir}")
        return "\n".join(lines)

    except Exception as e:
        return f"Error accessing directory: {e}"

# Example usage
# get_files_info("/home/user/project", "subdir")
