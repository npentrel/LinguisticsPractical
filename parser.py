#!/usr/bin/python

import os
import re
from pos import *

LOGGING = True

def removeEmptyChunks(chunks_input):
	chunks_output = []
	for chunk in chunks_input:
		if chunk:
			chunks_output.append(chunk)
	return chunks_output

def parse_single_file(fname):
	with open(fname) as f:
	    content = f.readlines()
	content = "".join(content)
	chunks = [x for x in content.split("======================================")]
	processed_chunks = []
	for chunk in chunks:
		matches = re.findall("[^\s]+/[^\s]+", chunk, re.DOTALL)
		processed_chunks.append(matches)
	processed_chunks = removeEmptyChunks(processed_chunks)
	return processed_chunks

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

	preprocessed_chunks = []
	for f in data_files:
		preprocessed_chunks.extend(parse_single_file(f))

	# if (LOGGING):
	# 	for pc in preprocessed_chunks:
	# 		print pc
	# 		print "-----"	

	# parse_single_file(data_files[0])

	pos = Pos("test", [], 0)
 	pos.display()

	print "Ending execution..."

main()