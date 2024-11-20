from operations import (
    find_duplicates,
    delete_duplicates,
    calculate_duplicate_space,
    calculate_space_freed,
)

import argparse

def main():
    parser = argparse.ArgumentParser(description="ZeroClone: A Duplicate File Finder Tool")
    parser.add_argument("directory", help="Directory to scan for duplicate files")
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Delete duplicate files after finding them",
    )
    parser.add_argument(
        "--space",
        action="store_true",
        help="Calculate the space occupied by duplicate files",
    )
    parser.add_argument(
        "--space-freed",
        action="store_true",
        help="Calculate the space freed after deleting duplicates",
    )
    
    args = parser.parse_args()

    if args.space_freed:
        space_freed = calculate_space_freed(args.directory)
        print(f"Space freed after deletion: {space_freed} bytes")
    elif args.space:
        duplicate_space = calculate_duplicate_space(args.directory)
        print(f"Space occupied by duplicates: {duplicate_space} bytes")
    elif args.delete:
        delete_duplicates(args.directory)
    else:
        duplicates = find_duplicates(args.directory)
        if duplicates:
            print("Duplicate files found:")
            for original, duplicate_list in duplicates.items():
                print(f"Original: {original}")
                for duplicate in duplicate_list:
                    print(f"  - Duplicate: {duplicate}")
        else:
            print("No duplicate files found.")

if __name__ == "__main__":
    main()
