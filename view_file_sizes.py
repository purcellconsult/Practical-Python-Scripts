import os

path_to_desktop_on_windows = r"C:\Users\dopurcell\Desktop"    # the r is need in front of the string
path_to_desktop_on_macos = r"/Users/username/Desktop"
path_to_desktop_on_linux = r" /home/username/Desktop"

os.chdir(path_to_desktop_on_windows)
files_in_desktop = os.listdir()

for x in files_in_desktop:
    print(f"{x} {os.path.getsize(x)} | bytes")