import os

def delete_files(dir_path, extension, file_size):
    """
    Deletes files in the given directory with the given extension and file size.

    Args:
    dir_path (str): The directory path where the files are located.
    extension (str): The file extension to delete (e.g. '.txt').
    file_size (int): The file size in bytes above which files should be deleted.
    """
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            if file.endswith(extension) and os.path.getsize(os.path.join(root, file)) > file_size:
                os.remove(os.path.join(root, file))
                print(f"{os.path.join(root, file)} deleted.")


delete_files("C:/Windows/Temp", ".sdb", 1024)
delete_files("C:/Windows/Temp", ".cgv", 1024)
delete_files("C:/Windows/Temp", ".tmp", 1024)
delete_files("C:/Windows/Temp", ".ses", 1024)
delete_files("C:/Windows/Temp", ".txt", 1024)


## this code is shit lol i put more effort into the other ones that do this + more

