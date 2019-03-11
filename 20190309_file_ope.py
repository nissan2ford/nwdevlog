import re

path = 'testdata.txt'
findfl = 1
startstr = r'.*show log.*'
endstr = r'^.*#'
findstr = r'ttt'
outfl = 0

hostname = 'test01'

with open(path) as f:
	for f_line in f:
#		print('f_line = ',f_line)
		
		result = re.match(startstr,f_line)
		if result:
			outfl = 1
			continue
			
		result = re.match(endstr,f_line)
		
		if result:
			break
				
#		print('outfl = ',outfl)
		
		result = re.match(findstr,f_line)
		
		if result:
			if findfl == 1 and outfl == 1:
				print(hostname,':',f_line.strip())
		else:
			if findfl == 0 and outfl == 1:
				print(hostname,':',f_line.strip())
				