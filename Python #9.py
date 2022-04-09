import os

print(os.getcwd()) # Get Current Working Directory (returns the path to the current folder)

os.chdir('..') # Change Directory (change to a different folder, can take an absolute path or a relative path)

# .        - the current directory
# ..       - go back one directory
# ../..    - go back 2 directories
# ../../.. - go back 3 directories etc

print(os.getcwd())

print(os.listdir()) # List the directory

py_count = 0
folder_count = 0
xls_count = 0

# Loop through every sub-folder in Coding
for dir in os.listdir():
    if dir[0] != '.': # skip hidden directories
        os.chdir(dir) # change directory to the next sub-folder
        print(os.getcwd()) # print which sub-folder we are in
        for item in os.listdir(): # check what is in the sub-folder and update our counters
            if os.path.isdir(item): # check if the item is a directory
                folder_count += 1
            elif os.path.isfile(item): # check if the item is a file
                
                # splitext means split extention, the 0th element is the filename, the 1st is the extention
                if os.path.splitext(item)[1] == '.py': 
                    py_count += 1
                elif os.path.splitext(item)[1] == '.xls':
                    xls_count += 1

        print('\n')
        os.chdir('..')

print(f'Folder count: {folder_count}')
print(f'Py count: {py_count}')
print(f'Xls count: {xls_count}')

print(os.listdir())
os.chdir('Statistics-for-Machine-Learning')
for root, dirs, files in os.walk('.'):
    # print(root)
    # print(dirs)
    # print(files)
    pass


# os.makedirs('Test_dir', exist_ok=True) # exist_ok means dont give me an error if the folder already exists
# os.chdir('Test_dir')
# os.rename('file_1.txt', 'file_2.txt') # renames a file, the first argument is the file you want to rename, the second is the new name

# counter = 0
# for pic in os.listdir():
#     os.rename(pic, 'Treacle_'+str(counter)+'.png')
#     counter += 1

# os.path.join('path_1', 'path_2') # this lets you join two incomplete paths together to make a complete path
# fig.save(os.path.join('users/brad/Desktop', 'My_Picture.png'))