#!/usr/bin/python

import os
import re
from pos import *
from catcat import *

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

def word_pos(word):
	allmatches = re.findall("\/(.*)", word, re.DOTALL)
  	pos = allmatches[0]
  	return pos[0:]


def main():
	word_functions = {}
	data = {}

	mainfolder = "WSJ-2-12"
	data_files = subfolder_names(mainfolder)

	preprocessed_chunks = []
	for f in data_files:
		preprocessed_chunks.extend(parse_single_file(f))

	for chunk in preprocessed_chunks:
		for word in chunk:
			both = re.findall("[^\s/]+", word, re.DOTALL)
			key = both[0]
			if word_functions.has_key(key) :
				if not word in word_functions[key] : 
	 				word_functions[key].append(word)
			else :
				word_functions[key] = [word]

	for chunk in preprocessed_chunks:
		for idx, word in enumerate(chunk):
			if ((idx + 2) >= len(chunk)):
				if (data.has_key(word)):
					data[word].update(word, "")
				else :
					data[word] = Pos(word, [], 1)
			else:
				if (data.has_key(word)):
					data[word].update(word, chunk[idx + 1])
				else :
					data[word] = Pos(word, [chunk[idx + 1]], 1)

	for d in sorted(data):
		data[d].display()

	p_cat_cat = {}

	for d in sorted(data):
		if p_cat_cat.has_key(data[d].word_pos()):
			p_cat_cat[data[d].word_pos()].update(data[d].following_categories())
		else:
			p_cat_cat[data[d].word_pos()] = Catcat(data[d].word_pos(), data[d].following_categories())

	for c in sorted(p_cat_cat):
		print p_cat_cat[c].display()

	# if (LOGGING):
	# 	for w in sorted(data):
	# 		print w + " : " + str(data[w]) 

	# if (LOGGING):
	# 	for pc in preprocessed_chunks:
	# 		print pc
	# 		print "-----"	


	# pos = Pos("test", [], 0)
 # 	pos.display()
 # 	data['test'] = pos
 # 	print data['test'].display()
 # 	print data.has_key('test')
 # 	print data.has_key('test2')
	# print "Ending execution..."

main()