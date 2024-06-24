import os, sys

relative_path = "dependencies.py"
absolute_path = os.path.abspath(relative_path)
path_components = absolute_path.split(os.path.sep)

path_components.pop()
# full_path = os.path.join(*path_components,"searchIndexing/searchIndexing/")
# full_path_with_drive = str(os.path.join(path_components[0], os.path.sep, full_path))

# sys.path.insert(1, str(full_path_with_drive))

print(absolute_path)