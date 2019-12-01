import urllib.request

def read_text():
    quotes = open("/Users/yogeshnaik/Yogesh/workspace/python/coursera/programming-foundations-with-python/movie_quotes.txt")
    contents = quotes.read()
    # print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text):
    param = urllib.parse.quote(text)
    con = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+param)
    resp = con.read().decode('UTF-8')

    if "true" == resp:
        print("Profanity Alert!")
    elif "false" == resp:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")


    con.close()

read_text()
