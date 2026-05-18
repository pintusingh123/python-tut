import os
# import shutil
def _file_path():
  return os.path.join(os.path.dirname(__file__), "app.txt")

_file_path =_file_path()
try:
  os.remove(_file_path) #file delete ke liye
  print("file deleted successfully")
except FileNotFoundError:
  print("file not found")

  # os.rmdir(_file_path) # empty directory delete ke liye

  # import shutil
  # shutil.rmtree(_file_path) # directory non empty delete ke liye