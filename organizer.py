import os
import shutil
from pathlib import Path

# Define extension mapping dictionary
EXTENSION_MAPPING = {
    '.pdf': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.xlsx': 'Documents',
    '.jpg': 'Images',
    '.jpeg': 'Images',
    '.png': 'Images',
    '.gif': 'Images',
    '.mp4': 'Videos',
    '.mkv': 'Videos',
    '.zip': 'Archives',
    '.rar': 'Archives',
    '.tar': 'Archives',
    '.py': 'Code',
    '.js': 'Code',
    '.html': 'Code'
}

def organize_directory(target_dir=None):
    if not target_dir:
        target_dir = input("Enter path of the directory to organize (leave blank for current working directory): ").strip()
        if not target_dir:
            target_dir = os.getcwd()

    target_path = Path(target_dir)

    if not target_path.exists() or not target_path.is_dir():
        print(f"❌ Error: Directory '{target_dir}' does not exist or is invalid.")
        return

    print(f"\n📂 Scanning directory: {target_path.absolute()}")
    moved_count = 0

    try:
        with os.scandir(target_path) as entries:
            for entry in entries:
                if entry.is_file():
                    file_path = Path(entry.path)
                    file_ext = file_path.suffix.lower()

                    # Determine category folder
                    category = EXTENSION_MAPPING.get(file_ext, 'Others')
                    dest_folder = target_path / category
                    
                    # Create subfolder if it doesn't exist
                    dest_folder.mkdir(exist_ok=True)

                    dest_path = dest_folder / file_path.name

                    # Handle name collisions
                    if dest_path.exists():
                        base_name = file_path.stem
                        counter = 1
                        while True:
                            new_name = f"{base_name}_{counter}{file_ext}"
                            dest_path = dest_folder / new_name
                            if not dest_path.exists():
                                break
                            counter += 1

                    try:
                        shutil.move(str(file_path), str(dest_path))
                        print(f"➡️ Moved: {file_path.name} -> {category}/")
                        moved_count += 1
                    except PermissionError:
                        print(f"⚠️ Permission denied: Could not move {file_path.name}")
                    except Exception as e:
                        print(f"⚠️ Error moving {file_path.name}: {e}")

        print(f"\n✨ Organization Complete! Total files relocated: {moved_count}")

    except Exception as e:
        print(f"❌ An error occurred during directory scanning: {e}")

if __name__ == "__main__":
    organize_directory()