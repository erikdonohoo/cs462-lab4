#!/usr/bin/env python
#
# Adapted from script by Diana MacLean 2011
#
# Adapted fro CS448G from Michael Noll"s tutorial on : http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/
#
#

from operator import itemgetter
import sys

# maps words to their counts
word2count = {}
stopWords = ["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves","he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their","theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was","were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and","but","if","or","because","as","until","while","of","at","by","for","with","about","against","between","into","through","during","before","after","above","below","to","from","up","down","in","out","on","off","over","under","again","further","then","once","here","there","when","where","why","how","all","any","both","each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very","s","t","can","will","just","don","should","now"]

# input comes from STDIN
for line in sys.stdin:
	# remove leading and trailing whitespace
	line = line.strip()

	# parse the input we got from mapper.py
	word, count = line.split('\t', 1)
	# convert count (currently a string) to int
	if not word in stopWords:
		try:
			count = int(count)
			word2count[word] = word2count.get(word, 0) + count
		except ValueError:
			# count was not a number, so silently
			# ignore/discard this line
			pass

counted_words = word2count.items()

# write the results to STDOUT (standard output)
for word, count in sorted(counted_words):
	print '%s\t%s'% (word, count)
