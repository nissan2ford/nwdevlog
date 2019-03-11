import os
import subprocess
import sys

import myfunction

print(os.getcwd())
cmd = 'cat testdata.txt'
#cmd = "ls -l"
for line in myfunction.command(cmd):
    print('===', line)
