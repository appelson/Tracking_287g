# Importing packages
import os
import hashlib

# Defining a function to get the hash of a filepath
def get_file_hash(filepath):
    hash_sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_sha256.update(chunk)
    return hash_sha256.hexdigest()

# Defining a function to remove duplicate files recursively (for agreements folder)
def remove_duplicate_files_recursive(base_path):
    seen_files = {}

    # Walking through all nested files and folders
    for root, dirs, files in sorted(os.walk(base_path)):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                file_hash = get_file_hash(file_path)
            except Exception:
                continue

            # Adding original file hash
            if file_hash not in seen_files:
                seen_files[file_hash] = file_path
            # Deleting duplicate file
            else:
                print(f"Deleting: {file_path}")
                os.remove(file_path)

# Defining a function to remove duplicate files for sheets folder
def remove_duplicate_files_one_level(base_path):
    seen_files = {}

    # Looping through one layer of subfolders in sheets
    for subfolder in sorted(os.listdir(base_path)):
        subfolder_path = os.path.join(base_path, subfolder)
        if not os.path.isdir(subfolder_path):
            continue

        # Looping through files inside each subfolder
        for file in os.listdir(subfolder_path):
            file_path = os.path.join(subfolder_path, file)
            if not os.path.isfile(file_path):
                continue
            try:
                file_hash = get_file_hash(file_path)
            except Exception:
                continue

            # Adding original file hash
            if file_hash not in seen_files:
                seen_files[file_hash] = file_path
            # Deleting duplicate file
            else:
                print(f"Deleting: {file_path}")
                os.remove(file_path)

# Removing empty directories
def delete_empty_dirs(base_path):
  
    # Walking directory tree from bottom up
    for root, dirs, files in os.walk(base_path, topdown=False):
        if not dirs and not files:
            try:
                os.rmdir(root)
                print(f"Deleted: {root}")
            except OSError:
                print(f"Error deleting: {root}")

# Running the script
if __name__ == "__main__":
    remove_duplicate_files_recursive("agreements")
    delete_empty_dirs("agreements")
    remove_duplicate_files_one_level("sheets")
    delete_empty_dirs("sheets")
