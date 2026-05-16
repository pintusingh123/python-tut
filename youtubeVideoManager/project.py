import json
import os


def _data_path():
   return os.path.join(os.path.dirname(__file__), "videos.txt")


def load_data():
  path = _data_path()
  try:
    with open(path, "r", encoding="utf-8") as f:
      test = json.load(f)
    #   print(type (test))
      return test
  except FileNotFoundError:
    return []
 
   

def save_data(videos):
   path = _data_path()
   with open(path, "w", encoding="utf-8") as f:
      json.dump(videos, f, ensure_ascii=False, indent=2)

def listAllVideos(videos):
  if not videos:
    print("No videos saved yet.")
    return

  for index, video in enumerate(videos, start=1):
    title = video.get("title", "<no title>")
    time = video.get("time", "")
    description = video.get("description", "")
    print(f"{index}. {title} ({time}) - {description}")
 

def addVideo(videos):
  title = input("Enter the video name: ")
  time = input("Enter the video time: ")
  url = input("Enter the video URL: ")
  description = input("Enter the video description: ")
  videos.append(
     {
        "title": title,
        "time": time,
        "url": url, 
        "description": description
        })
  
  save_data(videos)

def UpdateVideo(videos):
 listAllVideos(videos)
 input_index = input("Enter the video number to update: ")

 if 1 <= input_index <= len(videos):
    title = input("Enter the new video name: ")
    time = input("Enter the new video time: ")
    videos[input_index - 1] = {
        "title": title,
        "time": time
    }
 else:
   print("Invalid video number.")


 save_data(videos)


def deleteVideo(videos):
    listAllVideos(videos)
    input_index = int(input("Enter the video number to delete: "))
    if 1 <= input_index <= len(videos):
        del videos[input_index - 1]
         
        save_data(videos)
    else:
        print("Invalid video number.")

def main():
    videos = load_data()
    while True:
      print("\n Youtube Video Manager | choose an option")

      print("1. list a favourite video")
      print("2. add a youtube video")
      print("3. Update a youtube video details ")
      print("4. delete a youtube video")
      print("5. exit the app")

      input_option = input("Enter your option: ")
    #   print(videos)

      match input_option:
        case "1":
          listAllVideos(videos)
        case "2":
            addVideo(videos)
        case "3":  
            UpdateVideo(videos)
        case "4":
            deleteVideo(videos)
        case "5":
            print("Good bye")
            break
        case _:
            print("Invalid option, try again")

if __name__ == "__main__":
    main()