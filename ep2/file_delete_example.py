#we can remove file by usnig inbild os module
# import os
# os.remove("sample_file_2.txt")

#delete file if exist

import os
if os.path.exists("sample_file_2.txt"):
  os.remove("sample_file_2.txt")
else:
  print("The file does not exist")