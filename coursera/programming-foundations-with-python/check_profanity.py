import urllib

def read_text():
    quotes = open("C:\DDrive\MyData\Yogesh\git_repo\python\coursera\programming-foundations-with-python\movie_quotes.txt")
    contents = quotes.read()
    # print(contents)
    quotes.close()
    check_profanity(contents)

def check_profanity(text):
    con = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text)
    resp = con.read()

    if "true" in resp:
        print("Profanity Alert!")
    elif "false" in resp:
        print("This document has no curse words!")
    else:
        print("Could not scan the document properly.")
        
    
    con.close()

read_text()
