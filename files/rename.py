# Batch Rename file : original: 2019-01-03-HelloWorld.md => new: HelloWorld.md
import glob
import re
import os

folder = ""
filelists = glob.glob("./{}/*.md".format(folder))

# regex pattern
pattern = r'\d\d\d\d-\d\d-\d\d-'

for process in filelists:
    original = process
    new = re.sub(pattern, "", process)
    # for debug: you can check file name before you rename file. 
    print(f"original {original} => new {new}")  
    # os.rename(original, new)
