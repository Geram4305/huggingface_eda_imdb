import subprocess
import sys

# Create a virtual environment
subprocess.run(["python", "-m", "venv", "venv"])

# Activate the virtual environment
try:
    subprocess.run(["source","venv/bin/activate"])
    
except:
    subprocess.run(["/bin/bash","-c" ,"source venv/bin/activate"])

#Run requirements
result = subprocess.run(["pip", "install", "-r", "requirements.txt"], capture_output=True, text=True)
print(result.stderr)