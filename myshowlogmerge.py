import re
import myciscocom
import sys

if len(sys.argv) != 4:
	hostlfname = 'hostlist.csv'
	findfl = 0
	findstr = '.*up.*|.*down.*'
else:
	hostlfname = sys.argv[1]
	findfl = int(sys.argv[2])
	findstr = sys.argv[3]
	
#print('hostf = ',hostlfname)
#print('findfl = ',findfl)
#print('findstr = ',findstr)

with open(hostlfname) as f:
		for f_line in f:
			#print('f_line = ',f_line)
			
			result = re.match('^#.*',f_line)
			if result:
				continue
			
			tmpstr = f_line.split( )
			path = tmpstr[1]
			hostname = tmpstr[0]
			
			#print('hname  = ',hostname,'fname = ',path)
			myciscocom.merge_showlog(hostname,path,findfl,findstr)

