import shutil
import os

""" #arc_formats = shutil.get_archive_formats()
unarc_formats = shutil.get_unpack_formats()
print(unarc_formats)

# Source File location
source_file = '/home/arnamaity/Downloads/expense_tracker_api-master.zip'

# Constructing the path of the extraction location. 
dir_path = os.getcwd()
path = os.path.join(dir_path,'expense_tracker_api/')
os.mkdir(path)
dest_dir = path

print(path)

# Extract the files
shutil.unpack_archive(source_file,dest_dir,'zip')

# Print the Extracted Contents.
dir_list = os.listdir(path)
print('The final directory list: ')
print(dir_list)

# Compress extracted files into .tar.xz format.
filename = shutil.make_archive(path+'expense_tracker_api_master','xztar',path,path)

print(filename) """

print(shutil.get_archive_formats())