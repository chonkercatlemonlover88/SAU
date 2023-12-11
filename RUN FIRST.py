import subprocess
import sys

def install(package):
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])

packages = ["numpy", "scipy"]

for package in packages:
    install(package)
