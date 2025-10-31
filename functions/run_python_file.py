import os
import subprocess
import pathlib
from functions.config import TIME_OUT_AGENT


def run_python_file(working_directory, file_path, args=[]):
    abs_workdir = os.path.abspath(working_directory)
    abs_target = os.path.abspath(os.path.join(working_directory, file_path))

    if args is None:
        args = []
        
    if not abs_target.startswith(abs_workdir):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    if not os.path.exists(abs_target):
        return f'Error: File "{file_path}" not found.'
    if pathlib.Path(file_path).suffix != ".py":
        return f'Error: "{file_path}" is not a Python file.'
        
    cmd = ["python3", abs_target] + args

    try:
        result = subprocess.run(
            cmd,
            cwd=abs_workdir,
            timeout=TIME_OUT_AGENT,
            capture_output=True,
            text=True
        )
        return {
            "returncode": result.returncode,
            "STDOUT:": result.stdout,
            "stderr": result.stderr
        }

    except subprocess.TimeoutExpired:
        return {"error": f"Execution timed out after {TIME_OUT_AGENT} seconds."}
    except Exception as e:
        return {"error": str(e)}