import os


def get_files_info(working_directory, directory=None):
    if directory not in os.listdir(working_directory):
        return (f'Error: Cannot list "{directory}" as it is outside the permitted working directory')
    

    if (not os.path.isdir(os.path.join(working_directory, directory))):
        return (f'Error: "{directory}" is not a directory')
    

    for item in os.listdir(os.path.join(working_directory, directory)):

        item_path = os.path.join(working_directory, directory, item)

        if os.path.isfile(item_path):
            print(f"{item}: file_size: {os.path.getsize(item_path)} bytes is_dir: False")

        elif os.path.isdir(item_path):
            
            total_size = 0
            for file in os.listdir(item_path):
                filepath = os.path.join(item_path, file)
            # Skip broken symlinks or inaccessible files
                if os.path.isfile(filepath):
                    total_size += os.path.getsize(filepath)
            print(f"{item}: file_size: {total_size} bytes is_dir: True")
