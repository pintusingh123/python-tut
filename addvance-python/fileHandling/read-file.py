# reading file by another file 
import os 
def _file_path():
  return os.path.join(os.path.dirname(__file__), "test.txt")

file_path = _file_path()

try:
  file = open(file_path, "r") 
  data = file.read()
except FileNotFoundError:
  print("file not found")
finally:
  file.close()

print(data)