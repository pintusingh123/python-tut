# append data in another file
import os 
def _file_path():
  return os.path.join(os.path.dirname(__file__), "test.txt")

file_path = _file_path()
file = open(file_path, 'a')
try:
  file.write("hello this is a test file for append mode line one \n")
except FileNotFoundError:
  print("file not found")
finally:
  file.close()