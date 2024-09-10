# Script to copy an entire folder  to anotehr folder OR a file to anotehr file using shutil Library


import shutil

COPY_FROM = r"C:\Users\pokhr\Pictures"
COPY_TO = r"D:\Downloads3"

# By default, if you specify an existing directory as the destination,
# an error will occur. To avoid this, use the dirs_exist_ok 

shutil.copytree(COPY_FROM,COPY_TO)


# Copy single file
# shutil.copy2(COPY_FROM,COPY_TO)