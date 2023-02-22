import os

# specify the file name
file_path = '/home/james/Downloads/HN-2022-GC-002.pdf'

print('file_path')

if os.path.isfile(file_path):
    os.remove(file_path)
    print('The file is successfully deleted')
else:
    print('The file is not found')