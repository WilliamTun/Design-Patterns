from pathlib import Path 

# current working directory
Path.cwd()

# home directory on machine  
Path.home()

# create path object
linux_path = Path("usr/my/random/path")
linux_path2 = Path("/usr") / "bin" / "path"
linux_path3 = Path.cwd() / "bin" / "path"
windows_path = Path(r"c:\Windows\System32\cmd.exe")

# check if path exists
linux_path.exists() 

# check if path is a directory 
linux_path.is_dir()

# check if path is file
linux_path.is_file()

# read in contents of file
path = Path.cwd() / "file.yaml"
with path.open() as file:
    print(file.read())

# read in contents of text file [shortcut]
path.read_text()

# return PATH of a specific file
path = Path("somefile.txt")

full_path = path.resolve()  # FULL PATH of file
full_path.parent # parent directory of file
full_path.parent.parent # grand parent directory of file

full_path.name # name of original file
full_path.stem # name of file without suffix (eg. no csv/xlsx)
full_path.suffix # name of file extension (eg. csv / xlsx)



# Create a new file
new_file = Path.cwd() / "new_file.txt"
new_file.touch() # create new file
new_file.write_text("Hello") # write to new file
new_file.unlink() # delete file

# Create a new directory
from os import chdir
new_dir = Path.cwd() / "new_dir"
new_dir.mkdir() # make directory 
chdir(new_dir) # change directory
print(f" Current working directory {Path.cwd()}")
new_dir.rmdir() # delete directory

