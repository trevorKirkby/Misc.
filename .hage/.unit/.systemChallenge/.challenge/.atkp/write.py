def replace(fileName,replaceFrom,replaceWith):
	for line in open(fileName):
		if line == replaceFrom:
			print replaceWith
		else:
			print line
