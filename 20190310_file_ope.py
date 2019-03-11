import re
import myciscocom

hostlfname = 'hostlist.csv'
findfl = 0
findstr = r'.*up.*|.*down.*'

#print('hostf = ',hostlfname)

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