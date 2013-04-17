import sys
import time
#import pandas

print time.clock()

for i in range(10**4): 
	print "hello world",
	for j in range(2**4): 
		print j*i,
	print
	print time.clock()
