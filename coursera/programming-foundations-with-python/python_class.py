class Foo:
    a, b, c = 0, "foo", (1,2)


i = Foo()
print i.a, i.b, i.c

i.a = 12
i.new = "yikes" # dynamic attribute creation
print i.a, i.b, i.c, i.new
      
class Bar: pass
bar.a = 1
bar.b = 2
