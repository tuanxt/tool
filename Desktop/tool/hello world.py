import os

# Getting the current work directory (cwd)
thisdir = os.getcwd()

# r=root, d=directories, f = files
for r, d, f in os.walk(thisdir):
    for file in f:
        if ".docx" in file:
            print(os.path.join(r, file))
#hello2
for main