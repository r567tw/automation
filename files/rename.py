# 講檔名改成去除日期的

import glob
import re
import os

filelists = glob.glob("./*.md")

# regex pattern
pattern = r'\d\d\d\d-\d\d-\d\d-'

for process in filelists:
    original = process
    new = re.sub(pattern, "", process)
    print(f"original {original} => new {new}")  # for debug: you can check file name before you rename file
    # os.rename(original, new)
