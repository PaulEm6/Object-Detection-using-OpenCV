import os
import subprocess


script_path = os.path.join(os.getcwd(), "algorithm.py")

def explore_folder(folder_path):
    for root, dirs, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            # Run an external script with the file_path as an argument
            if ("eference" not in file_path) and ("object" not in file_path):
                print("Processing file: " + str(file_path))
                subprocess.run(["python", script_path, file_path])

if __name__ == "__main__":
    import sys

    if len(sys.argv) != 2:
        print("Usage: python /path/to/folder")
    else:
        folder_path = sys.argv[1]
        if os.path.exists(folder_path) and os.path.exists(script_path):
            explore_folder(folder_path)
        else:
            print("Folder or script does not exist.")
