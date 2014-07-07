#!/usr/bin/env python

#   AUTHOR  :   Avi Mehenwal
#   DATE    :   24th July 2014
#   PURPOSE :   Datetime manupulation with python


import datetime

date_format = "%m/%d/%Y %H:%M:%S"
a = datetime.datetime.today()
b = datetime.datetime.strptime('9/26/2008 17:31:32', date_format)
delta = b - a
print "In datetime.datetime Format \n", a, b
print "Delta Days   : ", delta.days
print "Not accurate : ", (delta).days * 24 * 60

# BUG: Doesnt gives accurate seconds when times are different
# FIX: Convert to same time format like Unix Timestamps


import time

# Current time in Tuple Format
print "\nTime tuple Old/Naive format date\n", a.timetuple()

# convert to unix timestamp
d1_ts = time.mktime(a.timetuple())
d2_ts = time.mktime(b.timetuple())

print "\nIn time.mktime Format \n", d1_ts, d2_ts

# they are now in seconds, subtract and then divide by 60 to get minutes.
print "Seconds Diff   : ", int(d2_ts-d1_ts) / 60



t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
secs = time.mktime( t )
print "time.mktime(t) :  %f" %  secs                                         # Float
print "asctime(localtime(secs)): %s" % time.asctime(time.localtime(secs))   # string
