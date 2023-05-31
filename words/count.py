import re

txt = "content.txt"
f = open(txt,mode="r")

content = f.read()

result = "".join(re.findall(r'\w+', content))

print(len(result))
f.close()