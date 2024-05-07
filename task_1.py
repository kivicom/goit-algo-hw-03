import os
import shutil
import argparse
from pathlib import Path

def parse_args():
    '''Встановлює аргументи командного рядка.'''
    parser = argparse.ArgumentParser(description="Copy files into extension-based subdirectories.")
    parser.add_argument('source_dir', type=str, help='Path to the source directory')
    parser.add_argument('destination_dir',
                        type=str, nargs='?',
                        default='dist',
                        help='Path to the destination directory (default is "dist")')

    return parser.parse_args()

def copy_files(src, dest):
    '''Рекурсивно обходить директорії, копіює файли в піддиректорії,
        створені за типом розширення файлу.'''
    try:
        for entry in os.listdir(src):
            full_path = os.path.join(src, entry)
            if os.path.isdir(full_path):
                copy_files(full_path, dest)
            else:
                ext = Path(full_path).suffix[1:] or "no_extension"
                target_dir = os.path.join(dest, ext)
                os.makedirs(target_dir, exist_ok=True)
                shutil.copy(full_path, target_dir)
                print(f"Copied {full_path} to {target_dir}")
    except FileNotFoundError:
        print(f"The directory {src} does not exist.")
    except PermissionError:
        print(f"Permission denied while accessing {src} or its contents.")
    except OSError as e:
        print(f"An error occurred related to OS: {e}")
    except Exception as e:  # As a last resort, catch any other unexpected issues
        print(f"An unexpected error occurred: {e}")

def main():
    '''Main'''
    args = parse_args()
    if not os.path.exists(args.source_dir):
        print("Source directory does not exist.")
        return
    if not os.path.exists(args.destination_dir):
        os.makedirs(args.destination_dir)
    copy_files(args.source_dir, args.destination_dir)

if __name__ == '__main__':
    main()
