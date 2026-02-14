import subprocess
import os
import shlex

def run_command(user_input):
    """Run a shell command from user input."""
    args = shlex.split(user_input)
    subprocess.call(args, check=False)

API_KEY = os.getenv("API_KEY")
