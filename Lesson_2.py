# Setting up a file to practice coding in Python
# Corresponds to the requirements of Udacity course "Programming Foundations with Python"
# https://www.udacity.com/course/programming-foundations-with-python--ud036

# Lesson 2: Use Functions

import time
import webbrowser

total_breaks = 3
break_count = 0

print("This program started on "+time.ctime())
while (break_count < total_breaks): 
	time.sleep(4)
	webbrowser.open("http://youtube.com")
	break_count = break_count + 1


