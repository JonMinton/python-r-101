# First example from following website
# https://appsilon.com/use-r-and-python-together/#:~:text=You%20can%20import%20any%20Python,and%20functions%20declared%20with%20R.&text=And%20that's%20how%20you%20can%20run,in%20R%20and%20R%20Markdown.

import subprocess

res = subprocess.call("Rscript /Users/JonMinton/repos/python-r-101/r/script.r", shell = True)
res