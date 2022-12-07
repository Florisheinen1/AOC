

folders = {"root": 0} # /p/a/t/h/foldername, size
files = {} # /p/a/t/h/filename, size

current_path = []

def current_path_to_string(filename = None):
    global current_path
    if not filename:
        return "/".join(current_path)
    return "/".join(current_path) + "/" + filename
    

with open("input.txt", 'r') as file:
    for row in file.readlines():
        if row[0] == "$":
            if "cd" in row:
                folder_name = row.rstrip()[5:]
                if folder_name == "/":
                    # Then we always go to / (empty path)
                    current_path = ["root"]
                elif folder_name == "..":
                    # Then we go folder up
                    current_path.pop()
                else:
                    # Then we go folder deeper
                    current_path.append(folder_name)
            else:
                # We entered ls... Do nothing
                pass
        else:
            # We received output. Either a folder or file
            params = row.rstrip().split(" ")
            if params[0] == "dir":
                # We got a directory. Do nothing
                dir_name = params[1]
                path = current_path_to_string(dir_name)
                folders[path] = 0
            else:
                # We have a file!
                size = int(params[0])
                filename = params[1]

                path = current_path_to_string(filename)
                files[path] = size

# print(folders)
# print("\n")
# print(files)

def get_folder_size(folder):
    global folders, files

    size = 0
    for file in files:
        if folder in file:
            size += files[file]
    return size

def set_folders_sizes():
    global folders, files

    for folder in folders:
        size = get_folder_size(folder)
        folders[folder] = size

set_folders_sizes()

TOTAL_1 = 0
for folder in folders:
    size = folders[folder]
    if size <= 100000:
        TOTAL_1 += size


print(folders["root"])

print(TOTAL_1)

####################################

MIN_DELETE = 8381165

SMALLEST = folders["root"]
for folder in folders:
    size = folders[folder]
    if size < SMALLEST and size > MIN_DELETE:
        SMALLEST = size

print(SMALLEST)