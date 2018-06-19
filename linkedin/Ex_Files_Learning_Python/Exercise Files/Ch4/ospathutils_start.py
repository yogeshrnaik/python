#
# Example file for working with os.path module
#
import os
from os import path
from datetime import date, time, timedelta, datetime
import time

def main():
  # Print the name of the OS
  print(os.name)

  # Check for item existence and type
  print("Item exists: ", path.exists('textfile.txt'))
  print("Item is a file: ", path.isfile('textfile.txt'))
  print("Item is a directory: ", path.isdir('textfile.txt'))

  # Work with file paths
  print("Item path: ", path.realpath('textfile.txt'))
  print("Item path and name: ", path.split(path.realpath('textfile.txt')))

  # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt"))
  print(t)
  print(datetime.fromtimestamp(path.getmtime("textfile.txt")))
  
  # Calculate how long ago the item was modified
  td = datetime.now() - datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print("It has been ", td, " since the file was modified")
  print("Or, ", td.total_seconds(), " seconds")

if __name__ == "__main__":
  main()
