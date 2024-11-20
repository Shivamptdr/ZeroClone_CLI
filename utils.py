import os

def list_files(directory):
    """Recursively find all files in a directory and its subdirectories."""
    for root, _, files in os.walk(directory):
        for file in files:
            yield os.path.join(root, file)

def files_are_equal(file1, file2, chunk_size=4096):
    """Compare two files chunk by chunk."""
    with open(file1, "rb") as f1, open(file2, "rb") as f2:
        while True:
            chunk1 = f1.read(chunk_size)
            chunk2 = f2.read(chunk_size)
            if chunk1 != chunk2:
                return False
            if not chunk1:  # End of file reached
                break
    return True
