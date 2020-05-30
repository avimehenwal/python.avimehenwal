#!/usr/bin/env python
 
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import time, os, subprocess, signal
 
def killXvfb():
	p = subprocess.Popen(['ps', '-A'], stdout=subprocess.PIPE)
	out, err = p.communicate()
 
	for line in out.splitlines():
		if 'Xvfb' in line:
			pid = int(line.split(None, 1)[0])
			os.kill(pid, signal.SIGKILL)
 
killXvfb()
os.system('/usr/bin/Xvfb :15 -ac -screen 0 1024x768x24 &')
os.environ['DISPLAY'] = 'localhost:15.0'
browser = webdriver.Firefox()
browser.delete_all_cookies()
timestart = time.time()
browser.get("http://en.mindinmotion.ru/")
timeend = time.time()
loadtime = timeend - timestart
print "Page loaded in: %(loadtime)d" % vars()
browser.close()
killXvfb()
