#!/usr/bin/python

import os
import re
import urllib2
import socks
import socket

def list_all_files(dir):
    for root, dirs, files in os.walk(dir, topdown=False):
        for name in files:
            process_file(os.path.join(root, name))
        for name in dirs:
            list_all_files(os.path.join(root, name))

def process_file(file):
	if os.path.splitext(file)[1] == '.md':
			#print(file)
		f = open(file)
		lines = f.read()
		for url in re.findall(r"\!\[.+\]\((.+)\)", lines):
			#url = url.replace('//imgur.com','//i.imgur.com')
			#print('Downloading ' + url)
			#f = urllib2.urlopen(url) 
			filename = os.path.basename(url)
			newurl = '/asset/images/archive/'+filename
			#with open("/Users/yangzhiyong/Downloads/images/" + filename, "wb") as code:
			#	code.write(f.read())
			print(filename)
		f.close()
    

socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5, "127.0.0.1", 1086)
socket.socket = socks.socksocket
list_all_files('/Users/yangzhiyong/Repository/github/iyang/source/_posts')
