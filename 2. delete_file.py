import os

file_path = '/home/james/Downloads/ProPlus2021Retail.img'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("The file is successfully deleted.")
else:
    print("The file is NOT FOUND.")