import sys
import re
output = open("testout.txt", "w")
output.write("Opening List: \n")
r=re.compile('[a-h]*')
for i in range(10):
	with open(sys.argv[1]) as inpuT:
		for line in inpuT:
			text=line.rstrip()
			good=r.match(text)
			if len(text)==i:
				if good is not None:
					if good.group()==text:
						output.write(text)
						output.write("\n")
	inpuT.close()
	#output.write(str(i)+" Moves:\n")

output.close()
