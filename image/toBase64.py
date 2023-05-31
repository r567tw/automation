import base64
import subprocess

img_path = 'images/1.png'

with open(img_path, 'rb') as f:
    image_data = f.read()
    base64_data = str(base64.b64encode(image_data))  # base64編碼

    # f = open("base64.txt","wb")
    # f.write(base64_data)
    # f.close()

    subprocess.run("pbcopy", text=True, input=base64_data)

    print("Finished")

    # print(base64_data)
