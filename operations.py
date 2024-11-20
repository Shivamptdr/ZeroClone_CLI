import os
from utils import list_files, files_are_equal

def find_duplicates(directory):
    """Find duplicate files in a directory and its subdirectories."""
    files = list(list_files(directory))
    duplicates = {}

    for i, file1 in enumerate(files):
        if file1 in duplicates:  # Skip already found duplicates
            continue
        duplicates[file1] = []
        for j in range(i + 1, len(files)):
            file2 = files[j]
            if os.path.getsize(file1) != os.path.getsize(file2):
                continue
            if files_are_equal(file1, file2):
                duplicates[file1].append(file2)

    # Remove non-duplicate entries
    duplicates = {key: val for key, val in duplicates.items() if val}
    return duplicates

def delete_duplicates(directory):
    """Find and delete duplicate files."""
    duplicates = find_duplicates(directory)
    for original, duplicates_list in duplicates.items():
        for duplicate in duplicates_list:
            os.remove(duplicate)
            print(f"Deleted: {duplicate}")

def calculate_duplicate_space(directory):
    """Calculate the space occupied by duplicate files."""
    duplicates = find_duplicates(directory)
    space = 0
    for duplicates_list in duplicates.values():
        space += sum(os.path.getsize(file) for file in duplicates_list)
    return space

def calculate_space_freed(directory):
    """Calculate the space that would be freed after deleting duplicates."""
    return calculate_duplicate_space(directory)
