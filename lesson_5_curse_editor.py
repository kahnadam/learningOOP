# open the file of text
def read_text():
    quotes = open(r"C:\Users\adamkahn\learningOOP\quotes.txt")
    contents_of_file = quotes.read() #allows you to read the contents of the file
    print(contents_of_file)
    quotes.close() #close the file that we opened
read_text()
