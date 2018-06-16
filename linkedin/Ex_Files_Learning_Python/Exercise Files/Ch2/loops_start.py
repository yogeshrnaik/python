#
# Example file for working with loops
#

def main():
  x = 0

  # define a while loop
  print ("***** while loop *****")
  while (x<5):
    print(x)
    x = x + 1

  print ("***** for loop *****")
  # define a for loop
  for x in range(5, 10):
    print(x)

  # use a for loop over a collection
  print ("***** for loop over a collection *****")
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for d in days:
    print (d)
 
  # use the break and continue statements
  print ("***** break and continue *****")
  for x in range(5, 10):
    #if (x == 7): break
    if (x % 2 == 0): continue
    print(x)

  #using the enumerate() function to get index 
  print ("***** enumerate() function *****")
  days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
  for i,d in enumerate(days):
    print (i, d)

if __name__ == "__main__":
  main()
