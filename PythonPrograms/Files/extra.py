#------------------------------------------------Write output in other File --------------------------------------------
import subprocess

with open("output.txt", "wb") as f:
    subprocess.check_call(["python", "CreatingTextFile.py"], stdout=f)