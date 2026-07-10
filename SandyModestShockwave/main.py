import os
import wget
import subprocess
name = input("Enter a folder name: ")
print(os.getcwd())
os.system('mkdir ' + name)
os.chdir("/home/runner/SandyModestShockwave/"+name)
print(os.getcwd())

#wget.download("https://github.com/playit-cloud/playit-minecraft-plugin/releases/latest/download/playit-minecraft-plugin.jar")
wget.download("https://raw.githubusercontent.com/EXALAB/AnLinux-Resources/master/Scripts/Installer/Ubuntu/ubuntu.sh")
subprocess.run(["bash", "ubuntu,sh"], 
   capture_output=True)