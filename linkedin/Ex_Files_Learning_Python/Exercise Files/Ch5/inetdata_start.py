# 
# Example file for retrieving data from the internet
#
import urllib.request

def main():
  with urllib.request.urlopen("http://www.google.com") as webUrl:
    print("Result code: ", webUrl.getcode())
    data = webUrl.read()
    print(data)

if __name__ == "__main__":
  main()
