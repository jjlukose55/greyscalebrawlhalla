from to_greyscale import to_greyscale
from find_directory import find_directory
import os

startpath = 'C:/Program Files (x86)/Steam/steamapps/common/'
subpaths = ['mapArt/Backgrounds', 'images/thumbnails']

# Find Brawlhalla Directory
path = find_directory('Brawlhalla', startpath)
if not path:
    print("Brawlhalla not found in Steam directory, searching entire system...")
    path = find_directory('Brawlhalla', '/')  # Root directory for Unix-like systems
    if not path:
        raise FileNotFoundError("Could not find Brawlhalla directory")

print(f"Found directory at: {path}")

# Process each subpath
for subpath in subpaths:
    full_path = os.path.join(path, subpath)
    if os.path.exists(full_path):
        print(f"Processing: {full_path}")
        to_greyscale(full_path, full_path)
    else:
        print(f"Warning: Subdirectory not found - {full_path}")