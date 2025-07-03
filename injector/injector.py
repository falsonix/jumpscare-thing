import os
import shutil
import sys

if __name__ == "__main__":
    # Get the path to the current executable or script
    if getattr(sys, 'frozen', False):
        exe_path = sys.executable
    else:
        exe_path = os.path.abspath(__file__)
    exe_dir = os.path.dirname(exe_path)
    exe_name = os.path.basename(exe_path)

    # List all .exe files in the same directory as the script, excluding itself
    exe_files = [
        f for f in os.listdir(exe_dir)
        if f.lower().endswith('.exe') and f != exe_name
    ]

    documents_folder = os.path.join(os.path.expanduser("~"), "Documents")

    for exe_file in exe_files:
        src_path = os.path.join(exe_dir, exe_file)
        target_path = os.path.join(documents_folder, exe_file)
        if not os.path.exists(target_path):
            try:
                shutil.copy2(src_path, target_path)
                print(f"Copied {exe_file} to Documents.")
            except Exception as e:
                print(f"Failed to copy {exe_file}: {e}")