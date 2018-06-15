import webbrowser
import time

print("This break program stated at: " + time.ctime())
total_breaks = 3
break_count = 0
while (break_count < total_breaks):
    time.sleep(2)
    webbrowser.open("http://youtube.com")
    break_count = break_count + 1

print "Good bye!"
