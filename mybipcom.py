import re 

def merge_showlog(hostname,path,findfl,findstr):
	startstr = r'.*show\s*sys\s*log.*'
	endstr = r'^.*#'
	outfl = 0

	with open(path) as f:
		for f_line in f:

			result = re.match(startstr,f_line)
			if result:
				outfl = 1
				continue

			result = re.match(endstr,f_line)
			if result:
				result = re.match(startstr,f_line)
				if result:
					outfl = 1
					continue
				else:
					outfl = 0

			result = re.match(findstr,f_line)
			if result:
				if (findfl == 1 and outfl == 1):
					print(hostname+':'+f_line.strip())
			else: 
				if (findfl == 0 and outfl == 1):
					print(hostname+':'+f_line.strip())
