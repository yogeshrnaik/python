#
# Read and write files using the built-in Python file methods
#

def main():  
  # Open a file for writing and create it if it doesn't exist
  #f = open('textfile.txt', 'w+')

  # Open the file for appending text to the end
  #f = open('textfile.txt', 'a')

  # write some lines of data to the file
  #for i in range(10):
  #  f.write("This is line %d\n" % (i+1))
  
  # close the file when done
  #f.close()

  # Open the file back up and read the contents
  # It is good practice to use the with keyword when dealing with file objects.
  # The advantage is that the file is properly closed, even if an exception is raised at some point
  with open('textfile.txt', 'r') as f:
    if (f.mode == 'r'):
      # contents = f.read()
      # print(contents)
      fl = f.readlines()
      for line in fl:
        print(line)

if __name__ == "__main__":
  main()
