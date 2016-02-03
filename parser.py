import os
import re

LOGGING = True



def parse_single_file(fname):
	with open(fname) as f:
	    content = f.readlines()
	for line in content:
		no_data = False
		if "===================" in line or line == "\n":
			no_data = True
			
		if pattern = re.compile("^([A-Z][0-9]+)*$")
pattern.match(string)


		if (not no_data):
			print line

def data_file_names(top_folder, folder):
	path = top_folder + "/" + folder
	files = os.listdir(path)
	files = [ (path + "/" + f) for f in files]
	return files

def subfolder_names(top_folder):
	if (LOGGING):
		print "Entering " + str(top_folder)		
	subfolders = os.listdir(top_folder)
	if (LOGGING):
		print "subfolders found: " + str(subfolders)
	all_data_files = []	
	for folder in subfolders:
		data_files = data_file_names(top_folder, folder)
		all_data_files.extend(data_files)
	# if (LOGGING):
	# 	print "data_files found: " + str(all_data_files) 
	return all_data_files

def main():
	mainfolder = "WSJ-2-12"
	data_files = subfolder_names(mainfolder)

	# for f in data_files:
	# 	parse_single_file(f)

	parse_single_file(data_files[0])

	print "Ending execution..."

main()