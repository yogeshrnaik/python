#
# Example file for working with classes
#
class MyClass():
  def method1(self):
    print("MyClass method1")

  def method2(self, someString):
    print("MyClass method2 : " + someString)


class AnotherClass(MyClass):
  def method1(self):
    MyClass.method1(self)
    print("AnotherClass method1")

  def method2(self, someString):
    print("AnotherClass method2")


def main():
  o = MyClass()
  o.method1()
  o.method2("This is some string")

  a = AnotherClass()
  a.method1()
  a.method2("This is another string")
  
if __name__ == "__main__":
  main()
