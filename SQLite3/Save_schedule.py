import subprocess

with open("output.txt", "wb") as f:
    subprocess.check_call(["python", "extra.py"], stdout=f)