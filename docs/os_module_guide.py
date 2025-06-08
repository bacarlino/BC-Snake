# os_module_guide.py
# Reference guide for basic file and folder operations using the os module

import os

# 1. Current working directory
cwd = os.getcwd()
print("Current Working Directory:", cwd)

# 2. Directory of the current script file
script_dir = os.path.dirname(__file__)
print("Script Directory:", script_dir)

# 3. Joining paths
snake_image_path = os.path.join(script_dir, 'assets', 'images', 'snake.png')
print("Snake Image Path:", snake_image_path)

# 4. Checking if a path exists
print("Exists:", os.path.exists(snake_image_path))
print("Is File:", os.path.isfile(snake_image_path))
print("Is Directory:", os.path.isdir(os.path.join(script_dir, 'assets')))

# 5. Navigating up or down folders
parent_dir = os.path.dirname(script_dir)
granny_dir = os.path.dirname(parent_dir)
print("Parent Dir:", parent_dir)
print("Grandparent Dir:", granny_dir)

# 6. Listing files and folders
assets_path = os.path.join(script_dir, 'assets')
if os.path.exists(assets_path):
    print("Files in assets:", os.listdir(assets_path))

# 7. Creating folders
# os.mkdir('new_folder')
# os.makedirs('nested/folder/here')

# 8. Removing files or folders
# os.remove('file.txt')
# os.rmdir('empty_folder')
# os.removedirs('a/b/c')

# 9. Getting absolute path
absolute_snake_path = os.path.abspath(snake_image_path)
print("Absolute Snake Path:", absolute_snake_path)

# 10. Get file name and extension
filename = os.path.basename(snake_image_path)
name, ext = os.path.splitext(filename)
print("Filename:", filename)
print("Name:", name)
print("Extension:", ext)

# TL;DR Common Usage
BASE_DIR = os.path.dirname(__file__)
ASSETS_DIR = os.path.join(BASE_DIR, '..', 'assets')
snake_path = os.path.join(ASSETS_DIR, 'images', 'snake.png')
if os.path.exists(snake_path):
    print("Snake image found:", snake_path)
