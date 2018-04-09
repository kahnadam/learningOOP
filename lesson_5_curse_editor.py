import urllib

# open the file of text
def read_text():
    quotes = open(r"C:\Users\adamkahn\learningOOP\quotes.txt")
    contents_of_file = quotes.read() #allows you to read the contents of the file
    print(contents_of_file)
    quotes.close() #close the file that we opened
    check_profanity(contents_of_file)

def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check) #opens a connection to a website
    output = connection.read()
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity alert!")
    elif "false" in output:
        print("No curse words in this document")
    else:
        print("Error - could not scan document")
    
read_text()
