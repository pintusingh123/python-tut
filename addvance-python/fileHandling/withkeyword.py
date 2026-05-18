
import os 
def _file_path():
  return os.path.join(os.path.dirname(__file__), "test.txt")

file_path = _file_path()


try:
    with open(file_path, "a") as f:
        f.write("Pintu\n")

    with open(file_path, "r") as f:
        print(f.read())

except Exception as e:
    
    print(e)