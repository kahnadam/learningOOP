# rename files with Python

import os
def rename_files():
	#(1) get file names from a folder
	file_list = os.listdir(r"C:\Users\adamkahn\learningOOP\lesson_2_prank")
	
	#find the current working directory
	saved_path = os.getcwd()
	print("Current Working Directory is "+saved_path)
	
	#change directory to the one with the files
	os.chdir(r"C:\Users\adamkahn\learningOOP\lesson_2_prank")
	
	#(2) for each file, rename file
	for file_name in file_list:
		print("Old Name - "+file_name)
		print("New Name - "+file_name.translate(None, "0123456789"))
		os.rename(file_name,file_name.translate(None, "0123456789"))
	#return to original working directory
	os.chdir(saved_path)