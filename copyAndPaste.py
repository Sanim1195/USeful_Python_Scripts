# Script to copy an entire folder  to anotehr folder OR a file to anotehr file using shutil Library

import shutil

COPY_FROM = r"C:\Users\pokhr\Pictures"
COPY_TO = r"E:\Pictures"

# If you specify an existing directory as the destination path,
# an error will occur. To avoid this, use the dirs_exist_ok as the third argument
# If the destination does not exist, it creates a new directory at the destination path
# and copies the source into it.


shutil.copytree(COPY_FROM,COPY_TO)


# Copy single file
# shutil.copy2(COPY_FROM,COPY_TO)

# Move a folder:
# shutil.move(src,dest) will detele the source directory after the move