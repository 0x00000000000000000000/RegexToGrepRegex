import sys
import re
n=len(sys.argv)
if (n==1):
	sys.exit()
else:
	x=sys.argv[1]
	y=[]
	for i in list(x):
		if(i in list('-@_!#%&*()<>?/|}{~:')):
			y.append("\\"+str(i))
		else:
			y.append(i)
	print(''.join(y))
