#!/usr/bin/env python
## Eagle Eye :: By Viss, with a lot of help from @achillean and others!
## To run this you'll need the shodan module as well as gevent.

# First things first, let's monkey patch Python to support greenthreads
from gevent import monkey
monkey.patch_all()

# Non-standard libraries that are being used
from gevent import joinall, sleep, spawn
from gevent.queue import Queue
from shodan import WebAPI

# Standard python stuff
import re
import socket
import sys
import time
import os

# Constants
API_KEY		= '<git yer own, theyre free!'
NUM_WORKERS	= 25
#del sys.argv[0]
#for arg in sys.argv:	
#	filter = " ".join(arg," ")

#filter = "org:amazon port:80"
filter = 'port:80 org:"Sony North America"' 
def checkCam(ip):
		print 'Checking %s...' % ip
		ipandport = ip.split()
		#port = ipandport[1]
		cmd = 'wkhtmltoimage-i386  --width 600 --load-error-handling ignore http://%s %s.png &' % (ip,ip)
		sleep(1)
		os.system(cmd)


def worker(queue):
	while 1:
		if queue.empty():
			sleep(5)
			continue

		ip = queue.get()
		checkCam(ip)


def main(queue):

	# Connect to Shodan
	api = WebAPI(API_KEY)

	# get the first page of results
	res = api.search(filter)

	#keep track of how many results we have left
	#total_results = res['total']
	total_results = res.get('total', 0)

	# Start looping through results now
	page = 1
	try:
		while(page * 100 <= total_results):
			#check the matches to see if they fit what we are looking for
			for host in res['matches']:
				queue.put_nowait(host['ip'])
			page +=1
			res = api.search(filter,page)
	except Exception, e:
		print e

	# Done querying Shodan, now wait for the queue to finish
	while not queue.empty():
		sleep(10)

	# Exit the program
	#sys.exit(0)


# Run the script if it's being executed
if __name__ == '__main__':
	print "You're searching for: %s" % filter
	# Create the worker queue that holds the potential webcams
	queue = Queue()

	# Spawn the main thread
	threads = [ spawn(main, queue) ]

	# Spawn the workers
	for i in range(NUM_WORKERS):
		threads.append(spawn(worker, queue))

	# Wait for the greenthreads to finish
	joinall(threads)
