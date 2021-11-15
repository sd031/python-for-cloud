#get current working directory
import os
currentWorkingDirectory = os.getcwd()
# print("Current Working Directory: ",currentWorkingDirectory)


#change directory to any path such as /var/logs 
# import os
# os.chdir('/var/logs')
# print("Changed to Directory: ",os.getcwd())
# os.chdir(currentWorkingDirectory)
# print("Current Working Directory: ",os.getcwd())

#check directories and file list
# import os
# print(os.listdir())
# print("Lit of Directories and files", os.listdir())

#create new directory
# import os
# if os.path.exists("my_new_sample_directory"):
#     print("The Folder already exists")
# else:
#     os.mkdir("my_new_sample_directory")
#     print("The Folder is created")

#renaming file or directory
# import os
# os.rename('my_new_sample_directory','my_renamed_sample_directory')
# print("The directory is renamed")

#removing a empty directory
# import os
# os.rmdir("my_renamed_sample_directory")

#removing a directory which alrady has few files and sub directories
# import shutil
# shutil.rmtree('my_renamed_sample_directory')

