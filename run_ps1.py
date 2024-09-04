import subprocess
import os

def run_powershell_script():
    # Define the path to your PowerShell script
    ps_script_path = os.path.join(os.getcwd(), "example.ps1")

    # Build the command to run the PowerShell script.
    command = ["powershell.exe", "-ExecutionPolicy", "Bypass", "-File", ps_script_path]

    try:
        # Run the command
        result = subprocess.run(command, capture, capture_output=True, text=True, check=True)
        print("Output:\n", result.stdout)
        print("Errors:\n", result.stderr)
    except subprocess.CalledProcessError as e:
        print(f"Error executing PowerShell script: {e}")

if __name__ == "__main__":
    run_powershell_script()