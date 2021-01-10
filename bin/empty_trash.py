#!/Library/Frameworks/Python.framework/Versions/3.8/bin/python3
import os

os.chdir("/users/davidorvek/Trash")
for file in os.listdir("/users/davidorvek/Trash"):
    os.remove(file)
