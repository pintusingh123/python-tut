# write mode in file
import os


def _file_path():
   return os.path.join(os.path.dirname(__file__), "test.txt")

file_path = _file_path()

file = open(file_path, "w")
file.write("hello this is a test file for write mode line one \n")
 
file.close()